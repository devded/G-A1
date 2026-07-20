<template>
  <div class="quiz-container">
    <!-- Header -->
    <div class="quiz-header">
      <div>
        <div class="quiz-label">✏️ Vocabulary Quiz</div>
        <div class="quiz-sub">Question {{ currentIndex + 1 }} of {{ questions.length }}</div>
      </div>
      <div class="quiz-score-badge">
        <div class="quiz-score-num">{{ score }}</div>
        <div class="quiz-score-lbl">Score</div>
      </div>
    </div>

    <!-- Progress bar -->
    <div class="progress-bar-container" style="margin-bottom: 20px">
      <div class="progress-bar-fill" :style="{ width: progressPercent + '%' }"></div>
    </div>

    <!-- Finished state -->
    <div v-if="finished" class="quiz-finished">
      <div class="quiz-score-ring">
        <span class="quiz-score-big">{{ score }}/{{ questions.length }}</span>
      </div>
      <div class="quiz-finish-msg">
        <span v-if="score === questions.length">🎉 Perfect! Ausgezeichnet!</span>
        <span v-else-if="score >= questions.length * 0.7">✅ Sehr gut! Well done!</span>
        <span v-else>💪 Keep practising! Übung macht den Meister!</span>
      </div>
      <button class="quiz-retry-btn" @click="restart">↩ Try Again</button>
    </div>

    <!-- Active question -->
    <div v-else>
      <!-- Question with audio button -->
      <div class="quiz-question-row">
        <div class="quiz-question">{{ current.question }}</div>
        <button class="q-audio-btn" @click="playAudio(current.question)" title="Hear question">🔊</button>
      </div>

      <div class="quiz-options">
        <button
          v-for="(opt, i) in current.options"
          :key="i"
          class="quiz-option"
          :class="{
            correct: answered && opt === current.answer,
            wrong:   answered && opt === selected && opt !== current.answer
          }"
          @click="selectOption(opt)"
          :disabled="answered"
        >
          <span class="opt-letter">{{ 'ABCD'[i] }}</span>
          <span class="opt-text">{{ opt }}</span>
          <span v-if="answered && opt === current.answer" class="opt-tick">✅</span>
          <span v-else-if="answered && opt === selected && opt !== current.answer" class="opt-tick">❌</span>
        </button>
      </div>

      <!-- Feedback row -->
      <div v-if="answered" class="quiz-feedback" :class="isCorrect ? 'correct' : 'wrong'">
        <span v-if="isCorrect">✅ Richtig! Correct!</span>
        <span v-else>❌ Answer: <strong>{{ current.answer }}</strong></span>
        <!-- Play the correct answer aloud after answering -->
        <button class="q-audio-btn q-audio-ans" @click="playAudio(current.answer)" title="Hear answer">🔊</button>
      </div>

      <div v-if="answered" style="text-align:center;margin-top:14px">
        <button class="quiz-next-btn" @click="next">
          {{ currentIndex + 1 < questions.length ? 'Next →' : 'See Results' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

const props = defineProps({
  questions: { type: Array, required: true }
  // Each: { question: String, answer: String, options: String[] }
})

const currentIndex = ref(0)
const score        = ref(0)
const answered     = ref(false)
const selected     = ref(null)
const isCorrect    = ref(false)
const finished     = ref(false)

const current = computed(() => props.questions[currentIndex.value])
const progressPercent = computed(() =>
  finished.value ? 100 : (currentIndex.value / props.questions.length) * 100
)

function selectOption(opt) {
  if (answered.value) return
  selected.value = opt
  answered.value = true
  isCorrect.value = opt === current.value.answer
  if (isCorrect.value) {
    score.value++
    playCorrectSound()
  } else {
    playWrongSound()
  }
  // Auto-play correct answer text after a moment
  setTimeout(() => playAudio(current.value.answer), 500)
}

function next() {
  if (currentIndex.value + 1 >= props.questions.length) {
    finished.value = true
  } else {
    currentIndex.value++
    answered.value = false
    selected.value = null
    isCorrect.value = false
  }
}

function restart() {
  currentIndex.value = 0
  score.value        = 0
  answered.value     = false
  selected.value     = null
  isCorrect.value    = false
  finished.value     = false
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

function playAudio(text) {
  if (!text) return
  if (audioEl) { audioEl.pause(); audioEl = null }
  const a = new Audio(`/audio/${slugify(text)}.mp3`)
  audioEl = a
  a.play().catch(() => speechFallback(text))
  a.onerror = () => speechFallback(text)
}

function speechFallback(text) {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) return
  window.speechSynthesis.cancel()
  const utt = new SpeechSynthesisUtterance(text)
  utt.lang  = 'de-DE'
  utt.rate  = 0.88
  utt.pitch = 1.08
  const go = () => {
    const v = window.speechSynthesis.getVoices()
    const pick = v.find(x => x.lang?.toLowerCase().includes('de') && (
      x.name.includes('Seraphina') || x.name.includes('Amala') ||
      x.name.includes('Katja')     || x.name.includes('Natural')
    )) || v.find(x => x.lang?.toLowerCase().includes('de'))
    if (pick) utt.voice = pick
    window.speechSynthesis.speak(utt)
  }
  const vs = window.speechSynthesis.getVoices()
  if (vs.length > 0) go()
  else { window.speechSynthesis.onvoiceschanged = () => { go(); window.speechSynthesis.onvoiceschanged = null }; setTimeout(go, 150) }
}

// Tiny synthesized feedback tones
function playCorrectSound() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)()
    const osc = ctx.createOscillator()
    const gain = ctx.createGain()
    osc.connect(gain); gain.connect(ctx.destination)
    osc.frequency.value = 880; osc.type = 'sine'
    gain.gain.setValueAtTime(0.2, ctx.currentTime)
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.4)
    osc.start(); osc.stop(ctx.currentTime + 0.4)
  } catch {}
}

