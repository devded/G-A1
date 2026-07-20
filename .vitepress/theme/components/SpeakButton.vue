<template>
  <span class="speak-wrap">
    <!-- Main speak button -->
    <button
      class="speak-btn"
      @click.stop="speak('normal')"
      :title="'Listen: ' + text"
      :aria-label="'Listen to ' + text"
      :class="{ playing: state === 'playing', loading: state === 'loading' }"
      type="button"
    >
      <span class="icon-inner">
        <svg v-if="state === 'playing'" class="wave-icon" viewBox="0 0 24 24" fill="currentColor">
          <rect x="2"  y="8"  width="3" height="8" rx="1.5" class="bar bar1"/>
          <rect x="7"  y="5"  width="3" height="14" rx="1.5" class="bar bar2"/>
          <rect x="12" y="3"  width="3" height="18" rx="1.5" class="bar bar3"/>
          <rect x="17" y="6"  width="3" height="12" rx="1.5" class="bar bar4"/>
        </svg>
        <svg v-else-if="state === 'loading'" class="spin-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>
        </svg>
        <svg v-else class="speaker-svg" viewBox="0 0 24 24" fill="currentColor">
          <path d="M11 5L6 9H2v6h4l5 4V5z"/>
          <path d="M15.54 8.46a5 5 0 0 1 0 7.07" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/>
          <path d="M19.07 4.93a10 10 0 0 1 0 14.14" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/>
        </svg>
      </span>
    </button>

    <!-- Slow mode button (shows on hover over the wrap) -->
    <button
      v-if="showSlow"
      class="speak-btn speak-slow-btn"
      @click.stop="speak('slow')"
      title="Listen slowly"
      aria-label="Listen slowly"
      :class="{ playing: state === 'slow-playing' }"
      type="button"
    >
      <span class="slow-label">🐢</span>
    </button>
  </span>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { withBase } from 'vitepress'

const props = defineProps({
  text:     { type: String, required: true },
  audioSrc: { type: String, default: '' },
  showSlow: { type: Boolean, default: true },
})

// state: idle | loading | playing | slow-playing | error
const state = ref('idle')
let currentAudio = null

// Slugify matches the Python generator exactly
function slugify(text) {
  if (!text) return ''
  let t = text.toLowerCase().trim()
  t = t.replace(/ae/g, 'ae2')
  t = t.replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
  t = t.replace(/á/g, 'a').replace(/é/g, 'e').replace(/ó/g, 'o').replace(/ú/g, 'u')
  t = t.replace(/[^a-z0-9]+/g, '_')
  t = t.replace(/^_+|_+$/g, '')
  if (t.length > 80) {
    // Can't do MD5 in browser without a lib — just truncate
    t = t.slice(0, 80)
  }
  return t
}

function audioUrl(text, slow = false) {
  const slug = slugify(text)
  const suffix = slow ? '_slow' : ''
  return withBase(`/audio/${slug}${suffix}.mp3`)
}

function speak(mode = 'normal') {
  const isSlow  = mode === 'slow'
  const busyStates = ['loading', 'playing', 'slow-playing']

  if (!props.text || busyStates.includes(state.value)) return

  // Stop any existing playback
  if (currentAudio) {
    currentAudio.pause()
    currentAudio = null
  }

  const url = audioUrl(props.text, isSlow)
  state.value = 'loading'

  const audio = new Audio(url)
  currentAudio = audio

  audio.addEventListener('canplaythrough', () => {
    state.value = isSlow ? 'slow-playing' : 'playing'
    audio.play().catch(() => fallback(isSlow))
  })

  audio.addEventListener('ended', () => {
    state.value = 'idle'
    currentAudio = null
  })

  audio.addEventListener('error', () => {
    // File not found — try Web Speech API fallback
    state.value = 'idle'
    currentAudio = null
    fallback(isSlow)
  })

  // Timeout: if no response in 3s, fall back
  setTimeout(() => {
    if (state.value === 'loading') {
      audio.pause()
      currentAudio = null
      fallback(isSlow)
    }
  }, 3000)
}

