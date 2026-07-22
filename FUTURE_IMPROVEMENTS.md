# Future Improvements & Roadmap Suggestions

> A strategic list of recommended feature enhancements, UX upgrades, interactive tools, and CI/CD improvements for future iterations of the **German A1 Self-Study Course**.

---

## 1. 🚀 Interactive Web App & UX Enhancements

- [ ] **`localStorage` Progress Persistence**
  - *Current State:* Custom Vue components ([VocabQuiz.vue](.vitepress/theme/components/VocabQuiz.vue) and [FlipDeck.vue](.vitepress/theme/components/FlipDeck.vue)) reset state upon page refresh.
  - *Target:* Save completed flashcards, quiz scores, and daily checklist items in browser `localStorage` across study sessions.

- [ ] **Audio-on-Flip in Flashcards**
  - *Target:* Add an optional "Auto-play Audio" toggle in `FlipDeck.vue` so flipping a card automatically plays the native TTS audio clip.

- [ ] **PWA (Progressive Web App) Support**
  - *Target:* Integrate `@vitepwa/vitepress` to enable full offline study capabilities on mobile devices (iOS/Android) and desktop browsers.

---

## 2. 📝 Interactive Goethe A1 Examination Engine

- [ ] **Interactive Mock Exam Component (`MockExam.vue`)**
  - *Current State:* Mock exams in [Exams/Mock-Exam-01](Exams/Mock-Exam-01/README.md) and [Exams/Mock-Exam-02](Exams/Mock-Exam-02/README.md) are static Markdown files.
  - *Target:* Build an interactive exam component with:
    1. A 65-minute countdown timer (matching official Goethe A1 timing).
    2. Interactive radio-button selection for Listening (*Hören*), Reading (*Lesen*), and Writing (*Schreiben*).
    3. Instant grading out of 60 points with pass/fail feedback (60% threshold = 36 points).

---

## 3. 🎙️ Dictation & Shadowing Practice Tools

- [ ] **Interactive Dictation Widget (`DictationPractice.vue`)**
  - *Target:* 
    1. Play a sentence audio clip from `public/audio/`.
    2. Prompt student to type the German sentence.
    3. Compare input against target text and provide real-time character/word error diffs.

---

## 4. 🤖 CI/CD & Build Automation

- [ ] **Automate Python Renderer in GitHub Actions**
  - *Current State:* [.github/workflows/deploy.yml](.github/workflows/deploy.yml) only executes `npm run build`.
  - *Target:* Update the workflow to set up Python 3.11 and run `python3 run_build_all.py` before building VitePress, ensuring generated content is validated on every commit:
    ```yaml
    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Build Course Files
      run: python3 run_build_all.py

    - name: Build VitePress Site
      run: npm run build
    ```

- [ ] **Automated Audio Asset Validator**
  - *Target:* Add an audio asset check in `run_build_all.py` to verify that every vocabulary item's audio file exists in `public/audio/` and raise build warnings if clips are missing.

---

## Summary Roadmap Matrix

| Feature | Category | Difficulty | Impact | Status |
|:---|:---|:---:|:---:|:---:|
| **Progress Persistence (`localStorage`)** | UX / Web | Low | ⭐️⭐️⭐️⭐️⭐️ | Planned |
| **Interactive Mock Exam Engine** | Exams / Core | Medium | ⭐️⭐️⭐️⭐️⭐️ | Planned |
| **PWA Offline Support** | Mobile / UX | Low | ⭐️⭐️⭐️⭐️ | Planned |
| **Dictation / Audio Diff Widget** | Skills / Audio | Medium | ⭐️⭐️⭐️⭐️ | Planned |
| **CI Python Build Validation** | DevOps | Low | ⭐️⭐️⭐️ | Planned |
