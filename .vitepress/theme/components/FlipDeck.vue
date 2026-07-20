<template>
  <div class="flipdeck-container">
    <div class="flipdeck-header">
      <div>
        <div class="flipdeck-label"><Icon name="layers" /> Vocabulary Flash Cards</div>
        <div class="flipdeck-sub">Tap card to flip · <Icon name="volume-2" /> auto-plays on reveal</div>
      </div>
      <div class="flipdeck-progress">
        <span class="flipdeck-index">{{ currentIndex + 1 }} / {{ cards.length }}</span>
      </div>
    </div>

    <!-- Progress bar -->
    <div class="progress-bar-container" style="margin-bottom:16px">
      <div class="progress-bar-fill" :style="{ width: ((currentIndex + 1) / cards.length * 100) + '%' }"></div>
    </div>

    <!-- Card -->
    <div class="flip-card" :class="{ flipped: isFlipped }" @click="handleClick">
      <div class="flip-card-inner">
        <!-- Front: German -->
        <div class="flip-card-front">
          <div v-if="current.article" class="fc-article">{{ current.article }}</div>
          <div class="fc-word">{{ current.german }}</div>
          <div v-if="current.ipa" class="fc-ipa-front">/{{ current.ipa }}/</div>
          <div class="fc-hint">Tap to reveal →</div>
          <!-- Auto-play icon pulse when card first shown -->
          <div class="fc-autoplay-hint" v-if="!isFlipped"><Icon name="volume-2" /> Listening...</div>
        </div>
        <!-- Back: English + IPA + Example -->
        <div class="flip-card-back">
          <div class="fc-translation">{{ current.english }}</div>
          <div v-if="current.ipa" class="fc-ipa">{{ current.ipa }}</div>
          <div v-if="current.example" class="fc-example">"{{ current.example }}"</div>
          <div class="fc-back-listen" @click.stop="playAudio(current.example || current.german, false)">
            <Icon name="volume-2" /> Hear example
          </div>
        </div>
      </div>
    </div>

    <!-- Controls row -->
    <div class="flipdeck-controls">
      <div class="flipdeck-nav">
        <button class="fc-btn" @click.stop="prev" :disabled="currentIndex === 0">← Prev</button>
        <button class="fc-btn fc-btn-restart" @click.stop="restart">↩ Restart</button>
        <button class="fc-btn" @click.stop="next" :disabled="currentIndex === cards.length - 1">Next →</button>
      </div>
      <div class="flipdeck-listen-row">
        <button class="fc-listen-btn" @click.stop="playAudio(fullWord, false)" title="Normal speed">
          <Icon name="volume-2" /> Normal
        </button>
        <button class="fc-listen-btn fc-listen-slow" @click.stop="playAudio(fullWord, true)" title="Slow speed">
          <Icon name="volume-2" /> Slow
        </button>
      </div>
    </div>

    <div class="flipdeck-tip">
      <Icon name="lightbulb" /> Say the German word aloud before flipping!
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { withBase } from 'vitepress'

const props = defineProps({
  cards: { type: Array, required: true }
  // Each: { german, english, article?, ipa?, example? }
})

const currentIndex = ref(0)
const isFlipped    = ref(false)

const current  = computed(() => props.cards[currentIndex.value])
const fullWord = computed(() => {
  const c = current.value
  if (!c) return ''
  const w = (c.german || '').trim()
  const a = (c.article || '').trim()
  if (a && w.toLowerCase().startsWith(a.toLowerCase() + ' ')) {
    return w
  }
  return a ? `${a} ${w}` : w
})

// Auto-play word when card changes
watch(currentIndex, () => {
  isFlipped.value = false
  // Short delay so card is visible first
  setTimeout(() => playAudio(fullWord.value, false), 400)
})

function handleClick() {
  if (!isFlipped.value) {
    isFlipped.value = true
    // Play example when card flips to back
    setTimeout(() => {
      const text = current.value.example || current.value.german
      playAudio(text, false)
    }, 350)
  } else {
    next()
  }
}

function next() {
  if (currentIndex.value < props.cards.length - 1) {
    isFlipped.value = false
    setTimeout(() => { currentIndex.value++ }, 260)
  }
}
function prev() {
  if (currentIndex.value > 0) {
    isFlipped.value = false
    setTimeout(() => { currentIndex.value-- }, 260)
  }
}
function restart() {
  isFlipped.value = false
  setTimeout(() => { currentIndex.value = 0 }, 260)
}

// ── Audio ────────────────────────────────────────────────────
function slugify(text) {
  if (!text) return ''
  let t = text.toLowerCase().trim()
  t = t.replace(/ae/g, 'ae2')
  t = t.replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
  t = t.replace(/á/g, 'a').replace(/é/g, 'e').replace(/ó/g, 'o').replace(/ú/g, 'u')
  t = t.replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '')
  return t.length > 80 ? t.slice(0, 80) : t
}

let audioEl = null

function playAudio(text, slow = false) {
  if (!text) return
  if (audioEl) { audioEl.pause(); audioEl = null }

  const slug   = slugify(text)
  const suffix = slow ? '_slow' : ''
  const url    = withBase(`/audio/${slug}${suffix}.mp3`)

  const a = new Audio(url)
  audioEl = a
  a.play().catch(() => speechFallback(text, slow))
  a.onerror = () => speechFallback(text, slow)
}