function fallback(slow = false) {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) return

  try {
    window.speechSynthesis.cancel()
    const utt  = new SpeechSynthesisUtterance(props.text)
    utt.lang   = 'de-DE'
    utt.rate   = slow ? 0.65 : 0.88
    utt.pitch  = 1.08
    utt.volume = 1

    const setVoice = () => {
      const voices = window.speechSynthesis.getVoices()
      const voice  = voices.find(v =>
        v.lang?.toLowerCase().includes('de') && (
          v.name.includes('Seraphina') ||
          v.name.includes('Amala') ||
          v.name.includes('Katja') ||
          v.name.includes('Google') ||
          v.name.includes('Natural') ||
          v.name.includes('Neural')
        )
      ) || voices.find(v => v.lang?.toLowerCase().includes('de'))

      if (voice) utt.voice = voice
      state.value = slow ? 'slow-playing' : 'playing'
      utt.onend   = () => { state.value = 'idle' }
      utt.onerror = () => { state.value = 'idle' }
      window.speechSynthesis.speak(utt)
    }

    const v = window.speechSynthesis.getVoices()
    if (v.length > 0) setVoice()
    else {
      window.speechSynthesis.onvoiceschanged = () => {
        setVoice()
        window.speechSynthesis.onvoiceschanged = null
      }
      setTimeout(setVoice, 150)
    }
  } catch {
    state.value = 'idle'
  }
}
</script>

<style scoped>
.speak-wrap {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  vertical-align: middle;
  margin-left: 5px;
}

.speak-btn {
  background: var(--vp-c-brand-soft, rgba(230,57,70,0.1));
  border: 1.5px solid var(--vp-c-brand-1, #e63946);
  color: var(--vp-c-brand-1, #e63946);
  border-radius: 50%;
  width: 30px;
  height: 30px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1);
  padding: 0;
  line-height: 1;
  flex-shrink: 0;
  position: relative;
  overflow: hidden;
}

.speak-btn::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: radial-gradient(circle, currentColor 0%, transparent 70%);
  opacity: 0;
  transform: scale(0);
  transition: all 0.3s ease;
}

.speak-btn:hover {
  background: var(--vp-c-brand-1, #e63946);
  color: #fff;
  transform: scale(1.1);
  box-shadow: 0 4px 14px rgba(230, 57, 70, 0.4);
}

.speak-btn.playing,
.speak-btn.loading {
  background: var(--vp-c-brand-1, #e63946);
  color: #fff;
  box-shadow: 0 0 0 3px rgba(230, 57, 70, 0.25);
}

.speak-slow-btn {
  width: 26px;
  height: 26px;
  font-size: 13px;
  opacity: 0;
  transform: scale(0.8);
  transition: all 0.2s ease;
  border-style: dashed;
}

.speak-wrap:hover .speak-slow-btn {
  opacity: 1;
  transform: scale(1);
}

.icon-inner {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 16px;
  height: 16px;
}

.speaker-svg,
.wave-icon,
.spin-icon {
  width: 16px;
  height: 16px;
}

/* Animated waveform bars when playing */
.wave-icon .bar {
  transform-origin: bottom;
  animation: wave-bounce 0.6s ease-in-out infinite alternate;
}
.wave-icon .bar1 { animation-delay: 0s;    }
.wave-icon .bar2 { animation-delay: 0.1s;  }
.wave-icon .bar3 { animation-delay: 0.2s;  }
.wave-icon .bar4 { animation-delay: 0.05s; }

@keyframes wave-bounce {
  0%   { transform: scaleY(0.4); }
  100% { transform: scaleY(1.0); }
}

/* Spinner for loading state */
.spin-icon {
  animation: spin 0.8s linear infinite;
}
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

.slow-label {
  font-size: 14px;
  line-height: 1;
}
</style>
