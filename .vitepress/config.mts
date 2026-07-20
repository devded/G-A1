import { defineConfig } from 'vitepress'

export default defineConfig({
  base: process.env.GITHUB_ACTIONS ? '/G-A1/' : '/',
  title: "German A1 Self-Study",
  description: "Zero to Goethe A1 in 12 weeks — 30 minutes/day, 8 vocabulary words daily, interactive practice, and full exam prep.",
  cleanUrls: true,
  lastUpdated: true,
  ignoreDeadLinks: true,

  rewrites: {
    'README.md': 'readme-overview.md',
    'Grammar/README.md': 'Grammar/index.md',
    'Vocabulary/README.md': 'Vocabulary/index.md',
    'Pronunciation/README.md': 'Pronunciation/index.md',
    'Listening/README.md': 'Listening/index.md',
    'Reading/README.md': 'Reading/index.md',
    'Speaking/README.md': 'Speaking/index.md',
    'Writing/README.md': 'Writing/index.md',
    'Exercises/README.md': 'Exercises/index.md',
    'CheatSheets/README.md': 'CheatSheets/index.md',
    'Exams/README.md': 'Exams/index.md',
    'Flashcards/README.md': 'Flashcards/index.md',
    'Resources/README.md': 'Resources/index.md',
    'Assets/README.md': 'Assets/index.md',
    'Exams/Mock-Exam-01/README.md': 'Exams/Mock-Exam-01/index.md',
    'Exams/Mock-Exam-02/README.md': 'Exams/Mock-Exam-02/index.md',
    'Exams/Speaking-Cards/README.md': 'Exams/Speaking-Cards/index.md',
    'Weeks/Week-01/README.md': 'Weeks/Week-01/index.md',
    'Weeks/Week-02/README.md': 'Weeks/Week-02/index.md',
    'Weeks/Week-03/README.md': 'Weeks/Week-03/index.md',
    'Weeks/Week-04/README.md': 'Weeks/Week-04/index.md',
    'Weeks/Week-05/README.md': 'Weeks/Week-05/index.md',
    'Weeks/Week-06/README.md': 'Weeks/Week-06/index.md',
    'Weeks/Week-07/README.md': 'Weeks/Week-07/index.md',
    'Weeks/Week-08/README.md': 'Weeks/Week-08/index.md',
    'Weeks/Week-09/README.md': 'Weeks/Week-09/index.md',
    'Weeks/Week-10/README.md': 'Weeks/Week-10/index.md',
    'Weeks/Week-11/README.md': 'Weeks/Week-11/index.md',
    'Weeks/Week-12/README.md': 'Weeks/Week-12/index.md'
  },

  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'German A1 — 30 Min/Day',
    nav: [
      { text: '🏠 Home', link: '/' },
      {
        text: '📋 Overview',
        items: [
          { text: 'Course Guide', link: '/COURSE_GUIDE' },
          { text: '12-Week Roadmap', link: '/ROADMAP' },
          { text: 'Study Plan (35 Min/Day)', link: '/STUDY_PLAN' },
          { text: 'Progress Tracker', link: '/PROGRESS_TRACKER' },
          { text: 'Course Manifest', link: '/COURSE_MANIFEST' },
          { text: 'FAQ', link: '/FAQ' },
          { text: 'Attribution & Sources', link: '/SOURCES_AND_ATTRIBUTION' },
          { text: 'Changelog', link: '/CHANGELOG' }
        ]
      },
      {
        text: '📅 12-Week Program',
        items: [
          { text: 'Week 1: Sounds & Greetings', link: '/Weeks/Week-01/Days/Day-01' },
          { text: 'Week 2: Personal Info & Identity', link: '/Weeks/Week-02/Days/Day-08' },
          { text: 'Week 3: Family & Possessives', link: '/Weeks/Week-03/Days/Day-15' },
          { text: 'Week 4: Home & Furniture', link: '/Weeks/Week-04/Days/Day-22' },
          { text: 'Week 5: Work & Numbers 0-100', link: '/Weeks/Week-05/Days/Day-29' },
          { text: 'Week 6: Time & Daily Routine', link: '/Weeks/Week-06/Days/Day-36' },
          { text: 'Week 7: Hobbies & Word Position', link: '/Weeks/Week-07/Days/Day-43' },
          { text: 'Week 8: Food & Accusative Case', link: '/Weeks/Week-08/Days/Day-50' },
          { text: 'Week 9: Dining Out & Preferences', link: '/Weeks/Week-09/Days/Day-57' },
          { text: 'Week 10: City, Directions & Dative', link: '/Weeks/Week-10/Days/Day-64' },
          { text: 'Week 11: Weather & Modal Verbs', link: '/Weeks/Week-11/Days/Day-71' },
          { text: 'Week 12: Health, Past Tense & Exams', link: '/Weeks/Week-12/Days/Day-78' }
        ]
      },
      {
        text: '📖 Core Modules',
        items: [
          { text: 'Grammar Reference (24 Topics)', link: '/Grammar/' },
          { text: 'Vocabulary Bank (950 Words)', link: '/Vocabulary/' },
          { text: 'Pronunciation & Phonetics', link: '/Pronunciation/' }
        ]
      },
      {
        text: '🎧 Skills',
        items: [
          { text: 'Listening Practice', link: '/Listening/' },
          { text: 'Reading Passages', link: '/Reading/' },
          { text: 'Speaking & Role Plays', link: '/Speaking/' },
          { text: 'Writing & Goethe Tasks', link: '/Writing/' }
        ]
      },
      {
        text: '📝 Practice & Tests',
        items: [
          { text: 'Cheat Sheets (12 Sheets)', link: '/CheatSheets/' },
          { text: 'Weekly Exercises', link: '/Exercises/' },
          { text: 'Exams & Mock Tests', link: '/Exams/' },
          { text: 'Flashcards (Anki Decks)', link: '/Flashcards/' },
          { text: 'Resources & Media', link: '/Resources/' }
        ]
      }
    ],

    sidebar: {
      '/Weeks/': [
        {
          text: '📅 Week 1: Sounds & Greetings',
          collapsed: false,
          items: [
            { text: 'Day 01 — Alphabet & Sounds', link: '/Weeks/Week-01/Days/Day-01' },
            { text: 'Day 02 — Basic Greetings', link: '/Weeks/Week-01/Days/Day-02' },
            { text: 'Day 03 — Spelling & Questions', link: '/Weeks/Week-01/Days/Day-03' },
            { text: 'Day 04 — Nouns & Definite Articles', link: '/Weeks/Week-01/Days/Day-04' },
            { text: 'Day 05 — Indefinite Articles & Negation', link: '/Weeks/Week-01/Days/Day-05' },
            { text: 'Day 06 — Numbers 0-20', link: '/Weeks/Week-01/Days/Day-06' },
            { text: 'Day 07 — Week 1 Review', link: '/Weeks/Week-01/Days/Day-07' }
          ]
        },
        {
          text: '📅 Week 2: Personal Info & Identity',
          collapsed: true,
          items: [
            { text: 'Day 08 — Introducing Yourself', link: '/Weeks/Week-02/Days/Day-08' },
            { text: 'Day 09 — Countries & Origin', link: '/Weeks/Week-02/Days/Day-09' },
            { text: 'Day 10 — Languages Spoken', link: '/Weeks/Week-02/Days/Day-10' },
            { text: 'Day 11 — City of Residence', link: '/Weeks/Week-02/Days/Day-11' },
            { text: 'Day 12 — Asking Others Info', link: '/Weeks/Week-02/Days/Day-12' },
            { text: 'Day 13 — Personal Forms', link: '/Weeks/Week-02/Days/Day-13' },
            { text: 'Day 14 — Week 2 Review', link: '/Weeks/Week-02/Days/Day-14' }
          ]
        },
        {
          text: '📅 Week 3: Family & Possessives',
          collapsed: true,
          items: [
            { text: 'Day 15 — Family Vocabulary', link: '/Weeks/Week-03/Days/Day-15' },
            { text: 'Day 16 — Possessive Mein & Dein', link: '/Weeks/Week-03/Days/Day-16' },
            { text: 'Day 17 — Possessive Sein & Ihr', link: '/Weeks/Week-03/Days/Day-17' },
            { text: 'Day 18 — Describing Family', link: '/Weeks/Week-03/Days/Day-18' },
            { text: 'Day 19 — Friends & People', link: '/Weeks/Week-03/Days/Day-19' },
            { text: 'Day 20 — Family Dialogue', link: '/Weeks/Week-03/Days/Day-20' },
            { text: 'Day 21 — Week 3 Review', link: '/Weeks/Week-03/Days/Day-21' }
          ]
        },
        {
          text: '📅 Week 4: Home & Furniture',
          collapsed: true,
          items: [
            { text: 'Day 22 — House & Apartment Rooms', link: '/Weeks/Week-04/Days/Day-22' },
            { text: 'Day 23 — Furniture Vocabulary', link: '/Weeks/Week-04/Days/Day-23' },
            { text: 'Day 24 — Plural Noun Endings', link: '/Weeks/Week-04/Days/Day-24' },
            { text: 'Day 25 — Verb Haben (To Have)', link: '/Weeks/Week-04/Days/Day-25' },
            { text: 'Day 26 — Verb Sein (To Be)', link: '/Weeks/Week-04/Days/Day-26' },
            { text: 'Day 27 — Describing Your Room', link: '/Weeks/Week-04/Days/Day-27' },
            { text: 'Day 28 — Week 4 Review', link: '/Weeks/Week-04/Days/Day-28' }
          ]
        },
        {
          text: '📅 Week 5: Work & Numbers 0-100',
          collapsed: true,
          items: [
            { text: 'Day 29 — Professions & Occupations', link: '/Weeks/Week-05/Days/Day-29' },
            { text: 'Day 30 — Workplace & Technology', link: '/Weeks/Week-05/Days/Day-30' },
            { text: 'Day 31 — Numbers 21 to 100', link: '/Weeks/Week-05/Days/Day-31' },
            { text: 'Day 32 — Asking & Giving Age', link: '/Weeks/Week-05/Days/Day-32' },
            { text: 'Day 33 — Telephone & Email', link: '/Weeks/Week-05/Days/Day-33' },
            { text: 'Day 34 — Talking About Your Job', link: '/Weeks/Week-05/Days/Day-34' },
            { text: 'Day 35 — Week 5 Review', link: '/Weeks/Week-05/Days/Day-35' }
          ]
        },
        {
          text: '📅 Week 6: Time & Daily Routine',
          collapsed: true,
          items: [
            { text: 'Day 36 — Clock Time (Official)', link: '/Weeks/Week-06/Days/Day-36' },
            { text: 'Day 37 — Clock Time (Informal)', link: '/Weeks/Week-06/Days/Day-37' },
            { text: 'Day 38 — Days & Months', link: '/Weeks/Week-06/Days/Day-38' },
            { text: 'Day 39 — Daily Routine Verbs', link: '/Weeks/Week-06/Days/Day-39' },
            { text: 'Day 40 — Separable Verbs (Aufstehen)', link: '/Weeks/Week-06/Days/Day-40' },
            { text: 'Day 41 — Meeting Schedules', link: '/Weeks/Week-06/Days/Day-41' },
            { text: 'Day 42 — Week 6 Review', link: '/Weeks/Week-06/Days/Day-42' }
          ]
        },
        {
          text: '📅 Week 7: Hobbies & Sentence Structure',
          collapsed: true,
          items: [
            { text: 'Day 43 — Hobbies & Sports', link: '/Weeks/Week-07/Days/Day-43' },
            { text: 'Day 44 — Regular Verb Conjugation', link: '/Weeks/Week-07/Days/Day-44' },
            { text: 'Day 45 — Position 2 Verb Rule', link: '/Weeks/Week-07/Days/Day-45' },
            { text: 'Day 46 — Expressing Likes (Gern)', link: '/Weeks/Week-07/Days/Day-46' },
            { text: 'Day 47 — Free Time Dialogue', link: '/Weeks/Week-07/Days/Day-47' },
            { text: 'Day 48 — Short Diary Entry', link: '/Weeks/Week-07/Days/Day-48' },
            { text: 'Day 49 — Week 7 Review', link: '/Weeks/Week-07/Days/Day-49' }
          ]
        },
        {
          text: '📅 Week 8: Food & Accusative Case',
          collapsed: true,
          items: [
            { text: 'Day 50 — Food & Fruits', link: '/Weeks/Week-08/Days/Day-50' },
            { text: 'Day 51 — Beverages & Drinks', link: '/Weeks/Week-08/Days/Day-51' },
            { text: 'Day 52 — Accusative Masculine (Einen)', link: '/Weeks/Week-08/Days/Day-52' },
            { text: 'Day 53 — Accusative Negation (Keinen)', link: '/Weeks/Week-08/Days/Day-53' },
            { text: 'Day 54 — Grocery Prices', link: '/Weeks/Week-08/Days/Day-54' },
            { text: 'Day 55 — Supermarket Dialogue', link: '/Weeks/Week-08/Days/Day-55' },
            { text: 'Day 56 — Week 8 Review', link: '/Weeks/Week-08/Days/Day-56' }
          ]
        },
        {
          text: '📅 Week 9: Dining Out & Preferences',
          collapsed: true,
          items: [
            { text: 'Day 57 — Restaurant Menu', link: '/Weeks/Week-09/Days/Day-57' },
            { text: 'Day 58 — Ordering Food', link: '/Weeks/Week-09/Days/Day-58' },
            { text: 'Day 59 — Asking for the Bill', link: '/Weeks/Week-09/Days/Day-59' },
            { text: 'Day 60 — Verb Mögen & Möchte', link: '/Weeks/Week-09/Days/Day-60' },
            { text: 'Day 61 — Preferences', link: '/Weeks/Week-09/Days/Day-61' },
            { text: 'Day 62 — Dining Out Dialogue', link: '/Weeks/Week-09/Days/Day-62' },
            { text: 'Day 63 — Week 9 Review', link: '/Weeks/Week-09/Days/Day-63' }
          ]
        },
        {
          text: '📅 Week 10: City, Directions & Dative',
          collapsed: true,
          items: [
            { text: 'Day 64 — City Places', link: '/Weeks/Week-10/Days/Day-64' },
            { text: 'Day 65 — Asking Directions (Wo ist...?)', link: '/Weeks/Week-10/Days/Day-65' },
            { text: 'Day 66 — Giving Directions', link: '/Weeks/Week-10/Days/Day-66' },
            { text: 'Day 67 — Public Transportation', link: '/Weeks/Week-10/Days/Day-67' },
            { text: 'Day 68 — Basic Dative Case (Dem, Der)', link: '/Weeks/Week-10/Days/Day-68' },
            { text: 'Day 69 — Dative Prepositions', link: '/Weeks/Week-10/Days/Day-69' },
            { text: 'Day 70 — Week 10 Review', link: '/Weeks/Week-10/Days/Day-70' }
          ]
        },
        {
          text: '📅 Week 11: Weather & Modal Verbs',
          collapsed: true,
          items: [
            { text: 'Day 71 — Weather & Seasons', link: '/Weeks/Week-11/Days/Day-71' },
            { text: 'Day 72 — Clothing & Colors', link: '/Weeks/Week-11/Days/Day-72' },
            { text: 'Day 73 — Modal Verb Können (Can)', link: '/Weeks/Week-11/Days/Day-73' },
            { text: 'Day 74 — Modal Verb Müssen (Must)', link: '/Weeks/Week-11/Days/Day-74' },
            { text: 'Day 75 — Modal Verb Wollen & Sollen', link: '/Weeks/Week-11/Days/Day-75' },
            { text: 'Day 76 — Describing Personality', link: '/Weeks/Week-11/Days/Day-76' },
            { text: 'Day 77 — Week 11 Review', link: '/Weeks/Week-11/Days/Day-77' }
          ]
        },
        {
          text: '📅 Week 12: Health, Past Tense & Exams',
          collapsed: true,
          items: [
            { text: 'Day 78 — Body Parts & Symptoms', link: '/Weeks/Week-12/Days/Day-78' },
            { text: 'Day 79 — Doctor Appointment', link: '/Weeks/Week-12/Days/Day-79' },
            { text: 'Day 80 — Past Tense (Perfekt mit Haben)', link: '/Weeks/Week-12/Days/Day-80' },
            { text: 'Day 81 — Past Tense (Perfekt mit Sein)', link: '/Weeks/Week-12/Days/Day-81' },
            { text: 'Day 82 — Goethe A1 Exam Overview', link: '/Weeks/Week-12/Days/Day-82' },
            { text: 'Day 83 — Full Mock Practice Check', link: '/Weeks/Week-12/Days/Day-83' },
            { text: 'Day 84 — Course Completion & Celebration', link: '/Weeks/Week-12/Days/Day-84' }
          ]
        }
      ],

      '/Grammar/': [
        {
          text: '📐 Grammar Overview',
          items: [{ text: 'Grammar Index & System', link: '/Grammar/' }]
        },
        {
          text: 'Core Lessons (01 - 12)',
          items: [
            { text: '01 Nouns, Articles & Gender', link: '/Grammar/01-Nouns-Articles-and-Gender' },
            { text: '02 Plural Forms', link: '/Grammar/02-Plural-Forms' },
            { text: '03 Personal Pronouns', link: '/Grammar/03-Personal-Pronouns' },
            { text: '04 Sein and Haben', link: '/Grammar/04-Sein-and-Haben' },
            { text: '05 Present Tense Regular Verbs', link: '/Grammar/05-Present-Tense-Regular-Verbs' },
            { text: '06 Present Tense Irregular Verbs', link: '/Grammar/06-Present-Tense-Irregular-Verbs' },
            { text: '07 Sentence Structure & Verb Position', link: '/Grammar/07-Sentence-Structure-and-Verb-Position' },
            { text: '08 Questions', link: '/Grammar/08-Questions' },
            { text: '09 Negation', link: '/Grammar/09-Negation' },
            { text: '10 Nominative Case', link: '/Grammar/10-Nominative-Case' },
            { text: '11 Accusative Case', link: '/Grammar/11-Accusative-Case' },
            { text: '12 Basic Dative Case', link: '/Grammar/12-Basic-Dative-Case' }
          ]
        },
        {
          text: 'Advanced A1 Lessons (13 - 24)',
          items: [
            { text: '13 Possessive Determiners', link: '/Grammar/13-Possessive-Determiners' },
            { text: '14 Modal Verbs', link: '/Grammar/14-Modal-Verbs' },
            { text: '15 Separable Verbs', link: '/Grammar/15-Separable-Verbs' },
            { text: '16 Prepositions', link: '/Grammar/16-Prepositions' },
            { text: '17 Conjunctions', link: '/Grammar/17-Conjunctions' },
            { text: '18 Adjectives', link: '/Grammar/18-Adjectives' },
            { text: '19 Basic Comparisons', link: '/Grammar/19-Basic-Comparisons' },
            { text: '20 Numbers, Dates and Time', link: '/Grammar/20-Numbers-Dates-and-Time' },
            { text: '21 Commands and Polite Requests', link: '/Grammar/21-Commands-and-Polite-Requests' },
            { text: '22 Basic Perfect Tense', link: '/Grammar/22-Basic-Perfect-Tense' },
            { text: '23 Common A1 Grammar Mistakes', link: '/Grammar/23-Common-A1-Grammar-Mistakes' },
            { text: '24 Final Grammar Review', link: '/Grammar/24-Final-Grammar-Review' }
          ]
        }
      ],

      '/Vocabulary/': [
        {
          text: '📙 Vocabulary Overview',
          items: [
            { text: 'Vocabulary Hub', link: '/Vocabulary/' },
            { text: 'Master Vocabulary List', link: '/Vocabulary/MASTER_VOCABULARY' },
            { text: 'Revision Schedule', link: '/Vocabulary/VOCABULARY_REVISION_SCHEDULE' }
          ]
        },
        {
          text: 'Topic Lists (01 - 10)',
          items: [
            { text: '01 Greetings & Introductions', link: '/Vocabulary/01-Greetings-and-Introductions' },
            { text: '02 Numbers, Dates & Time', link: '/Vocabulary/02-Numbers-Dates-and-Time' },
            { text: '03 Countries, Languages & Nationalities', link: '/Vocabulary/03-Countries-Languages-and-Nationalities' },
            { text: '04 Colors & Descriptions', link: '/Vocabulary/04-Colors-and-Descriptions' },
            { text: '05 Family & People', link: '/Vocabulary/05-Family-and-People' },
            { text: '06 House, Rooms & Furniture', link: '/Vocabulary/06-House-Rooms-and-Furniture' },
            { text: '07 Jobs, School & Technology', link: '/Vocabulary/07-Jobs-School-and-Technology' },
            { text: '08 Daily Routine', link: '/Vocabulary/08-Daily-Routine' },
            { text: '09 Hobbies & Sports', link: '/Vocabulary/09-Hobbies-and-Sports' },
            { text: '10 Food & Drinks', link: '/Vocabulary/10-Food-and-Drinks' }
          ]
        },
        {
          text: 'Topic Lists (11 - 20)',
          items: [
            { text: '11 Restaurants', link: '/Vocabulary/11-Restaurants' },
            { text: '12 Shopping & Quantities', link: '/Vocabulary/12-Shopping-and-Quantities' },
            { text: '13 Clothing', link: '/Vocabulary/13-Clothing' },
            { text: '14 City & Directions', link: '/Vocabulary/14-City-and-Directions' },
            { text: '15 Travel & Transportation', link: '/Vocabulary/15-Travel-and-Transportation' },
            { text: '16 Weather & Nature', link: '/Vocabulary/16-Weather-and-Nature' },
            { text: '17 Animals', link: '/Vocabulary/17-Animals' },
            { text: '18 Health & Body', link: '/Vocabulary/18-Health-and-Body' },
            { text: '19 Emergencies & Services', link: '/Vocabulary/19-Emergencies-and-Services' },
            { text: '20 Communication Repair Phrases', link: '/Vocabulary/20-Communication-Repair-Phrases' }
          ]
        }
      ],

      '/Pronunciation/': [
        {
          text: '🗣️ Pronunciation Guides',
          items: [
            { text: 'Pronunciation Overview', link: '/Pronunciation/' },
            { text: '01 German Alphabet', link: '/Pronunciation/01-German-Alphabet' },
            { text: '02 IPA for Beginners', link: '/Pronunciation/02-IPA-for-Beginners' },
            { text: '03 German Vowels', link: '/Pronunciation/03-German-Vowels' },
            { text: '04 Umlauts', link: '/Pronunciation/04-Umlauts' },
            { text: '05 German Consonants', link: '/Pronunciation/05-German-Consonants' },
            { text: '06 Letter Combinations', link: '/Pronunciation/06-Letter-Combinations' },
            { text: '07 CH, R & Challenging Sounds', link: '/Pronunciation/07-CH-R-and-Other-Challenging-Sounds' },
            { text: '08 Word Stress', link: '/Pronunciation/08-Word-Stress' },
            { text: '09 Sentence Stress & Intonation', link: '/Pronunciation/09-Sentence-Stress-and-Intonation' },
            { text: '10 Bengali Speaker Challenges', link: '/Pronunciation/10-Bengali-Speaker-Challenges' },
            { text: '11 Shadowing Guide', link: '/Pronunciation/11-Shadowing-Guide' },
            { text: '12 Pronunciation Self-Test', link: '/Pronunciation/12-Pronunciation-Self-Test' }
          ]
        }
      ],

      '/Listening/': [
        {
          text: '🎧 Listening Module',
          items: [
            { text: 'Listening Overview', link: '/Listening/' },
            { text: 'Listening Roadmap', link: '/Listening/LISTENING_ROADMAP' },
            { text: 'Beginner Dialogues', link: '/Listening/BEGINNER_DIALOGUES' },
            { text: 'Phone & Appointment Practice', link: '/Listening/PHONE_AND_APPOINTMENT_PRACTICE' },
            { text: 'Announcement Practice', link: '/Listening/ANNOUNCEMENT_PRACTICE' },
            { text: 'Dictation Exercises', link: '/Listening/DICTATION_EXERCISES' },
            { text: 'Listening Log', link: '/Listening/LISTENING_LOG' },
            { text: 'All Audio Scripts', link: '/Assets/Audio-Scripts/ALL_SCRIPTS' }
          ]
        }
      ],

      '/Reading/': [
        {
          text: '📑 Reading Module',
          items: [
            { text: 'Reading Overview', link: '/Reading/' },
            { text: '01 Words and Signs', link: '/Reading/01-Words-and-Signs' },
            { text: '02 Simple Sentences', link: '/Reading/02-Simple-Sentences' },
            { text: '03 Everyday Dialogues', link: '/Reading/03-Everyday-Dialogues' },
            { text: '04 Messages and Forms', link: '/Reading/04-Messages-and-Forms' },
            { text: '05 Short Stories', link: '/Reading/05-Short-Stories' },
            { text: '06 Simple Articles', link: '/Reading/06-Simple-Articles' },
            { text: '07 A1 Exam Passages', link: '/Reading/07-A1-Exam-Passages' }
          ]
        }
      ],

      '/Speaking/': [
        {
          text: '🎙️ Speaking Module',
          items: [
            { text: 'Speaking Overview', link: '/Speaking/' },
            { text: 'Speaking Roadmap', link: '/Speaking/SPEAKING_ROADMAP' },
            { text: 'Self Introduction', link: '/Speaking/SELF_INTRODUCTION' },
            { text: 'Q&A Bank (100+ Questions)', link: '/Speaking/QUESTION_AND_ANSWER_BANK' },
            { text: 'Speaking Alone Protocol', link: '/Speaking/SPEAKING_ALONE' },
            { text: 'Picture Description', link: '/Speaking/PICTURE_DESCRIPTION' },
            { text: 'Role Plays & Dialogues', link: '/Speaking/ROLE_PLAYS' },
            { text: 'Weekly Checkpoints', link: '/Speaking/WEEKLY_CHECKPOINTS' },
            { text: 'AI Conversation Partner Guide', link: '/Speaking/AI_CONVERSATION_GUIDE' }
          ]
        }
      ],

      '/Writing/': [
        {
          text: '✍️ Writing Module',
          items: [
            { text: 'Writing Overview', link: '/Writing/' },
            { text: 'Writing Roadmap', link: '/Writing/WRITING_ROADMAP' },
            { text: 'Sentence Building Patterns', link: '/Writing/SENTENCE_BUILDING' },
            { text: 'Forms & Personal Information', link: '/Writing/FORMS_AND_PERSONAL_INFORMATION' },
            { text: 'Messages & Emails', link: '/Writing/MESSAGES_AND_EMAILS' },
            { text: 'Paragraph Writing', link: '/Writing/PARAGRAPH_WRITING' },
            { text: 'Goethe A1 Writing Tasks', link: '/Writing/GOETHE_A1_WRITING_TASKS' },
            { text: 'Diary Prompts', link: '/Writing/DIARY_PROMPTS' },
            { text: 'Self-Correction Checklist', link: '/Writing/SELF_CORRECTION_CHECKLIST' }
          ]
        }
      ],

      '/Exercises/': [
        {
          text: '🎯 Exercises Hub',
          items: [{ text: 'Exercises Index', link: '/Exercises/' }]
        },
        {
          text: 'Vocabulary Exercises',
          items: [
            { text: 'Week 1 Vocabulary', link: '/Exercises/Vocabulary/Week-01' },
            { text: 'Week 2 Vocabulary', link: '/Exercises/Vocabulary/Week-02' },
            { text: 'Week 3 Vocabulary', link: '/Exercises/Vocabulary/Week-03' },
            { text: 'Week 4 Vocabulary', link: '/Exercises/Vocabulary/Week-04' },
            { text: 'Week 5 Vocabulary', link: '/Exercises/Vocabulary/Week-05' },
            { text: 'Week 6 Vocabulary', link: '/Exercises/Vocabulary/Week-06' },
            { text: 'Week 7 Vocabulary', link: '/Exercises/Vocabulary/Week-07' },
            { text: 'Week 8 Vocabulary', link: '/Exercises/Vocabulary/Week-08' }
          ]
        },
        {
          text: 'Reading Exercises',
          items: [
            { text: 'Week 1 Reading', link: '/Exercises/Reading/Week-01' },
            { text: 'Week 2 Reading', link: '/Exercises/Reading/Week-02' },
            { text: 'Week 3 Reading', link: '/Exercises/Reading/Week-03' },
            { text: 'Week 4 Reading', link: '/Exercises/Reading/Week-04' },
            { text: 'Week 5 Reading', link: '/Exercises/Reading/Week-05' },
            { text: 'Week 6 Reading', link: '/Exercises/Reading/Week-06' },
            { text: 'Week 7 Reading', link: '/Exercises/Reading/Week-07' },
            { text: 'Week 8 Reading', link: '/Exercises/Reading/Week-08' }
          ]
        },
        {
          text: 'Dictation Exercises',
          items: [
            { text: 'Week 1 Dictation', link: '/Exercises/Dictation/Week-01' },
            { text: 'Week 2 Dictation', link: '/Exercises/Dictation/Week-02' },
            { text: 'Week 3 Dictation', link: '/Exercises/Dictation/Week-03' },
            { text: 'Week 4 Dictation', link: '/Exercises/Dictation/Week-04' },
            { text: 'Week 5 Dictation', link: '/Exercises/Dictation/Week-05' },
            { text: 'Week 6 Dictation', link: '/Exercises/Dictation/Week-06' },
            { text: 'Week 7 Dictation', link: '/Exercises/Dictation/Week-07' },
            { text: 'Week 8 Dictation', link: '/Exercises/Dictation/Week-08' }
          ]
        },
        {
          text: 'Mixed Revision',
          items: [
            { text: 'Week 1 Revision', link: '/Exercises/Mixed-Revision/Week-01' },
            { text: 'Week 2 Revision', link: '/Exercises/Mixed-Revision/Week-02' },
            { text: 'Week 3 Revision', link: '/Exercises/Mixed-Revision/Week-03' },
            { text: 'Week 4 Revision', link: '/Exercises/Mixed-Revision/Week-04' },
            { text: 'Week 5 Revision', link: '/Exercises/Mixed-Revision/Week-05' },
            { text: 'Week 6 Revision', link: '/Exercises/Mixed-Revision/Week-06' },
            { text: 'Week 7 Revision', link: '/Exercises/Mixed-Revision/Week-07' },
            { text: 'Week 8 Revision', link: '/Exercises/Mixed-Revision/Week-08' }
          ]
        }
      ],

      '/CheatSheets/': [
        {
          text: '📑 Quick Reference Cheat Sheets',
          items: [
            { text: 'Cheat Sheets Overview', link: '/CheatSheets/' },
            { text: 'Articles and Cases', link: '/CheatSheets/ARTICLES_AND_CASES' },
            { text: 'Numbers, Dates & Time', link: '/CheatSheets/NUMBERS_DATES_AND_TIME' },
            { text: 'Question Words', link: '/CheatSheets/QUESTION_WORDS' },
            { text: 'Pronouns', link: '/CheatSheets/PRONOUNS' },
            { text: 'Verb Conjugation', link: '/CheatSheets/VERB_CONJUGATION' },
            { text: 'Separable Verbs', link: '/CheatSheets/SEPARABLE_VERBS' },
            { text: 'Modal Verbs', link: '/CheatSheets/MODAL_VERBS' },
            { text: 'Prepositions', link: '/CheatSheets/PREPOSITIONS' },
            { text: 'Word Order', link: '/CheatSheets/WORD_ORDER' },
            { text: 'Survival Phrases', link: '/CheatSheets/SURVIVAL_PHRASES' },
            { text: 'Exam Day Checklist', link: '/CheatSheets/EXAM_DAY_CHECKLIST' }
          ]
        }
      ],

      '/Exams/': [
        {
          text: '🧪 Exams & Mock Tests',
          items: [
            { text: 'Exam Preparation Plan', link: '/Exams/EXAM_PREPARATION_PLAN' },
            { text: 'Goethe A1 Exam Guide', link: '/Exams/GOETHE_A1_GUIDE' },
            { text: 'TELC A1 Exam Guide', link: '/Exams/TELC_A1_GUIDE' },
            { text: 'ÖSD A1 Exam Guide', link: '/Exams/OESD_A1_GUIDE' },
            { text: 'Exam Comparison', link: '/Exams/EXAM_COMPARISON' },
            { text: 'Exam Readiness Tracker', link: '/Exams/EXAM_READINESS_TRACKER' },
            { text: 'Speaking Cards Bank', link: '/Exams/Speaking-Cards/' }
          ]
        },
        {
          text: '📝 Mock Exam 01',
          items: [
            { text: 'Mock Exam 01 Hub', link: '/Exams/Mock-Exam-01/' },
            { text: 'Listening Section', link: '/Exams/Mock-Exam-01/Listening' },
            { text: 'Reading Section', link: '/Exams/Mock-Exam-01/Reading' },
            { text: 'Writing Section', link: '/Exams/Mock-Exam-01/Writing' },
            { text: 'Speaking Section', link: '/Exams/Mock-Exam-01/Speaking' },
            { text: 'Answer Key & Explanations', link: '/Exams/Answer-Keys/Mock-01-Answers' }
          ]
        },
        {
          text: '📝 Mock Exam 02',
          items: [
            { text: 'Mock Exam 02 Hub', link: '/Exams/Mock-Exam-02/' },
            { text: 'Listening Section', link: '/Exams/Mock-Exam-02/Listening' },
            { text: 'Reading Section', link: '/Exams/Mock-Exam-02/Reading' },
            { text: 'Writing Section', link: '/Exams/Mock-Exam-02/Writing' },
            { text: 'Speaking Section', link: '/Exams/Mock-Exam-02/Speaking' },
            { text: 'Answer Key & Explanations', link: '/Exams/Answer-Keys/Mock-02-Answers' }
          ]
        }
      ],

      '/Flashcards/': [
        {
          text: '🎴 Flashcards & Anki Decks',
          items: [
            { text: 'Flashcards Hub', link: '/Flashcards/' },
            { text: 'Anki Import Guide', link: '/Flashcards/ANKI_IMPORT_GUIDE' }
          ]
        }
      ],

      '/Resources/': [
        {
          text: '📚 Resources & Media',
          items: [
            { text: 'Resources Hub', link: '/Resources/' },
            { text: 'Core Resources', link: '/Resources/CORE_RESOURCES' },
            { text: 'Apps & Flashcards', link: '/Resources/APPS_AND_FLASHCARDS' },
            { text: 'Dictionaries & Translation', link: '/Resources/DICTIONARIES_AND_TRANSLATION' },
            { text: 'Free PDFs & Exercises', link: '/Resources/FREE_PDFS_AND_EXERCISES' },
            { text: 'Listening Resources', link: '/Resources/LISTENING_RESOURCES' },
            { text: 'Pronunciation Resources', link: '/Resources/PRONUNCIATION_RESOURCES' },
            { text: 'Resource Usage Schedule', link: '/Resources/RESOURCE_USAGE_SCHEDULE' },
            { text: 'YouTube Channels & Podcasts', link: '/Resources/YOUTUBE_AND_PODCASTS' }
          ]
        },
        {
          text: '📁 Assets & Templates',
          items: [
            { text: 'Assets Overview', link: '/Assets/' },
            { text: 'All Audio Scripts', link: '/Assets/Audio-Scripts/ALL_SCRIPTS' },
            { text: 'Printable Daily Tracker', link: '/Assets/Printable-Trackers/DAILY_TRACKER' },
            { text: 'Daily Lesson Template', link: '/Assets/Templates/DAILY_LESSON_TEMPLATE' },
            { text: 'Error Log Template', link: '/Assets/Templates/ERROR_LOG_TEMPLATE' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com' }
    ],

    search: {
      provider: 'local'
    },

    footer: {
      message: 'Released under CC BY-SA 4.0 License.',
      copyright: 'German A1 Self-Study Course'
    }
  }
})
