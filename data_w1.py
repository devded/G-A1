# Week 1 Data
weeks_data = []

weeks_data.append({
    "weekNum": 1,
    "title": "Alphabet, Greetings & First Words",
    "level": "A1.1",
    "goal": "Master German pronunciation, introduce yourself, count from 1 to 20, use basic greetings, and understand articles der/die/das.",
    "days": [
        {
            "dayNum": 1, "title": "Alphabet, Sounds & First Greetings",
            "vocab": [
                {"word": "Hallo", "article": "", "badge": "phrase", "translation": "Hello / Hi", "ipa": "/ˈhaloː/", "ex": "Hallo! Wie heißt du?", "exEn": "Hello! What's your name?"},
                {"word": "Guten Morgen", "article": "", "badge": "phrase", "translation": "Good morning", "ipa": "/ˈɡuːtən ˈmɔʁɡən/", "ex": "Guten Morgen, Herr Schmidt!", "exEn": "Good morning, Mr Schmidt!"},
                {"word": "Guten Tag", "article": "", "badge": "phrase", "translation": "Good day / Hello (formal)", "ipa": "/ˈɡuːtən taːk/", "ex": "Guten Tag! Ich bin Anna.", "exEn": "Good day! I am Anna."},
                {"word": "Guten Abend", "article": "", "badge": "phrase", "translation": "Good evening", "ipa": "/ˈɡuːtən ˈaːbənt/", "ex": "Guten Abend, wie geht es Ihnen?", "exEn": "Good evening, how are you? (formal)"},
                {"word": "Tschüss", "article": "", "badge": "phrase", "translation": "Bye / See you (informal)", "ipa": "/tʃʏs/", "ex": "Tschüss, bis morgen!", "exEn": "Bye, see you tomorrow!"},
                {"word": "Auf Wiedersehen", "article": "", "badge": "phrase", "translation": "Goodbye (formal)", "ipa": "/aʊf ˈviːdɐzeːən/", "ex": "Auf Wiedersehen, Frau Müller!", "exEn": "Goodbye, Mrs Müller!"},
                {"word": "Bitte", "article": "", "badge": "phrase", "translation": "Please / You're welcome", "ipa": "/ˈbɪtə/", "ex": "Ein Kaffee, bitte.", "exEn": "A coffee, please."},
                {"word": "Danke", "article": "", "badge": "phrase", "translation": "Thank you", "ipa": "/ˈdaŋkə/", "ex": "Danke schön!", "exEn": "Thank you very much!"}
            ],
            "grammarTitle": "The German Alphabet & Special Sounds",
            "grammarContent": """
### Key Sounds & Special Characters
German uses the same 26 letters as English, plus 4 special characters: **ä, ö, ü, ß**

• **ä** (like "e" in "bed"): Bäcker
• **ö** (like "u" in "burn"): schön
• **ü** (like "u" + pucker lips): über
• **ß** (like double "ss"): Straße
• **ei** (like "eye"): nein
• **ie** (like "ee"): hier
• **eu / äu** (like "oy"): neu

### Formal vs Informal Greetings
• **Friends / family**: Hallo! Tschüss!
• **Adults / strangers**: Guten Tag! Auf Wiedersehen!
• **On the phone**: Guten Tag! Auf Wiederhören!
""",
            "fillIns": [
                {"q": "___! Wie heißt du?", "a": "Hallo"},
                {"q": "Guten ___! Ich bin Anna.", "a": "Tag"},
                {"q": "Guten ___! Wie geht es Ihnen?", "a": "Abend"},
                {"q": "Ein Kaffee, ___.", "a": "bitte"},
                {"q": "___, bis morgen!", "a": "Tschüss"}
            ],
            "quiz": [
                {"question": "How do you say Good Morning in German?", "answer": "Guten Morgen", "options": ["Guten Morgen", "Guten Tag", "Guten Abend", "Tschüss"]},
                {"question": "Which special character sounds like a double 'ss'?", "answer": "ß", "options": ["ä", "ö", "ü", "ß"]},
                {"question": "How do you say goodbye formally on the phone?", "answer": "Auf Wiederhören", "options": ["Tschüss", "Auf Wiedersehen", "Auf Wiederhören", "Guten Tag"]},
                {"question": "What does 'Danke' mean?", "answer": "Thank you", "options": ["Please", "Thank you", "Goodbye", "Hello"]}
            ],
            "checkpoints": [
                "I know the 4 special German characters (ä, ö, ü, ß)",
                "I can greet someone formally and informally",
                "I know when to use Tschüss vs Auf Wiedersehen",
                "I can say please and thank you in German"
            ],
            "tomorrow": "Personal pronouns and introducing yourself!"
        },
        {
            "dayNum": 2, "title": "Personal Pronouns & Introducing Yourself",
            "vocab": [
                {"word": "ich", "article": "", "badge": "pronoun", "translation": "I", "ipa": "/ɪç/", "ex": "Ich bin Student.", "exEn": "I am a student."},
                {"word": "du", "article": "", "badge": "pronoun", "translation": "you (informal)", "ipa": "/duː/", "ex": "Wie heißt du?", "exEn": "What is your name?"},
                {"word": "er / sie / es", "article": "", "badge": "pronoun", "translation": "he / she / it", "ipa": "/eːɐ/ /ziː/ /ɛs/", "ex": "Er ist müde.", "exEn": "He is tired."},
                {"word": "wir", "article": "", "badge": "pronoun", "translation": "we", "ipa": "/viːɐ/", "ex": "Wir sind Freunde.", "exEn": "We are friends."},
                {"word": "Sie", "article": "", "badge": "pronoun", "translation": "you (formal)", "ipa": "/ziː/", "ex": "Wie heißen Sie?", "exEn": "What is your name? (formal)"},
                {"word": "heißen", "article": "", "badge": "verb", "translation": "to be called / named", "ipa": "/ˈhaɪsən/", "ex": "Ich heiße Klaus.", "exEn": "My name is Klaus."},
                {"word": "sein", "article": "", "badge": "verb", "translation": "to be", "ipa": "/zaɪn/", "ex": "Ich bin aus Deutschland.", "exEn": "I am from Germany."},
                {"word": "kommen", "article": "", "badge": "verb", "translation": "to come (from)", "ipa": "/ˈkɔmən/", "ex": "Ich komme aus der Türkei.", "exEn": "I come from Turkey."}
            ],
            "grammarTitle": "The Verb sein (to be) & Introductions",
            "grammarContent": """
### Conjugation: **sein** (to be)

| Pronoun | Form | Pronunciation |
|:---:|:---:|:---:|
| ich | **bin** | /bɪn/ |
| du | **bist** | /bɪst/ |
| er/sie/es | **ist** | /ɪst/ |
| wir | **sind** | /zɪnt/ |
| ihr | **seid** | /zaɪt/ |
| Sie/sie | **sind** | /zɪnt/ |

> <Icon name="target" /> **Self-Introduction Formulas:**  
> • Ich bin [Name].  
> • Ich heiße [Name].  
> • Ich komme aus [Country].
""",
            "fillIns": [
                {"q": "Ich ___ Maria.", "a": "bin"},
                {"q": "Du ___ sehr nett.", "a": "bist"},
                {"q": "Er ___ mein Freund.", "a": "ist"},
                {"q": "Wir ___ aus Deutschland.", "a": "sind"},
                {"q": "Wie heißen ___? (formal)", "a": "Sie"}
            ],
            "quiz": [
                {"question": "Complete: Ich ___ Maria.", "answer": "bin", "options": ["bin", "bist", "ist", "sind"]},
                {"question": "How do you say 'My name is Anna'?", "answer": "Ich heiße Anna.", "options": ["Ich bin Anna.", "Ich heiße Anna.", "Du heißt Anna.", "Sie heißt Anna."]},
                {"question": "Conjugate: Du ___ sehr nett.", "answer": "bist", "options": ["bin", "bist", "ist", "sind"]},
                {"question": "What is the formal 'you' in German?", "answer": "Sie", "options": ["du", "ihr", "Sie", "wir"]}
            ],
            "checkpoints": [
                "I can conjugate the irregular verb sein",
                "I know how to introduce myself in German",
                "I know the difference between du and Sie",
                "I can say which country I come from"
            ],
            "tomorrow": "Numbers 1 to 20 and stating your age!"
        },
        {
            "dayNum": 3, "title": "Numbers 1-20 & Stating Your Age",
            "vocab": [
                {"word": "eins", "article": "", "badge": "number", "translation": "one (1)", "ipa": "/aɪns/", "ex": "Ich habe eins.", "exEn": "I have one."},
                {"word": "zwei", "article": "", "badge": "number", "translation": "two (2)", "ipa": "/tsvaɪ/", "ex": "Zwei Kaffee, bitte.", "exEn": "Two coffees, please."},
                {"word": "drei", "article": "", "badge": "number", "translation": "three (3)", "ipa": "/dʁaɪ/", "ex": "Er hat drei Kinder.", "exEn": "He has three children."},
                {"word": "zehn", "article": "", "badge": "number", "translation": "ten (10)", "ipa": "/tseːn/", "ex": "Es ist zehn Uhr.", "exEn": "It is ten o'clock."},
                {"word": "zwölf", "article": "", "badge": "number", "translation": "twelve (12)", "ipa": "/tsvœlf/", "ex": "Zwölf Monate.", "exEn": "Twelve months."},
                {"word": "zwanzig", "article": "", "badge": "number", "translation": "twenty (20)", "ipa": "/ˈtsvantsɪç/", "ex": "Ich bin zwanzig Jahre alt.", "exEn": "I am twenty years old."},
                {"word": "das Jahr", "article": "das", "badge": "noun", "translation": "the year", "ipa": "/jaːʁ/", "ex": "Ein gutes Jahr.", "exEn": "A good year."},
                {"word": "alt", "article": "", "badge": "adjective", "translation": "old", "ipa": "/alt/", "ex": "Wie alt bist du?", "exEn": "How old are you?"}
            ],
            "grammarTitle": "Numbers 1-20 & Stating Age",
            "grammarContent": """
### German Numbers 1 to 20
• **1-4**: eins, zwei, drei, vier
• **5-8**: fünf, sechs, sieben, acht
• **9-12**: neun, zehn, elf, zwölf
• **13-19**: dreizehn, vierzehn, fünfzehn, sechzehn, siebzehn, achtzehn, neunzehn
• **20**: zwanzig

> <Icon name="target" /> **Stating Age Formula:**  
> Use **sein** + [Number] + **Jahre alt**:  
> • Ich bin 25 Jahre alt.  
> • Wie alt bist du? / Wie alt sind Sie?
""",
            "fillIns": [
                {"q": "Ich bin ___ (20) Jahre alt.", "a": "zwanzig"},
                {"q": "Wie alt ___ (bist/sind) du?", "a": "bist"},
                {"q": "Zwei + drei = ___ (5).", "a": "fünf"},
                {"q": "Zehn + zehn = ___ (20).", "a": "zwanzig"},
                {"q": "Er ist 18 ___ (years) alt.", "a": "Jahre"}
            ],
            "quiz": [
                {"question": "How do you say 'How old are you?' in German?", "answer": "Wie alt bist du?", "options": ["Wie bist du?", "Wie alt bist du?", "Wie alt hast du?", "Wie heißt du?"]},
                {"question": "What is the German word for 12?", "answer": "zwölf", "options": ["zehn", "elf", "zwölf", "zwanzig"]},
                {"question": "What is 7 + 8 in German?", "answer": "fünfzehn", "options": ["vierzehn", "fünfzehn", "sechzehn", "siebzehn"]},
                {"question": "Complete: Er ist 30 Jahre ___.", "answer": "alt", "options": ["jung", "alt", "Jahre", "sein"]}
            ],
            "checkpoints": [
                "I can count from 1 to 20 in German",
                "I can ask someone their age in German",
                "I can state my age in German using sein",
                "I know the spelling of numbers 1-20"
            ],
            "tomorrow": "Days of the week, colors, and basic sentences!"
        },
        {
            "dayNum": 4, "title": "Days of the Week & Basic Colors",
            "vocab": [
                {"word": "der Montag", "article": "der", "badge": "noun", "translation": "Monday", "ipa": "/ˈmoːntaːk/", "ex": "Heute ist Montag.", "exEn": "Today is Monday."},
                {"word": "der Dienstag", "article": "der", "badge": "noun", "translation": "Tuesday", "ipa": "/ˈdiːnstaːk/", "ex": "Am Dienstag lerne ich Deutsch.", "exEn": "On Tuesday I learn German."},
                {"word": "der Mittwoch", "article": "der", "badge": "noun", "translation": "Wednesday", "ipa": "/ˈmɪtvɔx/", "ex": "Mittwoch ist die Mitte der Woche.", "exEn": "Wednesday is the middle of the week."},
                {"word": "der Donnerstag", "article": "der", "badge": "noun", "translation": "Thursday", "ipa": "/ˈdɔnɐstaːk/", "ex": "Donnerstag habe ich frei.", "exEn": "On Thursday I have the day off."},
                {"word": "der Freitag", "article": "der", "badge": "noun", "translation": "Friday", "ipa": "/ˈfʁaɪtaːk/", "ex": "Freitag ist mein Lieblingstag.", "exEn": "Friday is my favorite day."},
                {"word": "rot", "article": "", "badge": "adjective", "translation": "red", "ipa": "/ʁoːt/", "ex": "Das Auto ist rot.", "exEn": "The car is red."},
                {"word": "blau", "article": "", "badge": "adjective", "translation": "blue", "ipa": "/blaʊ/", "ex": "Der Himmel ist blau.", "exEn": "The sky is blue."},
                {"word": "grün", "article": "", "badge": "adjective", "translation": "green", "ipa": "/ɡʁyːn/", "ex": "Das Gras ist grün.", "exEn": "The grass is green."}
            ],
            "grammarTitle": "Days of the Week & Preposition am",
            "grammarContent": """
### The 7 Days of the Week (All Masculine: der)
• **der Montag, der Dienstag, der Mittwoch**
• **der Donnerstag, der Freitag**
• **der Samstag, der Sonntag**

> <Icon name="target" /> **Preposition Rule for Days:**  
> Always use **am** (on) before days of the week:  
> • **am** Montag (on Monday)  
> • **am** Wochenende (on the weekend)
""",
            "fillIns": [
                {"q": "___ (On) Montag habe ich Deutschunterricht.", "a": "Am"},
                {"q": "Heute ist ___ (Monday).", "a": "Montag"},
                {"q": "Der Himmel ist ___ (blue).", "a": "blau"},
                {"q": "Das Auto ist ___ (red).", "a": "rot"},
                {"q": "Freitag ist mein ___ (favorite day).", "a": "Lieblingstag"}
            ],
            "quiz": [
                {"question": "What preposition is used before days of the week?", "answer": "am", "options": ["im", "am", "um", "an"]},
                {"question": "All days of the week have which gender in German?", "answer": "masculine (der)", "options": ["masculine (der)", "feminine (die)", "neuter (das)", "plural"]},
                {"question": "What is the German word for Wednesday?", "answer": "Mittwoch", "options": ["Montag", "Dienstag", "Mittwoch", "Donnerstag"]},
                {"question": "Translate: 'The sky is blue.'", "answer": "Der Himmel ist blau.", "options": ["Der Himmel ist rot.", "Der Himmel ist blau.", "Der Himmel ist grün.", "Der Himmel ist gelb."]}
            ],
            "checkpoints": [
                "I know all 7 days of the week in German",
                "I know to use am before days",
                "I can name basic colors in German",
                "I know all days of the week are der"
            ],
            "tomorrow": "Definite and indefinite articles (der, die, das)!"
        },
        {
            "dayNum": 5, "title": "Nouns & Gender: der, die, das",
            "vocab": [
                {"word": "der Mann", "article": "der", "badge": "noun", "translation": "the man", "ipa": "/man/", "ex": "Der Mann ist freundlich.", "exEn": "The man is friendly."},
                {"word": "die Frau", "article": "die", "badge": "noun", "translation": "the woman", "ipa": "/fʁaʊ/", "ex": "Die Frau arbeitet hier.", "exEn": "The woman works here."},
                {"word": "das Kind", "article": "das", "badge": "noun", "translation": "the child", "ipa": "/kɪnt/", "ex": "Das Kind spielt.", "exEn": "The child is playing."},
                {"word": "der Tisch", "article": "der", "badge": "noun", "translation": "the table", "ipa": "/tɪʃ/", "ex": "Der Tisch ist neu.", "exEn": "The table is new."},
                {"word": "die Tasche", "article": "die", "badge": "noun", "translation": "the bag", "ipa": "/ˈtaʃə/", "ex": "Die Tasche ist groß.", "exEn": "The bag is big."},
                {"word": "das Buch", "article": "das", "badge": "noun", "translation": "the book", "ipa": "/buːx/", "ex": "Das Buch ist gut.", "exEn": "The book is good."},
                {"word": "ein", "article": "", "badge": "article", "translation": "a / an (masculine & neuter)", "ipa": "/aɪn/", "ex": "Das ist ein Tisch.", "exEn": "That is a table."},
                {"word": "eine", "article": "", "badge": "article", "translation": "a / an (feminine)", "ipa": "/ˈaɪnə/", "ex": "Das ist eine Tasche.", "exEn": "That is a bag."}
            ],
            "grammarTitle": "German Noun Genders & Indefinite Articles",
            "grammarContent": """
### The 3 Genders in German
• **der** (Masculine): der Mann, der Tisch
• **die** (Feminine): die Frau, die Tasche
• **das** (Neuter): das Kind, das Buch

### Indefinite Articles (a / an)
• **Masculine (der)** → **ein** (ein Mann, ein Tisch)
• **Feminine (die)** → **eine** (eine Frau, eine Tasche)
• **Neuter (das)** → **ein** (ein Kind, ein Buch)

> <Icon name="target" /> **Rule:** ALWAYS learn nouns together with their article (der/die/das)!
""",
            "fillIns": [
                {"q": "Das ist ___ (a) Mann.", "a": "ein"},
                {"q": "Das ist ___ (a) Frau.", "a": "eine"},
                {"q": "Das ist ___ (a) Buch.", "a": "ein"},
                {"q": "___ (The) Tisch ist neu.", "a": "Der"},
                {"q": "___ (The) Tasche ist schön.", "a": "Die"}
            ],
            "quiz": [
                {"question": "What is the indefinite article for feminine nouns?", "answer": "eine", "options": ["ein", "eine", "einen", "eines"]},
                {"question": "Which article goes with 'Kind'?", "answer": "das", "options": ["der", "die", "das", "den"]},
                {"question": "What is 'a table' in German?", "answer": "ein Tisch", "options": ["ein Tisch", "eine Tisch", "das Tisch", "der Tisch"]},
                {"question": "Which article is used for 'Tasche'?", "answer": "die", "options": ["der", "die", "das", "den"]}
            ],
            "checkpoints": [
                "I know the 3 German genders (der, die, das)",
                "I can use indefinite articles ein and eine correctly",
                "I know to memorize every noun with its gender",
                "I can form simple sentences with nouns"
            ],
            "tomorrow": "Core Verbs: sein & haben deep dive!"
        },
        {
            "dayNum": 6, "title": "Core Verbs: sein & haben Deep Dive",
            "vocab": [
                {"word": "haben", "article": "", "badge": "verb", "translation": "to have", "ipa": "/ˈhaːbən/", "ex": "Ich habe eine Frage.", "exEn": "I have a question."},
                {"word": "die Frage", "article": "die", "badge": "noun", "translation": "the question", "ipa": "/ˈfʁaːɡə/", "ex": "Eine gute Frage!", "exEn": "A good question!"},
                {"word": "der Zeit", "article": "die", "badge": "noun", "translation": "the time", "ipa": "/tsaɪt/", "ex": "Ich habe keine Zeit.", "exEn": "I have no time."},
                {"word": "das Geld", "article": "das", "badge": "noun", "translation": "the money", "ipa": "/ɡɛlt/", "ex": "Hast du Geld?", "exEn": "Do you have money?"},
                {"word": "müde", "article": "", "badge": "adjective", "translation": "tired", "ipa": "/ˈmyːdə/", "ex": "Ich bin müde.", "exEn": "I am tired."},
                {"word": "hungrig", "article": "", "badge": "adjective", "translation": "hungry", "ipa": "/ˈhʊŋʁɪç/", "ex": "Bist du hungrig?", "exEn": "Are you hungry?"},
                {"word": "durstig", "article": "", "badge": "adjective", "translation": "thirsty", "ipa": "/ˈdʊʁstɪç/", "ex": "Wir sind durstig.", "exEn": "We are thirsty."},
                {"word": "kein", "article": "", "badge": "article", "translation": "no / not any (masc/neut)", "ipa": "/kaɪn/", "ex": "Ich habe kein Geld.", "exEn": "I have no money."}
            ],
            "grammarTitle": "sein vs haben in Everyday Expressions",
            "grammarContent": """
### Comparing **sein** and **haben**

| Pronoun | sein (to be) | haben (to have) |
|:---:|:---:|:---:|
| ich | **bin** | **habe** |
| du | **bist** | **hast** |
| er/sie/es | **ist** | **hat** |
| wir | **sind** | **haben** |
| ihr | **seid** | **habt** |
| sie/Sie | **sind** | **haben** |

> <Icon name="target" /> **Expressing Feelings:**  
> • German uses **sein** for physical states: *Ich bin müde.* (I am tired).  
> • German can also use **haben** + Noun: *Ich habe Hunger.* (I have hunger = I am hungry).
""",
            "fillIns": [
                {"q": "Ich ___ (haben) eine Frage.", "a": "habe"},
                {"q": "Er ___ (sein) müde.", "a": "ist"},
                {"q": "Hast du ___ (no) Geld?", "a": "kein"},
                {"q": "Wir ___ (haben) Zeit.", "a": "haben"},
                {"q": "Bist du ___ (hungry)?", "a": "hungrig"}
            ],
            "quiz": [
                {"question": "How do you say 'I am tired' in German?", "answer": "Ich bin müde.", "options": ["Ich bin müde.", "Ich habe müde.", "Ich bin hungrig.", "Ich habe Zeit."]},
                {"question": "Translate: 'I have no money.'", "answer": "Ich habe kein Geld.", "options": ["Ich bin kein Geld.", "Ich habe kein Geld.", "Ich habe nicht Geld.", "Ich bin ohne Geld."]},
                {"question": "Conjugate: Er ___ (haben) Zeit.", "answer": "hat", "options": ["habe", "hast", "hat", "haben"]},
                {"question": "What is the opposite of 'durstig'?", "answer": "satt", "options": ["hungrig", "müde", "satt", "krank"]}
            ],
            "checkpoints": [
                "I can conjugate both sein and haben effortlessly",
                "I know how to express tiredness and hunger in German",
                "I can use the negative article kein",
                "I am ready for the Week 1 review test!"
            ],
            "tomorrow": "Week 1 Mastery Review & Speaking Test!"
        },
        {
            "dayNum": 7, "title": "Week 1 Mastery Review",
            "isReview": True,
            "reviewCards": [
                {"german": "Hallo", "english": "Hello / Hi", "ipa": "/ˈhaloː/", "example": "Hallo! Wie heißt du?"},
                {"german": "Guten Morgen", "english": "Good morning", "ipa": "/ˈɡuːtən ˈmɔʁɡən/", "example": "Guten Morgen, Herr Schmidt!"},
                {"german": "Guten Tag", "english": "Good day / Hello", "ipa": "/ˈɡuːtən taːk/", "example": "Guten Tag! Ich bin Anna."},
                {"german": "Guten Abend", "english": "Good evening", "ipa": "/ˈɡuːtən ˈaːbənt/", "example": "Guten Abend, wie geht es Ihnen?"},
                {"german": "Tschüss", "english": "Bye (informal)", "ipa": "/tʃʏs/", "example": "Tschüss, bis morgen!"},
                {"german": "Auf Wiedersehen", "english": "Goodbye (formal)", "ipa": "/aʊf ˈviːdɐzeːən/", "example": "Auf Wiedersehen, Frau Müller!"},
                {"german": "ich / du / er / sie", "english": "I / you / he / she", "ipa": "/ɪç/ /duː/", "example": "Ich bin Student."},
                {"german": "sein (bin/bist/ist)", "english": "to be", "ipa": "/zaɪn/", "example": "Ich bin aus Deutschland."},
                {"german": "haben (habe/hast/hat)", "english": "to have", "ipa": "/ˈhaːbən/", "example": "Ich habe eine Frage."},
                {"german": "der / die / das", "english": "the (m/f/n)", "ipa": "/deːɐ/ /diː/ /das/", "example": "der Mann, die Frau, das Kind"}
            ],
            "grammarSummary": """
### Week 1 Grammar Recap

• **Greetings**: Guten Morgen, Guten Tag, Guten Abend, Tschüss, Auf Wiedersehen
• **Personal Pronouns**: ich, du, er/sie/es, wir, ihr, sie/Sie
• **Verbs**: sein (bin, bist, ist, sind, seid) & haben (habe, hast, hat, haben, habt)
• **Numbers 1-20**: eins, zwei, drei ... zwanzig
• **Nouns & Gender**: der Mann (m), die Frau (f), das Kind (n)
• **Indefinite Articles**: ein Mann (m), eine Frau (f), ein Kind (n)
""",
            "quiz": [
                {"question": "How do you introduce yourself formally in German?", "answer": "Guten Tag, ich heiße...", "options": ["Hallo, ich bin...", "Guten Tag, ich heiße...", "Tschüss, ich bin...", "Danke, ich bin..."]},
                {"question": "What is the correct conjugation: Wir ___ (sein) aus Deutschland.", "answer": "sind", "options": ["bin", "bist", "ist", "sind"]},
                {"question": "What is the indefinite article for 'Frau'?", "answer": "eine", "options": ["ein", "eine", "einen", "eines"]},
                {"question": "How do you ask someone's age?", "answer": "Wie alt bist du?", "options": ["Wie alt bist du?", "Wie bist du?", "Wie alt hast du?", "Wie heißt du?"]}
            ],
            "speakingPrompt": """
> <Icon name="mic" /> **Speaking Challenge:** Introduce yourself in 3 complete German sentences:  
> 1. *Hallo, ich heiße [Name].*  
> 2. *Ich komme aus [Country].*  
> 3. *Ich bin [Age] Jahre alt.*
""",
            "checkpoints": [
                "I can introduce myself fluently in German",
                "I know all numbers 1-20 and days of the week",
                "I understand der, die, das and ein, eine",
                "I am confident to start Week 2!"
            ]
        }
    ]
})