function speechFallback(text, slow) {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) return
  window.speechSynthesis.cancel()
  const utt  = new SpeechSynthesisUtterance(text)
  utt.lang   = 'de-DE'
  utt.rate   = slow ? 0.65 : 0.88
  utt.pitch  = 1.08

  const go = () => {
    const v = window.speechSynthesis.getVoices()
    const pick = v.find(x =>
      x.lang?.toLowerCase().includes('de') && (
        x.name.includes('Seraphina') || x.name.includes('Amala') ||
        x.name.includes('Katja')     || x.name.includes('Natural')
      )
    ) || v.find(x => x.lang?.toLowerCase().includes('de'))
    if (pick) utt.voice = pick
    window.speechSynthesis.speak(utt)
  }

  const voices = window.speechSynthesis.getVoices()
  if (voices.length > 0) go()
  else {
    window.speechSynthesis.onvoiceschanged = () => { go(); window.speechSynthesis.onvoiceschanged = null }
    setTimeout(go, 150)
  }
}
</script>

<style scoped>
.flipdeck-container {
  background: var(--g-card-bg, var(--vp-c-bg-soft));
  border: 1px solid var(--g-card-border, var(--vp-c-divider));
  border-radius: 18px;
  padding: 22px 24px;
  margin: 1.5rem 0;
  box-shadow: var(--g-card-shadow, 0 4px 16px rgba(0,0,0,0.08));
}

.flipdeck-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}

.flipdeck-label {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #6366f1;
  margin-bottom: 2px;
}

.flipdeck-sub {
  font-size: 0.78rem;
  color: var(--vp-c-text-3);
}

.flipdeck-index {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--vp-c-text-2);
}

.flip-card {
  perspective: 1200px;
  height: 190px;
  cursor: pointer;
  margin-bottom: 16px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.55s cubic-bezier(0.4, 0, 0.2, 1);
  transform-style: preserve-3d;
}

.flip-card.flipped .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 5px;
  padding: 16px;
  text-align: center;
}

.flip-card-front {
  background: linear-gradient(135deg, #1d3557 0%, #274a72 100%);
  color: #fff;
  border-top: 3px solid var(--g-gold, #ffb703);
}

.flip-card-back {
  background: var(--vp-c-bg, #fff);
  border: 1px solid var(--vp-c-divider);
  border-top: 3px solid var(--g-gold, #ffb703);
  color: var(--vp-c-text-1);
  transform: rotateY(180deg);
}

.fc-word {
  font-size: 1.7rem;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.fc-article {
  font-size: 0.78rem;
  font-weight: 600;
  opacity: 0.85;
  background: rgba(255,255,255,0.2);
  padding: 2px 10px;
  border-radius: 100px;
}

.fc-ipa-front {
  font-size: 0.78rem;
  opacity: 0.75;
  font-style: italic;
}

.fc-hint {
  font-size: 0.72rem;
  opacity: 0.6;
  margin-top: 2px;
}

.fc-autoplay-hint {
  font-size: 0.68rem;
  opacity: 0.55;
  margin-top: 2px;
  animation: blink 1.5s ease-in-out infinite;
}

@keyframes blink {
  0%, 100% { opacity: 0.55; }
  50%       { opacity: 0.2; }
}

.fc-translation {
  font-size: 1.4rem;
  font-weight: 700;
}

.fc-ipa {
  font-size: 0.85rem;
  opacity: 0.8;
  font-family: 'JetBrains Mono', monospace;
}

.fc-example {
  font-size: 0.8rem;
  opacity: 0.8;
  font-style: italic;
  max-width: 88%;
  line-height: 1.4;
}

.fc-back-listen {
  font-size: 0.72rem;
  opacity: 0.7;
  cursor: pointer;
  margin-top: 4px;
  background: rgba(255,255,255,0.15);
  padding: 3px 10px;
  border-radius: 100px;
  transition: opacity 0.2s;
}
.fc-back-listen:hover { opacity: 1; }

.flipdeck-controls {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 12px;
}

.flipdeck-nav {
  display: flex;
  gap: 10px;
  justify-content: center;
}

.flipdeck-listen-row {
  display: flex;
  gap: 8px;
  justify-content: center;
}

.fc-btn, .fc-listen-btn {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-1);
  border-radius: 8px;
  padding: 8px 16px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.fc-btn:hover:not(:disabled),
.fc-listen-btn:hover {
  background: var(--vp-c-brand-soft, rgba(29, 53, 87, 0.09));
  border-color: var(--vp-c-brand-1, #1d3557);
  color: var(--vp-c-brand-1, #1d3557);
}

.fc-btn:disabled { opacity: 0.4; cursor: not-allowed; }

.fc-btn-restart {
  background: var(--vp-c-brand-soft, rgba(29, 53, 87, 0.09));
  border-color: var(--vp-c-brand-1, #1d3557);
  color: var(--vp-c-brand-1, #1d3557);
}

.fc-listen-slow {
  background: rgba(99, 102, 241, 0.08);
  border-color: #6366f1;
  color: #6366f1;
}

.flipdeck-tip {
  text-align: center;
  font-size: 0.76rem;
  color: var(--vp-c-text-3);
}
</style>
