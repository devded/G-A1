import DefaultTheme from 'vitepress/theme'
import { withBase } from 'vitepress'
import SpeakButton from './components/SpeakButton.vue'
import VocabQuiz from './components/VocabQuiz.vue'
import FlipDeck from './components/FlipDeck.vue'
import Icon from './components/Icon.vue'
import WeekCards from './components/WeekCards.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.config.globalProperties.$withBase = withBase
    app.component('SpeakButton', SpeakButton)
    app.component('VocabQuiz', VocabQuiz)
    app.component('FlipDeck', FlipDeck)
    app.component('Icon', Icon)
    app.component('WeekCards', WeekCards)
  }
}
