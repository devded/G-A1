<template>
  <div class="week-cards">
    <a
      v-for="week in weeks"
      :key="week.num"
      :href="withBase(week.link)"
      class="week-card"
    >
      <div class="week-badge">{{ week.days }}</div>
      <div class="week-num">Week {{ week.num }}</div>
      <div class="week-title">{{ week.title }}</div>
      <div class="week-meta">
        <span>{{ week.words }} words</span>
        <span>·</span>
        <span>Grammar: {{ week.grammar }}</span>
      </div>
    </a>
  </div>
</template>

<script setup>
import { withBase } from 'vitepress'

const weeks = [
  {
    num: 1,
    days: 'Days 1–7',
    title: 'Alphabet, Sounds & Greetings',
    words: 56,
    grammar: 'Nouns, Articles',
    link: '/Weeks/Week-01/Days/Day-01'
  },
  {
    num: 2,
    days: 'Days 8–14',
    title: 'Personal Info & Identity',
    words: 56,
    grammar: 'sein, Pronouns',
    link: '/Weeks/Week-02/Days/Day-08'
  },
  {
    num: 3,
    days: 'Days 15–21',
    title: 'Family & Possessives',
    words: 56,
    grammar: 'mein/dein/sein',
    link: '/Weeks/Week-03/Days/Day-15'
  },
  {
    num: 4,
    days: 'Days 22–28',
    title: 'Home, Rooms & Furniture',
    words: 56,
    grammar: 'haben, Plurals',
    link: '/Weeks/Week-04/Days/Day-22'
  },
  {
    num: 5,
    days: 'Days 29–35',
    title: 'Jobs, School & Numbers',
    words: 56,
    grammar: 'Regular Verbs',
    link: '/Weeks/Week-05/Days/Day-29'
  },
  {
    num: 6,
    days: 'Days 36–42',
    title: 'Time, Dates & Daily Routine',
    words: 56,
    grammar: 'Separable Verbs',
    link: '/Weeks/Week-06/Days/Day-36'
  },
  {
    num: 7,
    days: 'Days 43–49',
    title: 'Hobbies, Sports & Sentence Structure',
    words: 56,
    grammar: 'Word Order (V2)',
    link: '/Weeks/Week-07/Days/Day-43'
  },
  {
    num: 8,
    days: 'Days 50–56',
    title: 'Food, Drinks & Accusative Case',
    words: 56,
    grammar: 'Accusative',
    link: '/Weeks/Week-08/Days/Day-50'
  },
  {
    num: 9,
    days: 'Days 57–63',
    title: 'City, Transport & Directions',
    words: 56,
    grammar: 'Contractions (im/am/zum)',
    link: '/Weeks/Week-09/Days/Day-57'
  },
  {
    num: 10,
    days: 'Days 64–70',
    title: 'Weather, Seasons & Modal Verbs',
    words: 56,
    grammar: 'Modal Verbs (können/müssen)',
    link: '/Weeks/Week-10/Days/Day-64'
  },
  {
    num: 11,
    days: 'Days 71–77',
    title: 'Health & Present Perfect Tense',
    words: 56,
    grammar: 'Perfekt (haben/sein)',
    link: '/Weeks/Week-11/Days/Day-71'
  },
  {
    num: 12,
    days: 'Days 78–84',
    title: 'Goethe A1 Exam Prep & Mock Exams',
    words: 56,
    grammar: 'Perfekt + Mock Exams',
    link: '/Weeks/Week-12/Days/Day-78'
  }
]
</script>