function playWrongSound() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)()
    const osc = ctx.createOscillator()
    const gain = ctx.createGain()
    osc.connect(gain); gain.connect(ctx.destination)
    osc.frequency.value = 220; osc.type = 'square'
    gain.gain.setValueAtTime(0.15, ctx.currentTime)
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.3)
    osc.start(); osc.stop(ctx.currentTime + 0.3)
  } catch {}
}
</script>

<style scoped>
.quiz-container {
  background: var(--g-card-bg, var(--vp-c-bg-soft));
  border: 1px solid var(--g-card-border, var(--vp-c-divider));
  border-radius: 18px;
  padding: 22px 24px;
  margin: 1.5rem 0;
  box-shadow: var(--g-card-shadow, 0 4px 16px rgba(0,0,0,0.08));
}

.quiz-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}

.quiz-label {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #3b82f6;
  margin-bottom: 2px;
}

.quiz-sub { font-size: 0.85rem; color: var(--vp-c-text-2); }

.quiz-score-badge { text-align: right; }
.quiz-score-num {
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--vp-c-brand-1);
}
.quiz-score-lbl {
  font-size: 0.7rem;
  color: var(--vp-c-text-3);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.quiz-question-row {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 18px;
}

.quiz-question {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  line-height: 1.5;
  flex: 1;
}

.q-audio-btn {
  background: rgba(59,130,246,0.1);
  border: 1px solid #3b82f6;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  flex-shrink: 0;
  transition: all 0.15s;
}
.q-audio-btn:hover { background: #3b82f6; }
.q-audio-ans {
  background: transparent;
  border-color: currentColor;
  color: inherit;
  width: 24px; height: 24px;
  margin-left: 8px;
}

.quiz-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-bottom: 14px;
}

@media (max-width: 500px) {
  .quiz-options { grid-template-columns: 1fr; }
}

.quiz-option {
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--vp-c-bg);
  border: 2px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 12px 14px;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--vp-c-text-1);
  cursor: pointer;
  text-align: left;
  transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1);
  font-family: inherit;
  min-height: 52px;
}

.quiz-option:hover:not(:disabled) {
  border-color: #3b82f6;
  background: rgba(59,130,246,0.06);
  transform: translateY(-1px);
}

.quiz-option:disabled { cursor: not-allowed; }

.quiz-option.correct {
  border-color: #22c55e;
  background: rgba(34,197,94,0.12);
  color: #16a34a;
}

.quiz-option.wrong {
  border-color: #ef4444;
  background: rgba(239,68,68,0.1);
  color: #dc2626;
}

.opt-letter {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--vp-c-brand-soft, rgba(230,57,70,0.1));
  color: var(--vp-c-brand-1, #e63946);
  font-size: 0.72rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.opt-text { flex: 1; }
.opt-tick { flex-shrink: 0; }

.quiz-feedback {
  border-radius: 10px;
  padding: 10px 16px;
  font-size: 0.9rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 4px;
}

.quiz-feedback.correct {
  background: rgba(34,197,94,0.12);
  color: #16a34a;
  border: 1px solid rgba(34,197,94,0.3);
}

.quiz-feedback.wrong {
  background: rgba(239,68,68,0.1);
  color: #dc2626;
  border: 1px solid rgba(239,68,68,0.25);
}

.quiz-finished {
  text-align: center;
  padding: 20px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.quiz-score-ring {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--vp-c-brand-1), #f4b942);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 24px rgba(230, 57, 70, 0.3);
}

.quiz-score-big { color:#fff; font-size:1.4rem; font-weight:800; }
.quiz-finish-msg { font-size:1.1rem; font-weight:700; color:var(--vp-c-text-1); }

.quiz-retry-btn, .quiz-next-btn {
  background: var(--vp-c-brand-1);
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 10px 24px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  font-family: inherit;
}

.quiz-retry-btn:hover, .quiz-next-btn:hover {
  background: #c1121f;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(230, 57, 70, 0.35);
}
</style>
