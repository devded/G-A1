# Week 5 Data

w5 = {
    "weekNum": 5,
    "title": "Time, Days & Daily Routine",
    "level": "A1.2",
    "goal": "Tell time (official & informal), name days and months, describe your full daily routine with separable verbs, and master V2 word order with time expressions.",
    "days": [
        {
            "dayNum": 29, "title": "Official Clock Time (24h System)",
            "vocab": [
                {"word": "die Uhr", "article": "die", "badge": "noun", "translation": "the clock / o'clock", "ipa": "/uːɐ/", "ex": "Es ist 8 Uhr.", "exEn": "It is 8 o'clock."},
                {"word": "die Minute", "article": "die", "badge": "noun", "translation": "the minute", "ipa": "/miˈnuːtə/", "ex": "Eine Stunde hat 60 Minuten.", "exEn": "An hour has 60 minutes."},
                {"word": "die Stunde", "article": "die", "badge": "noun", "translation": "the hour", "ipa": "/ˈʃtʊndə/", "ex": "Ich lerne eine Stunde Deutsch.", "exEn": "I study German for one hour."},
                {"word": "der Morgen", "article": "der", "badge": "noun", "translation": "the morning", "ipa": "/ˈmɔʁɡən/", "ex": "Am Morgen trinke ich Kaffee.", "exEn": "In the morning I drink coffee."},
                {"word": "der Mittag", "article": "der", "badge": "noun", "translation": "midday / noon", "ipa": "/ˈmɪtaːk/", "ex": "Um Mittag esse ich zu Hause.", "exEn": "At noon I eat at home."},
                {"word": "der Abend", "article": "der", "badge": "noun", "translation": "the evening", "ipa": "/ˈaːbənt/", "ex": "Am Abend sehe ich fern.", "exEn": "In the evening I watch TV."},
                {"word": "die Nacht", "article": "die", "badge": "noun", "translation": "the night", "ipa": "/naxt/", "ex": "In der Nacht schlafe ich.", "exEn": "At night I sleep."},
                {"word": "um", "article": "", "badge": "prep", "translation": "at (specific time)", "ipa": "/ʊm/", "ex": "Der Der Zug kommt um 8 Uhr.", "exEn": "The train arrives at 8 o'clock."}
            ],
            "grammarTitle": "Official Clock Time & Time Prepositions",
            "grammarContent": """
### Official Time Formula: **Es ist [Hour] Uhr [Minutes]**

In official contexts (train stations, news, schedules), German uses the 24-hour clock:

• 08:00 → **Es ist acht Uhr.**  
• 08:15 → **Es ist acht Uhr fünfzehn.**  
• 14:30 → **Es ist vierzehn Uhr dreißig.**  
• 19:45 → **Es ist neunzehn Uhr fünfundvierzig.**

### Time Prepositions

| Time Unit | Preposition | Example |
|:---:|:---:|:---|
| **Clock Time** | **um** | *um* 8 Uhr, *um* 14:30 |
| **Parts of Day** | **am** | *am* Morgen, *am* Abend (Exception: *in der* Nacht!) |
""",
            "fillIns": [
                {"q": "Der Film beginnt ___ (at) 20 Uhr.", "a": "um"},
                {"q": "08:30 official: Es ist acht Uhr ___.", "a": "dreißig"},
                {"q": "___ (In the morning) trinke ich Tee.", "a": "Am Morgen"},
                {"q": "15:15 official: Es ist fünfzehn Uhr ___.", "a": "fünfzehn"},
                {"q": "In ___ (the night) ist es ruhig.", "a": "der Nacht"}
            ],
            "quiz": [
                {"question": "How do you say 'at 8 o'clock' in German?", "answer": "um 8 Uhr", "options": ["am 8 Uhr", "im 8 Uhr", "um 8 Uhr", "an 8 Uhr"]},
                {"question": "What is the official time for 14:30?", "answer": "Es ist vierzehn Uhr dreißig.", "options": ["Es ist zwei Uhr dreißig.", "Es ist vierzehn Uhr dreißig.", "Es ist vierzehn dreißig Uhr.", "Es ist halb drei Uhr."]},
                {"question": "Which preposition goes with parts of the day like Morgen, Abend?", "answer": "am", "options": ["um", "im", "am", "an"]},
                {"question": "What is the exception preposition for 'night'?", "answer": "in der Nacht", "options": ["am Nacht", "um Nacht", "in der Nacht", "im Nacht"]}
            ],
            "checkpoints": [
                "I can state official 24-hour clock times",
                "I know to use 'um' for exact times (um 8 Uhr)",
                "I know to use 'am' for morning/afternoon/evening",
                "I know the exception 'in der Nacht'"
            ],
            "tomorrow": "Informal clock time (halb, Viertel nach, Viertel vor)!"
        },
        {
            "dayNum": 30, "title": "Informal Clock Time (halb, Viertel)",
            "vocab": [
                {"word": "halb", "article": "", "badge": "phrase", "translation": "half (before next hour)", "ipa": "/halp/", "ex": "Es ist halb drei. (= 2:30)", "exEn": "It is half past two."},
                {"word": "Viertel nach", "article": "", "badge": "phrase", "translation": "quarter past", "ipa": "/ˈfɪʁtəl naːx/", "ex": "Es ist Viertel nach acht. (= 8:15)", "exEn": "It is quarter past eight."},
                {"word": "Viertel vor", "article": "", "badge": "phrase", "translation": "quarter to", "ipa": "/ˈfɪʁtəl foːɐ/", "ex": "Es ist Viertel vor neun. (= 8:45)", "exEn": "It is quarter to nine."},
                {"word": "nach", "article": "", "badge": "prep", "translation": "past (minutes after)", "ipa": "/naːx/", "ex": "Es ist zehn nach acht. (= 8:10)", "exEn": "It is ten past eight."},
                {"word": "vor", "article": "", "badge": "prep", "translation": "to / before (minutes to)", "ipa": "/foːɐ/", "ex": "Es ist fünf vor neun. (= 8:55)", "exEn": "It is five to nine."},
                {"word": "gegen", "article": "", "badge": "prep", "translation": "around / roughly", "ipa": "/ˈɡeːɡən/", "ex": "Ich komme gegen 8 Uhr.", "exEn": "I am coming around 8 o'clock."},
                {"word": "pünktlich", "article": "", "badge": "adj", "translation": "punctual / on time", "ipa": "/ˈpʏŋktlɪç/", "ex": "Der Bus ist pünktlich.", "exEn": "The bus is on time."},
                {"word": "zu spät", "article": "", "badge": "phrase", "translation": "late / too late", "ipa": "/tsuː ʃpɛːt/", "ex": "Ich bin zu spät!", "exEn": "I am too late!"}
            ],
            "grammarTitle": "The Informal German Clock System",
            "grammarContent": """
### ⚠️ CRITICAL WARNING: **halb** Means Half BEFORE the Hour!

In German, *halb* looks ahead to the **NEXT** hour!  
👉 **halb drei** = 2:30 (halfway to 3:00, NOT 3:30!)

| Time | Structure | German |
|:---:|:---:|:---|
| **8:05** | 5 past 8 | **fünf nach acht** |
| **8:15** | quarter past 8 | **Viertel nach acht** |
| **8:25** | 5 before half 9 | **fünf vor halb neun** |
| **8:30** | half before 9 | **halb neun** |
| **8:35** | 5 past half 9 | **fünf nach halb neun** |
| **8:45** | quarter to 9 | **Viertel vor neun** |
| **8:55** | 5 to 9 | **fünf vor neun** |
""",
            "fillIns": [
                {"q": "2:30 in informal German is: halb ___.", "a": "drei"},
                {"q": "8:15 is: Viertel ___ acht.", "a": "nach"},
                {"q": "8:45 is: Viertel ___ neun.", "a": "vor"},
                {"q": "7:30 is: halb ___.", "a": "acht"},
                {"q": "Ich komme ___ (around) 7 Uhr.", "a": "gegen"}
            ],
            "quiz": [
                {"question": "What time is 'halb vier' in English?", "answer": "3:30", "options": ["4:30", "3:30", "3:15", "4:15"]},
                {"question": "What is 8:15 in informal German?", "answer": "Viertel nach acht", "options": ["Viertel vor acht", "Viertel nach acht", "halb acht", "acht Uhr fünfzehn"]},
                {"question": "What is 8:45 in informal German?", "answer": "Viertel vor neun", "options": ["Viertel nach acht", "Viertel vor neun", "halb neun", "Viertel vor acht"]},
                {"question": "What does 'pünktlich' mean?", "answer": "on time / punctual", "options": ["too late", "slow", "on time / punctual", "early"]}
            ],
            "checkpoints": [
                "I know that 'halb vier' means 3:30 (not 4:30)",
                "I can say Viertel nach (quarter past) and Viertel vor (quarter to)",
                "I can use nach (past) and vor (to)",
                "I know terms like gegen, pünktlich, zu spät"
            ],
            "tomorrow": "Days of the week, months, and date prepositions!"
        },
        {
            "dayNum": 31, "title": "Days of the Week, Months & Seasons",
            "vocab": [
                {"word": "der Montag", "article": "der", "badge": "noun", "translation": "Monday", "ipa": "/ˈmoːntaːk/", "ex": "Am Montag arbeite ich.", "exEn": "On Monday I work."},
                {"word": "der Mittwoch", "article": "der", "badge": "noun", "translation": "Wednesday", "ipa": "/ˈmɪtvoːx/", "ex": "Am Mittwoch habe ich frei.", "exEn": "On Wednesday I have time off."},
                {"word": "das Wochenende", "article": "das", "badge": "noun", "translation": "the weekend", "ipa": "/ˈvɔxənˌɛndə/", "ex": "Am Wochenende schlafe ich lange.", "exEn": "At the weekend I sleep long."},
                {"word": "der Januar", "article": "der", "badge": "noun", "translation": "January", "ipa": "/ˈjanuaːɐ/", "ex": "Im Januar ist es kalt.", "exEn": "In January it is cold."},
                {"word": "der Juli", "article": "der", "badge": "noun", "translation": "July", "ipa": "/ˈjuːli/", "ex": "Im Juli mache ich Urlaub.", "exEn": "In July I go on holiday."},
                {"word": "das Jahr", "article": "das", "badge": "noun", "translation": "the year", "ipa": "/jaːɐ/", "ex": "Dieses Jahr lerne ich Deutsch.", "exEn": "This year I am learning German."},
                {"word": "heute", "article": "", "badge": "phrase", "translation": "today", "ipa": "/ˈhɔʏtə/", "ex": "Heute ist Montag.", "exEn": "Today is Monday."},
                {"word": "morgen", "article": "", "badge": "phrase", "translation": "tomorrow", "ipa": "/ˈmɔʁɡən/", "ex": "Morgen ist Dienstag.", "exEn": "Tomorrow is Tuesday."}
            ],
            "grammarTitle": "Prepositions for Days, Months & Seasons",
            "grammarContent": """
### 🎯 The Preposition Rule for Time

| Unit | Preposition | Examples |
|:---:|:---:|:---|
| **Days of Week** | **am** | **am** Montag, **am** Freitag |
| **Weekend** | **am** | **am** Wochenende |
| **Months** | **im** | **im** Januar, **im** Juli |
| **Seasons** | **im** | **im** Sommer, **im** Winter |
| **Exact Clock Time** | **um** | **um** 8 Uhr |

### All Days of the Week (All Masculine: **der**)
1. **Montag** (Mon) 2. **Dienstag** (Tue) 3. **Mittwoch** (Wed) 4. **Donnerstag** (Thu)  
5. **Freitag** (Fri) 6. **Samstag** (Sat) 7. **Sonntag** (Sun)
""",
            "fillIns": [
                {"q": "___ (On) Montag gehe ich zum Arzt.", "a": "Am"},
                {"q": "___ (In) Juli haben wir Urlaub.", "a": "Im"},
                {"q": "Was machst du ___ (at the) Wochenende?", "a": "am"},
                {"q": "___ (Today) ist ein schöner Tag.", "a": "Heute"},
                {"q": "Der Kurs beginnt ___ (at) 9 Uhr.", "a": "um"}
            ],
            "quiz": [
                {"question": "Which preposition is used with days of the week?", "answer": "am", "options": ["im", "am", "um", "an"]},
                {"question": "Which preposition is used with months (e.g. Januar)?", "answer": "im", "options": ["am", "im", "um", "in"]},
                {"question": "What is 'Mittwoch'?", "answer": "Wednesday", "options": ["Tuesday", "Wednesday", "Thursday", "Friday"]},
                {"question": "What article do ALL days of the week take?", "answer": "der", "options": ["der", "die", "das", "die (pl)"]}
            ],
            "checkpoints": [
                "I can list all 7 days of the week in German",
                "I know to use 'am' for days and weekend (am Montag)",
                "I know to use 'im' for months and seasons (im Januar)",
                "I can say what day today and tomorrow are"
            ],
            "tomorrow": "Daily routine verbs & separable verbs (trennbare Verben)!"
        },
        {
            "dayNum": 32, "title": "Daily Routine Verbs & Separable Verbs",
            "vocab": [
                {"word": "aufstehen", "article": "", "badge": "verb", "translation": "to get up / stand up", "ipa": "/ˈaʊfˌʃteːən/", "ex": "Ich stehe um 7 Uhr auf.", "exEn": "I get up at 7 o'clock."},
                {"word": "frühstücken", "article": "", "badge": "verb", "translation": "to eat breakfast", "ipa": "/ˈfʁyːʃˌtʏkən/", "ex": "Ich frühstücke um 7:30 Uhr.", "exEn": "I eat breakfast at 7:30."},
                {"word": "losfahren", "article": "", "badge": "verb", "translation": "to set off / drive off", "ipa": "/ˈloːsˌfaːʁən/", "ex": "Ich fahre um 8 Uhr los.", "exEn": "I set off at 8 o'clock."},
                {"word": "einkaufen", "article": "", "badge": "verb", "translation": "to go shopping", "ipa": "/ˈaɪnˌkaʊfən/", "ex": "Er kauft im Supermarkt ein.", "exEn": "He goes shopping at the supermarket."},
                {"word": "anrufen", "article": "", "badge": "verb", "translation": "to call on phone", "ipa": "/ˈanˌʁuːfən/", "ex": "Ich rufe dich am Abend an.", "exEn": "I will call you in the evening."},
                {"word": "fernsehen", "article": "", "badge": "verb", "translation": "to watch TV", "ipa": "/ˈfɛʁnˌzeːən/", "ex": "Wir sehen abends fern.", "exEn": "We watch TV in the evening."},
                {"word": "einschlafen", "article": "", "badge": "verb", "translation": "to fall asleep", "ipa": "/ˈaɪnˌʃlaːfən/", "ex": "Ich schlafe um 23 Uhr ein.", "exEn": "I fall asleep at 11 pm."},
                {"word": "aufräumen", "article": "", "badge": "verb", "translation": "to tidy up", "ipa": "/ˈaʊfˌʁɔʏmən/", "ex": "Sie räumt das Zimmer auf.", "exEn": "She tidies up the room."}
            ],
            "grammarTitle": "Separable Verbs (Trennbare Verben)",
            "grammarContent": """
### Prefix Splits and Goes to the VERY END of the Sentence!

In German, separable verbs have a prefix (like *auf-*, *an-*, *ein-*, *fern-*) that detaches in present tense sentences!

👉 **Formula:**  
**Subject + Conjugated Verb (Pos 2) + ... + Prefix (At End!)**

| Infinitive | Conjugated Sentence |
|:---|:---|
| **aufstehen** | Ich **stehe** um 7 Uhr **auf**. |
| **einkaufen** | Er **kauft** im Supermarkt **ein**. |
| **anrufen** | Ich **rufe** meine Mutter **an**. |
| **fernsehen** | Wir **sehen** abends **fern**. |
| **einschlafen** | Das Baby **schläft** um 20 Uhr **ein**. |

> 💡 **Common Separable Prefixes:** *auf-, an-, ab-, ein-, aus-, mit-, fern-, los-*
""",
            "fillIns": [
                {"q": "Ich stehe um 7 Uhr ___ (aufstehen).", "a": "auf"},
                {"q": "Er kauft im Supermarkt ___ (einkaufen).", "a": "ein"},
                {"q": "Wir sehen abends ___ (fernsehen).", "a": "fern"},
                {"q": "Ich rufe dich morgen ___ (anrufen).", "a": "an"},
                {"q": "Das Kind schläft schnell ___ (einschlafen).", "a": "ein"}
            ],
            "quiz": [
                {"question": "Where does the prefix of a separable verb go in a present tense sentence?", "answer": "to the very end of the sentence", "options": ["right after the verb", "to the very end of the sentence", "to the beginning", "it doesn't split"]},
                {"question": "How do you conjugate 'Ich + aufstehen'?", "answer": "Ich stehe ... auf.", "options": ["Ich aufstehe.", "Ich stehe ... auf.", "Ich stehe auf ...", "Ich bin aufstehen."]},
                {"question": "What is 'fernsehen'?", "answer": "to watch TV", "options": ["to look far", "to call", "to watch TV", "to sleep"]},
                {"question": "Translate: 'He tidies up his room.'", "answer": "Er räumt sein Zimmer auf.", "options": ["Er aufräumt sein Zimmer.", "Er räumt sein Zimmer auf.", "Er räumt auf sein Zimmer.", "Er ist sein Zimmer aufräumen."]}
            ],
            "checkpoints": [
                "I understand how separable verbs split in the present tense",
                "I know that the prefix goes to the very end of the sentence",
                "I know 8 common daily routine separable verbs",
                "I can describe when I get up, shop, watch TV, and sleep"
            ],
            "tomorrow": "Sentence word order with time expressions & V2 rule!"
        },
        {
            "dayNum": 33, "title": "Sentence Word Order & the V2 Rule",
            "vocab": [
                {"word": "zuerst", "article": "", "badge": "phrase", "translation": "first / firstly", "ipa": "/tsuˈeːɐst/", "ex": "Zuerst stehe ich auf.", "exEn": "First I get up."},
                {"word": "dann", "article": "", "badge": "phrase", "translation": "then", "ipa": "/dan/", "ex": "Dann frühstücke ich.", "exEn": "Then I eat breakfast."},
                {"word": "danach", "article": "", "badge": "phrase", "translation": "afterwards / after that", "ipa": "/daˈnaːx/", "ex": "Danach fahre ich zur Arbeit.", "exEn": "After that I drive to work."},
                {"word": "später", "article": "", "badge": "phrase", "translation": "later", "ipa": "/ˈʃpɛːtɐ/", "ex": "Später esse ich zu Mittag.", "exEn": "Later I eat lunch."},
                {"word": "immer", "article": "", "badge": "phrase", "translation": "always", "ipa": "/ˈɪmɐ/", "ex": "Ich frühstücke immer um 7 Uhr.", "exEn": "I always eat breakfast at 7."},
                {"word": "oft", "article": "", "badge": "phrase", "translation": "often", "ipa": "/ɔft/", "ex": "Ich gehe oft spazieren.", "exEn": "I often go for a walk."},
                {"word": "selten", "article": "", "badge": "phrase", "translation": "rarely / seldom", "ipa": "/ˈzɛltən/", "ex": "Ich trinke selten Alkohol.", "exEn": "I rarely drink alcohol."},
                {"word": "normalerweise", "article": "", "badge": "phrase", "translation": "normally / usually", "ipa": "/nɔʁˈmaːlɐˌvaɪzə/", "ex": "Normalerweise stehe ich früh auf.", "exEn": "Normally I get up early."}
            ],
            "grammarTitle": "The V2 Rule: Verb ALWAYS Stays in Position 2!",
            "grammarContent": """
### The Golden Rule of German Syntax: **V2 (Verb Position 2)**

In German main clauses, the conjugated verb **MUST be the 2nd element**!  
If you start the sentence with a **time word** (zuerst, dann, am Montag, um 8 Uhr), the **subject flips to Position 3**!

| Position 1 (Element) | Position 2 (VERB) | Position 3 (Subject) | Rest of Sentence |
|:---:|:---:|:---:|:---|
| **Ich** | **stehe** | — | um 7 Uhr auf. |
| **Um 7 Uhr** | **stehe** | **ich** | auf. |
| **Dann** | **frühstücke** | **ich** | in der Küche. |
| **Am Montag** | **fahre** | **ich** | nach Berlin. |
| **Zuerst** | **mache** | **ich** | Hausaufgaben. |

> 🎯 **Notice:** Starting with *dann* or *danach* forces the subject behind the verb: **Dann esse ich...** (NOT: *Dann ich esse...*)!
""",
            "fillIns": [
                {"q": "Dann ___ (frühstücken) ich.", "a": "frühstücke"},
                {"q": "Um 8 Uhr ___ (fahren) er los.", "a": "fährt"},
                {"q": "Zuerst ___ (duschen) ich.", "a": "dusche"},
                {"q": "Am Samstag ___ (schlafen) wir lange.", "a": "schlafen"},
                {"q": "Normalerweise ___ (arbeiten) sie viel.", "a": "arbeitet"}
            ],
            "quiz": [
                {"question": "What position MUST the conjugated verb take in a German main clause?", "answer": "Position 2", "options": ["Position 1", "Position 2", "Position 3", "at the very end"]},
                {"question": "Which sentence has correct German word order?", "answer": "Dann trinke ich Kaffee.", "options": ["Dann ich trinke Kaffee.", "Dann trinke ich Kaffee.", "Trinke ich dann Kaffee.", "Kaffee trinke ich dann."]},
                {"question": "What happens to the subject when sentence starts with 'Um 8 Uhr'?", "answer": "moves to Position 3 right after verb", "options": ["stays at Position 1", "moves to Position 3 right after verb", "goes to the end", "disappears"]},
                {"question": "What is 'zuerst'?", "answer": "first / firstly", "options": ["then", "afterwards", "first / firstly", "later"]}
            ],
            "checkpoints": [
                "I understand the V2 rule (verb in position 2)",
                "I know to flip subject to position 3 when starting with time words",
                "I know transition connectors: zuerst, dann, danach, später",
                "I can write a sequence of daily activities with correct word order"
            ],
            "tomorrow": "Full daily routine paragraph & nach Hause vs zu Hause!"
        },
        {
            "dayNum": 34, "title": "Daily Routine Paragraph & nach/zu Hause",
            "vocab": [
                {"word": "duschen", "article": "", "badge": "verb", "translation": "to shower", "ipa": "/ˈdʊʃən/", "ex": "Ich dusche jeden Morgen.", "exEn": "I shower every morning."},
                {"word": "sich anziehen", "article": "", "badge": "verb", "translation": "to get dressed", "ipa": "/zɪç ˈanˌtsiːən/", "ex": "Ich ziehe mich um 7:30 an.", "exEn": "I get dressed at 7:30."},
                {"word": "der Weg", "article": "der", "badge": "noun", "translation": "the way / route", "ipa": "/veːk/", "ex": "Der Weg dauert 20 Minuten.", "exEn": "The route takes 20 minutes."},
                {"word": "dauern", "article": "", "badge": "verb", "translation": "to take / last (time)", "ipa": "/ˈdaʊɐn/", "ex": "Das dauert eine Stunde.", "exEn": "That takes an hour."},
                {"word": "die Pause", "article": "die", "badge": "noun", "translation": "the break / pause", "ipa": "/ˈpaʊzə/", "ex": "Ich mache um 12 Uhr Pause.", "exEn": "I take a break at 12."},
                {"word": "nach Hause", "article": "", "badge": "phrase", "translation": "home (movement towards)", "ipa": "/naːx ˈhaʊzə/", "ex": "Ich gehe nach Hause.", "exEn": "I am going home."},
                {"word": "zu Hause", "article": "", "badge": "phrase", "translation": "at home (location state)", "ipa": "/tsuː ˈhaʊzə/", "ex": "Ich bin zu Hause.", "exEn": "I am at home."},
                {"word": "die Freizeit", "article": "die", "badge": "noun", "translation": "the free time", "ipa": "/ˈfʁaɪˌtsaɪt/", "ex": "In der Freizeit lese ich.", "exEn": "In my free time I read."}
            ],
            "grammarTitle": "Crucial Distinction: nach Hause vs. zu Hause",
            "grammarContent": """
### Direction vs. Location: **nach Hause** vs. **zu Hause**

1. **nach Hause** = direction (going / driving / coming home)  
   • *Ich gehe nach Hause.* (I am walking home.)  
   • *Er fährt um 17 Uhr nach Hause.* (He drives home at 5 pm.)

2. **zu Hause** = static location (being / staying / eating at home)  
   • *Ich bin zu Hause.* (I am at home.)  
   • *Wir essen zu Hause.* (We eat at home.)

### Sample Daily Routine Text

> *"Ich stehe um 6:30 Uhr auf. Zuerst dusche ich und ziehe mich an. Um 7:00 Uhr frühstücke ich. Danach fahre ich zur Arbeit. Der Weg dauert 30 Minuten. Ich arbeite von 8:00 bis 16:30 Uhr. Um 17:00 Uhr komme ich nach Hause. Am Abend sehe ich fern oder lese ein Buch. Um 23:00 Uhr schlafe ich ein."*
""",
            "fillIns": [
                {"q": "Ich gehe jetzt ___ (home / direction).", "a": "nach Hause"},
                {"q": "Am Sonntag bin ich ___ (at home / location).", "a": "zu Hause"},
                {"q": "Der Weg zur Arbeit ___ (takes) 20 Minuten.", "a": "dauert"},
                {"q": "Um 12 Uhr mache ich ___ (break).", "a": "Pause"},
                {"q": "Ich ziehe mich um 7 Uhr ___ (anziehen).", "a": "an"}
            ],
            "quiz": [
                {"question": "Which expression means 'going home' (movement)?", "answer": "nach Hause", "options": ["zu Hause", "nach Hause", "im Hause", "bei Hause"]},
                {"question": "Which expression means 'being at home' (location)?", "answer": "zu Hause", "options": ["zu Hause", "nach Hause", "in Hause", "an Hause"]},
                {"question": "Translate: 'How long does the journey take?'", "answer": "Wie lange dauert der Weg?", "options": ["Wie viel dauert der Weg?", "Wie lange dauert der Weg?", "Was dauert der Weg?", "Wie weit ist der Weg?"]},
                {"question": "What is 'die Freizeit'?", "answer": "free time", "options": ["work time", "free time", "break time", "night time"]}
            ],
            "checkpoints": [
                "I know the difference between nach Hause (direction) and zu Hause (location)",
                "I can use routine verbs like duschen, sich anziehen, Pause machen",
                "I can write a 6-sentence paragraph of my daily routine",
                "I can state how long activities take (dauern)"
            ],
            "tomorrow": "Week 5 Review and Speaking Practice!"
        },
        {
            "dayNum": 35, "isReview": True, "title": "Week 5 Review & Speaking Practice",
            "reviewCards": [
                {"german": "um 8 Uhr", "english": "at 8 o'clock", "example": "Der Kurs beginnt um 8 Uhr."},
                {"german": "halb drei (2:30)", "english": "half past two", "example": "Es ist halb drei."},
                {"german": "Viertel nach / vor", "english": "quarter past / to", "example": "Viertel nach acht = 8:15."},
                {"german": "am Montag", "english": "on Monday", "example": "Am Montag arbeite ich."},
                {"german": "im Januar", "english": "in January", "example": "Im Januar schneit es."},
                {"german": "aufstehen (steht ... auf)", "english": "to get up", "example": "Ich stehe um 7 Uhr auf."},
                {"german": "einkaufen (kauft ... ein)", "english": "to shop", "example": "Er kauft im Supermarkt ein."},
                {"german": "anrufen (ruft ... an)", "english": "to call", "example": "Ich rufe meine Mutter an."},
                {"german": "fernsehen (sieht ... fern)", "english": "to watch TV", "example": "Wir sehen abends fern."},
                {"german": "zuerst / dann / danach", "english": "first / then / after that", "example": "Zuerst dusche ich, dann esse ich."},
                {"german": "nach Hause", "english": "home (direction)", "example": "Ich gehe nach Hause."},
                {"german": "zu Hause", "english": "at home (location)", "example": "Ich bin zu Hause."},
                {"german": "pünktlich", "english": "on time", "example": "Der Zug ist pünktlich."},
                {"german": "immer / oft / selten", "english": "always / often / rarely", "example": "Ich stehe immer früh auf."},
                {"german": "V2 rule", "english": "verb in position 2", "example": "Am Montag fahre ich..."}
            ],
            "grammarSummary": """
### Week 5 Master Summary

1. **Clock Time:**  
   - Official: *Es ist 14 Uhr 30.*  
   - Informal: *halb drei* (= 2:30!), *Viertel nach acht* (= 8:15), *Viertel vor neun* (= 8:45).
2. **Time Prepositions:**  
   - **um** + clock time (*um 8 Uhr*)  
   - **am** + day/weekend (*am Montag, am Wochenende*)  
   - **im** + month/season (*im Januar, im Sommer*)
3. **Separable Verbs:** Prefix splits and goes to the VERY END (*Ich stehe um 7 Uhr auf*).
4. **V2 Word Order:** Verb ALWAYS stays in Position 2! Starting with time flips subject to Pos 3 (*Dann esse ich...*).
5. **Home Expressions:** *nach Hause* (going home) vs. *zu Hause* (being at home).
""",
            "quiz": [
                {"question": "What time is 'halb fünf'?", "answer": "4:30", "options": ["5:30", "4:30", "4:15", "5:15"]},
                {"question": "Which preposition is used for days of the week?", "answer": "am", "options": ["um", "im", "am", "an"]},
                {"question": "Conjugate: Ich + aufstehen", "answer": "Ich stehe ... auf.", "options": ["Ich aufstehe.", "Ich stehe ... auf.", "Ich stehe auf ...", "Ich bin aufstehen."]},
                {"question": "Where does verb go when sentence starts with 'Am Dienstag'?", "answer": "Position 2 (right after 'Am Dienstag')", "options": ["Position 1", "Position 2 (right after 'Am Dienstag')", "Position 3", "At the end"]},
                {"question": "Which phrase means 'I am staying at home'?", "answer": "Ich bleibe zu Hause.", "options": ["Ich bleibe nach Hause.", "Ich bleibe zu Hause.", "Ich bleibe im Hause.", "Ich bleibe an Hause."]},
                {"question": "What is 8:45 in informal German?", "answer": "Viertel vor neun", "options": ["Viertel nach acht", "Viertel vor neun", "halb neun", "Viertel vor acht"]},
                {"question": "Translate: 'Then I drink coffee.'", "answer": "Dann trinke ich Kaffee.", "options": ["Dann ich trinke Kaffee.", "Dann trinke ich Kaffee.", "Trinke dann ich Kaffee.", "Ich trinke dann Kaffee."]},
                {"question": "What preposition is used for exact clock time?", "answer": "um", "options": ["am", "im", "um", "an"]}
            ],
            "speakingPrompt": """
### 🗣️ Speaking Exercise — Describe Your Entire Daily Routine

Read this script aloud and record yourself or practice with a partner:

> *"Ich beschreibe meinen Tag: Ich stehe normalerweise um [Time] Uhr auf. Zuerst gehe ich ins Bad und dusche. Um [Time] Uhr frühstücke ich. Um [Time] Uhr fahre ich zur Arbeit. Ich arbeite von [Time] bis [Time] Uhr. Um 13 Uhr esse ich zu Mittag. Um [Time] Uhr komme ich nach Hause. Am Abend sehe ich fern oder lese ein Buch. Ich schlafe gegen [Time] Uhr ein."*
""",
            "checkpoints": [
                "I can tell official and informal time fluently",
                "I can use separable verbs in present tense sentences",
                "I can apply V2 word order after time expressions",
                "I can give a 90-second spoken presentation of my daily schedule"
            ]
        }
    ]
}

print("Week 5 data populated.")
