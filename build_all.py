import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))

# Full curriculum definition for Weeks 2-12
weeks_data = [
    # WEEK 2
    {
        "weekNum": 2,
        "title": "Family & Possessives",
        "level": "A1.1",
        "goal": "Describe your family, use possessive pronouns (mein, dein, sein, ihr), state ages and jobs, and count up to 100.",
        "days": [
            {
                "dayNum": 8,
                "title": "Family Vocabulary 1",
                "vocab": [
                    {"word": "die Mutter", "article": "die", "badge": "noun", "translation": "the mother", "ipa": "/ˈmʊtɐ/", "ex": "Das ist meine Mutter.", "exEn": "That is my mother."},
                    {"word": "der Vater", "article": "der", "badge": "noun", "translation": "the father", "ipa": "/ˈfaːtɐ/", "ex": "Mein Vater heißt Klaus.", "exEn": "My father's name is Klaus."},
                    {"word": "die Schwester", "article": "die", "badge": "noun", "translation": "the sister", "ipa": "/ˈʃvɛstɐ/", "ex": "Ich habe eine Schwester.", "exEn": "I have a sister."},
                    {"word": "der Bruder", "article": "der", "badge": "noun", "translation": "the brother", "ipa": "/ˈbʁuːdɐ/", "ex": "Mein Bruder ist 18 Jahre alt.", "exEn": "My brother is 18 years old."},
                    {"word": "die Eltern", "article": "die", "badge": "noun", "translation": "the parents (pl)", "ipa": "/ˈɛltɐn/", "ex": "Meine Eltern wohnen in Hamburg.", "exEn": "My parents live in Hamburg."},
                    {"word": "die Familie", "article": "die", "badge": "noun", "translation": "the family", "ipa": "/faˈmiːliə/", "ex": "Meine Familie ist groß.", "exEn": "My family is big."},
                    {"word": "das Baby", "article": "das", "badge": "noun", "translation": "the baby", "ipa": "/ˈbeːbi/", "ex": "Das Baby schläft.", "exEn": "The baby is sleeping."},
                    {"word": "die Großmutter", "article": "die", "badge": "noun", "translation": "the grandmother", "ipa": "/ˈɡʁoːsmʊtɐ/", "ex": "Meine Großmutter ist 70 Jahre alt.", "exEn": "My grandmother is 70 years old."}
                ],
                "grammarTitle": "The Verb haben (to have) & Family Nouns",
                "grammarContent": """
### Conjugation: **haben** (to have)

| Pronoun | Form | Pronunciation |
|:---:|:---:|:---:|
| ich | hab**e** | /ˈhaːbə/ |
| du | ha**st** | /hast/ |
| er/sie/es | ha**t** | /hat/ |
| wir | hab**en** | /ˈhaːbən/ |
| ihr | hab**t** | /hapt/ |
| Sie/sie | hab**en** | /ˈhaːbən/ |

> 🎯 **Expressing Family:** Use *haben* + accusative article:  
> • Ich habe **einen** Bruder. (masculine → einen)  
> • Ich habe **eine** Schwester. (feminine → eine)  
> • Ich habe **ein** Baby. (neuter → ein)  
> • Ich habe **keine** Geschwister. (negative → keine)
""",
                "fillIns": [
                    {"q": "Ich ___ (haben) eine große Familie.", "a": "habe"},
                    {"q": "___ (du / haben) einen Bruder?", "a": "Hast du"},
                    {"q": "Er ___ (haben) zwei Schwestern.", "a": "hat"},
                    {"q": "Wir ___ (haben) eine liebe Großmutter.", "a": "haben"},
                    {"q": "Ich habe ___ (no / not a) Bruder.", "a": "keinen"}
                ],
                "quiz": [
                    {"question": "What is the German word for mother?", "answer": "die Mutter", "options": ["der Vater", "die Mutter", "die Schwester", "die Tante"]},
                    {"question": "Conjugate: Er ___ (haben) ein Baby.", "answer": "hat", "options": ["habe", "hast", "hat", "haben"]},
                    {"question": "How do you say 'I have a brother'?", "answer": "Ich habe einen Bruder.", "options": ["Ich habe ein Bruder.", "Ich habe einen Bruder.", "Ich habe eine Bruder.", "Ich habe der Bruder."]},
                    {"question": "What does 'die Eltern' mean?", "answer": "the parents", "options": ["the elders", "the parents", "the uncles", "the sisters"]}
                ],
                "checkpoints": [
                    "I can name 8 core family members in German",
                    "I can conjugate the irregular verb haben",
                    "I know to use einen Bruder for masculine accusative",
                    "I can say if I have brothers or sisters"
                ],
                "tomorrow": "Possessive determiners mein (my) and dein (your)!"
            },
            {
                "dayNum": 9,
                "title": "Possessive Determiners: mein & dein",
                "vocab": [
                    {"word": "der Großvater", "article": "der", "badge": "noun", "translation": "the grandfather", "ipa": "/ˈɡʁoːsfaːtɐ/", "ex": "Mein Großvater kommt aus Polen.", "exEn": "My grandfather comes from Poland."},
                    {"word": "der Sohn", "article": "der", "badge": "noun", "translation": "the son", "ipa": "/zoːn/", "ex": "Mein Sohn ist zehn Jahre alt.", "exEn": "My son is ten years old."},
                    {"word": "die Tochter", "article": "die", "badge": "noun", "translation": "the daughter", "ipa": "/ˈtɔxtɐ/", "ex": "Meine Tochter heißt Lisa.", "exEn": "My daughter is named Lisa."},
                    {"word": "die Oma", "article": "die", "badge": "noun", "translation": "grandma (informal)", "ipa": "/ˈoːma/", "ex": "Meine Oma backt Kuchen.", "exEn": "My grandma bakes cake."},
                    {"word": "der Opa", "article": "der", "badge": "noun", "translation": "grandpa (informal)", "ipa": "/ˈoːpa/", "ex": "Mein Opa ist Rentner.", "exEn": "My grandpa is a retiree."},
                    {"word": "die Tante", "article": "die", "badge": "noun", "translation": "the aunt", "ipa": "/ˈtantə/", "ex": "Meine Tante wohnt in Wien.", "exEn": "My aunt lives in Vienna."},
                    {"word": "der Onkel", "article": "der", "badge": "noun", "translation": "the uncle", "ipa": "/ˈɔŋkəl/", "ex": "Mein Onkel ist Arzt.", "exEn": "My uncle is a doctor."},
                    {"word": "der Cousin", "article": "der", "badge": "noun", "translation": "the cousin (m)", "ipa": "/kuˈzɛ̃/", "ex": "Mein Cousin spielt Fußball.", "exEn": "My cousin plays football."}
                ],
                "grammarTitle": "Possessives: mein (my) & dein (your)",
                "grammarContent": """
### Possessive Determiners (Nominative)

| Gender | my | your (informal) | Example |
|:---:|:---:|:---:|:---|
| **Masculine** | **mein** | **dein** | mein Vater, dein Opa |
| **Feminine** | **meine** | **deine** | meine Mutter, deine Oma |
| **Neuter** | **mein** | **dein** | mein Kind, dein Baby |
| **Plural** | **meine** | **deine** | meine Eltern, deine Tanten |

> 💡 **Golden Rule:** If the noun is **feminine or plural**, add **-e**!  
> • mein Sohn (masc) vs. meine Tochter (fem)  
> • dein Opa (masc) vs. deine Oma (fem)
""",
                "fillIns": [
                    {"q": "Das ist ___ (my) Vater.", "a": "mein"},
                    {"q": "Ist das ___ (your) Mutter?", "a": "deine"},
                    {"q": "___ (my) Tochter heißt Sarah.", "a": "Meine"},
                    {"q": "Wo wohnt ___ (your) Onkel?", "a": "dein"},
                    {"q": "___ (my) Eltern wohnen in Berlin.", "a": "Meine"}
                ],
                "quiz": [
                    {"question": "What form of 'my' is used with feminine nouns?", "answer": "meine", "options": ["mein", "meine", "meinen", "meiner"]},
                    {"question": "Translate: 'Is that your sister?'", "answer": "Ist das deine Schwester?", "options": ["Ist das dein Schwester?", "Ist das deine Schwester?", "Ist das mein Schwester?", "Ist das du Schwester?"]},
                    {"question": "What is 'der Sohn'?", "answer": "the son", "options": ["the sun", "the son", "the uncle", "the cousin"]},
                    {"question": "Choose correct: ___ (my) Opa ist 80 Jahre alt.", "answer": "Mein", "options": ["Mein", "Meine", "Meinen", "Meines"]}
                ],
                "checkpoints": [
                    "I know when to use mein vs meine",
                    "I know when to use dein vs deine",
                    "I can talk about extended family (Tante, Onkel, Oma, Opa)",
                    "I can ask someone about their family"
                ],
                "tomorrow": "Possessives for his/her/our (sein, ihr, unser) and describing personality!"
            },
            {
                "dayNum": 10,
                "title": "Possessives: sein, ihr, unser & Adjectives",
                "vocab": [
                    {"word": "verheiratet", "article": "", "badge": "adj", "translation": "married", "ipa": "/fɛɐˈhaɪʁatɛt/", "ex": "Meine Schwester ist verheiratet.", "exEn": "My sister is married."},
                    {"word": "ledig", "article": "", "badge": "adj", "translation": "single / unmarried", "ipa": "/ˈleːdɪç/", "ex": "Ich bin ledig.", "exEn": "I am single."},
                    {"word": "geschieden", "article": "", "badge": "adj", "translation": "divorced", "ipa": "/ɡəˈʃiːdən/", "ex": "Er ist geschieden.", "exEn": "He is divorced."},
                    {"word": "jung", "article": "", "badge": "adj", "translation": "young", "ipa": "/jʊŋ/", "ex": "Mein Bruder ist sehr jung.", "exEn": "My brother is very young."},
                    {"word": "groß", "article": "", "badge": "adj", "translation": "tall / big", "ipa": "/ɡʁoːs/", "ex": "Mein Vater ist sehr groß.", "exEn": "My father is very tall."},
                    {"word": "klein", "article": "", "badge": "adj", "translation": "short / small", "ipa": "/klaɪn/", "ex": "Meine Mutter ist klein.", "exEn": "My mother is short."},
                    {"word": "nett", "article": "", "badge": "adj", "translation": "nice / friendly", "ipa": "/nɛt/", "ex": "Meine Familie ist sehr nett.", "exEn": "My family is very nice."},
                    {"word": "sympathisch", "article": "", "badge": "adj", "translation": "likeable / pleasant", "ipa": "/zʏmˈpaːtɪʃ/", "ex": "Mein Onkel ist sehr sympathisch.", "exEn": "My uncle is very pleasant."}
                ],
                "grammarTitle": "Possessives: sein (his) & ihr (her/their/your formal)",
                "grammarContent": """
### All Possessive Determiners

| Subject | Masculine / Neuter | Feminine / Plural | Example |
|:---:|:---:|:---:|:---|
| **ich** (I) | mein | meine | mein Bruder |
| **du** (you) | dein | deine | deine Schwester |
| **er** (he) | **sein** | **seine** | sein Vater / seine Mutter |
| **sie** (she) | **ihr** | **ihre** | ihr Sohn / ihre Tochter |
| **wir** (we) | **unser** | **unsere** | unser Haus / unsere Eltern |
| **Sie** (you, formal) | **Ihr** | **Ihre** | Ihr Mann / Ihre Frau |

> 🎯 **Key Distinction:**  
> • **sein** = his (describing a man's family: Peter und *sein* Bruder)  
> • **ihr** = her (describing a woman's family: Anna und *ihre* Schwester)
""",
                "fillIns": [
                    {"q": "Das ist Thomas und ___ (his) Frau.", "a": "seine"},
                    {"q": "Das ist Maria und ___ (her) Sohn.", "a": "ihr"},
                    {"q": "Wir lieben ___ (our) Familie.", "a": "unsere"},
                    {"q": "Herr Müller, wie heißt ___ (your, formal) Frau?", "a": "Ihre"},
                    {"q": "Er ist ___ (single) und 25 Jahre alt.", "a": "ledig"}
                ],
                "quiz": [
                    {"question": "What possessive means 'his' for a feminine noun?", "answer": "seine", "options": ["sein", "seine", "ihr", "ihre"]},
                    {"question": "What possessive means 'her' for a masculine noun?", "answer": "ihr", "options": ["sein", "seine", "ihr", "ihre"]},
                    {"question": "Translate 'ledig':", "answer": "single / unmarried", "options": ["married", "divorced", "single / unmarried", "young"]},
                    {"question": "What is 'our house' in German?", "answer": "unser Haus", "options": ["unser Haus", "unsere Haus", "sein Haus", "ihr Haus"]}
                ],
                "checkpoints": [
                    "I can use sein/seine for his",
                    "I can use ihr/ihre for her",
                    "I can state marital status (ledig, verheiratet, geschieden)",
                    "I can describe family members with basic adjectives"
                ],
                "tomorrow": "Describing professions and work without articles!"
            },
            {
                "dayNum": 11,
                "title": "Describing Professions & Work",
                "vocab": [
                    {"word": "der Beruf", "article": "der", "badge": "noun", "translation": "the job / profession", "ipa": "/beˈʁuːf/", "ex": "Was ist Ihr Beruf?", "exEn": "What is your profession?"},
                    {"word": "der Arzt", "article": "der", "badge": "noun", "translation": "the doctor (m)", "ipa": "/aːɐtst/", "ex": "Mein Vater ist Arzt.", "exEn": "My father is a doctor."},
                    {"word": "die Ärztin", "article": "die", "badge": "noun", "translation": "the doctor (f)", "ipa": "/ˈɛːɐtstn̩/", "ex": "Meine Mutter ist Ärztin.", "exEn": "My mother is a doctor."},
                    {"word": "der Lehrer", "article": "der", "badge": "noun", "translation": "the teacher (m)", "ipa": "/ˈleːʁɐ/", "ex": "Mein Bruder ist Lehrer.", "exEn": "My brother is a teacher."},
                    {"word": "die Lehrerin", "article": "die", "badge": "noun", "translation": "the teacher (f)", "ipa": "/ˈleːʁɐʁɪn/", "ex": "Meine Tante ist Lehrerin.", "exEn": "My aunt is a teacher."},
                    {"word": "der Student", "article": "der", "badge": "noun", "translation": "the student (m)", "ipa": "/ʃtuˈdɛnt/", "ex": "Ich bin Student.", "exEn": "I am a student."},
                    {"word": "die Studentin", "article": "die", "badge": "noun", "translation": "the student (f)", "ipa": "/ʃtuˈdɛntɪn/", "ex": "Meine Schwester ist Studentin.", "exEn": "My sister is a student."},
                    {"word": "arbeiten", "article": "", "badge": "verb", "translation": "to work", "ipa": "/ˈaʁbaɪtən/", "ex": "Wo arbeitest du?", "exEn": "Where do you work?"}
                ],
                "grammarTitle": "Professions in German — No Articles!",
                "grammarContent": """
### Key Rule: No Article with Professions

In German, when saying what someone's job is after *sein* or *arbeiten als*, **DO NOT use an article**!

• English: I am **a** doctor.  
• German: Ich bin **Arzt**. (NOT: Ich bin *ein* Arzt.)

### Feminine Job Suffix: **-in**

Most female job titles are formed by adding **-in** to the masculine form (and sometimes adding an umlaut):

| Masculine | Feminine | Meaning |
|:---:|:---:|:---:|
| der Lehrer | die Lehrer**in** | teacher |
| der Student | die Student**in** | university student |
| der Arzt | die **Ä**rzt**in** | doctor |
| der Kellner | die Kellner**in** | waiter / waitress |

> 🗣️ **Asking someone's job:**  
> • Informal: *Was bist du von Beruf?* / *Was machst du?*  
> • Formal: *Was sind Sie von Beruf?* / *Was arbeiten Sie?*
""",
                "fillIns": [
                    {"q": "Ich bin ___ (teacher, f).", "a": "Lehrerin"},
                    {"q": "Er arbeitet ___ (as) Arzt.", "a": "als"},
                    {"q": "Was ___ (be) du von Beruf?", "a": "bist"},
                    {"q": "Meine Schwester ___ (arbeiten) in Berlin.", "a": "arbeitet"},
                    {"q": "Mein Vater ist ___ (no article) Ingenieur.", "a": "—"}
                ],
                "quiz": [
                    {"question": "How do you say 'I am a doctor' (male) in German?", "answer": "Ich bin Arzt.", "options": ["Ich bin ein Arzt.", "Ich bin Arzt.", "Ich bin der Arzt.", "Ich habe Arzt."]},
                    {"question": "What suffix creates feminine job titles?", "answer": "-in", "options": ["-en", "-in", "-es", "-ung"]},
                    {"question": "How do you ask 'What is your job?' formally?", "answer": "Was sind Sie von Beruf?", "options": ["Wie heißen Sie?", "Was sind Sie von Beruf?", "Wo arbeiten du?", "Wer bist du?"]},
                    {"question": "What is 'die Studentin'?", "answer": "the female student", "options": ["the male student", "the female student", "the high schooler", "the teacher"]}
                ],
                "checkpoints": [
                    "I know NOT to use an article when stating professions",
                    "I know how to form feminine job titles with -in",
                    "I can ask someone what their job is (formal & informal)",
                    "I can describe my job or studies"
                ],
                "tomorrow": "Numbers 21 to 100 and stating ages!"
            },
            {
                "dayNum": 12,
                "title": "Numbers 21–100 & Ages",
                "vocab": [
                    {"word": "dreißig", "article": "", "badge": "phrase", "translation": "thirty (30)", "ipa": "/ˈdʁaɪsɪç/", "ex": "Ich bin dreißig Jahre alt.", "exEn": "I am thirty years old."},
                    {"word": "vierzig", "article": "", "badge": "phrase", "translation": "forty (40)", "ipa": "/ˈfɪʁtsɪç/", "ex": "Er ist vierzig Jahre alt.", "exEn": "He is forty years old."},
                    {"word": "fünfzig", "article": "", "badge": "phrase", "translation": "fifty (50)", "ipa": "/ˈfʏnftsɪç/", "ex": "Meine Mutter ist fünfzig.", "exEn": "My mother is fifty."},
                    {"word": "sechzig", "article": "", "badge": "phrase", "translation": "sixty (60)", "ipa": "/ˈzɛçtsɪç/", "ex": "Mein Opa ist sechzig Jahre alt.", "exEn": "My grandpa is sixty years old."},
                    {"word": "siebzig", "article": "", "badge": "phrase", "translation": "seventy (70)", "ipa": "/ˈziːptsɪç/", "ex": "Meine Oma ist siebzig.", "exEn": "My grandma is seventy."},
                    {"word": "achtzig", "article": "", "badge": "phrase", "translation": "eighty (80)", "ipa": "/ˈaxtsɪç/", "ex": "Der Großvater ist achtzig.", "exEn": "The grandfather is eighty."},
                    {"word": "neunzig", "article": "", "badge": "phrase", "translation": "ninety (90)", "ipa": "/ˈnɔʏntsɪç/", "ex": "Er ist neunzig Jahre alt.", "exEn": "He is ninety years old."},
                    {"word": "hundert", "article": "", "badge": "phrase", "translation": "hundred (100)", "ipa": "/ˈhʊndɐt/", "ex": "Es kostet hundert Euro.", "exEn": "It costs a hundred euros."}
                ],
                "grammarTitle": "German Compound Numbers (21–99)",
                "grammarContent": """
### Structure of German Numbers 21–99

In German, numbers from 21 onwards are spoken **backwards**:  
👉 **Ones + und + Tens** (written as a single long word!)

| Number | Breakdown | German |
|:---:|:---:|:---|
| **21** | 1 + and + 20 | **ein**undzwanzig |
| **35** | 5 + and + 30 | fünfund**dreißig** |
| **42** | 2 + and + 40 | zweiundvierzig |
| **67** | 7 + and + 60 | siebenundsechzig |
| **89** | 9 + and + 80 | neunundachtzig |

> ⚠️ **Watch Out:**  
> • 21 is *ein*undzwanzig (no 's' on eins!)  
> • 30 is *drei**ß**ig* (uses 'ß', not 'z')  
> • 60 is *sechzig* (drops 's' from sechs)  
> • 70 is *siebzig* (drops 'en' from sieben)
""",
                "fillIns": [
                    {"q": "25 in German is: fünfund___.", "a": "zwanzig"},
                    {"q": "41 in German is: ___undvierzig.", "a": "ein"},
                    {"q": "30 is written with 'ß': ___.", "a": "dreißig"},
                    {"q": "70 in German is: ___ (not siebenzig).", "a": "siebzig"},
                    {"q": "Mein Vater ist 54 Jahre alt: ___undfünfzig.", "a": "vier"}
                ],
                "quiz": [
                    {"question": "What is 35 in German?", "answer": "fünfunddreißig", "options": ["dreißigundfünf", "fünfunddreißig", "fünfzehndreißig", "dreifünf"]},
                    {"question": "How do you write 21?", "answer": "einundzwanzig", "options": ["einsundzwanzig", "einundzwanzig", "zwanzigundeins", "zweieins"]},
                    {"question": "What is 70 in German?", "answer": "siebzig", "options": ["siebenzig", "siebzig", "siebzehn", "siebenhundert"]},
                    {"question": "Translate: 'He is 48 years old.'", "answer": "Er ist achtundvierzig Jahre alt.", "options": ["Er hat 48 Jahre.", "Er ist achtundvierzig Jahre alt.", "Er ist vierzigundacht Jahre alt.", "Er wohnt 48 Jahre."]}
                ],
                "checkpoints": [
                    "I can count by tens (20, 30, 40... 100)",
                    "I understand how compound numbers work (ones + und + tens)",
                    "I can say my age and my family members' ages",
                    "I know that 30 uses -ßig"
                ],
                "tomorrow": "Family description paragraphs and connectors!"
            },
            {
                "dayNum": 13,
                "title": "Family Descriptions & Paragraph Writing",
                "vocab": [
                    {"word": "das Foto", "article": "das", "badge": "noun", "translation": "the photo", "ipa": "/ˈfoːto/", "ex": "Das ist ein Foto von meiner Familie.", "exEn": "That is a photo of my family."},
                    {"word": "zusammen", "article": "", "badge": "phrase", "translation": "together", "ipa": "/tsuˈzamən/", "ex": "Wir wohnen zusammen.", "exEn": "We live together."},
                    {"word": "noch", "article": "", "badge": "phrase", "translation": "still / yet", "ipa": "/nɔx/", "ex": "Ich wohne noch bei meinen Eltern.", "exEn": "I still live with my parents."},
                    {"word": "schon", "article": "", "badge": "phrase", "translation": "already", "ipa": "/ʃoːn/", "ex": "Mein Bruder ist schon verheiratet.", "exEn": "My brother is already married."},
                    {"word": "allein", "article": "", "badge": "phrase", "translation": "alone / by oneself", "ipa": "/aˈlaɪn/", "ex": "Meine Schwester wohnt allein.", "exEn": "My sister lives alone."},
                    {"word": "das Geschwister", "article": "das", "badge": "noun", "translation": "the sibling", "ipa": "/ɡəˈʃvɪstɐ/", "ex": "Ich habe zwei Geschwister.", "exEn": "I have two siblings."},
                    {"word": "das Einzelkind", "article": "das", "badge": "noun", "translation": "the only child", "ipa": "/ˈaɪntsl̩kɪnt/", "ex": "Ich bin Einzelkind.", "exEn": "I am an only child."},
                    {"word": "die Großeltern", "article": "die", "badge": "noun", "translation": "the grandparents (pl)", "ipa": "/ˈɡʁoːsˌɛltɐn/", "ex": "Meine Großeltern leben in Bayern.", "exEn": "My grandparents live in Bavaria."}
                ],
                "grammarTitle": "Structuring a Personal / Family Profile",
                "grammarContent": """
### Sample Family Profile Paragraph

> *"Hallo! Ich heiße Lukas. Ich bin 28 Jahre alt und wohne in Berlin. Ich bin ledig und habe zwei Geschwister: einen Bruder und eine Schwester. Mein Bruder heißt Stefan, er ist 25 und arbeitet als Ingenieur. Meine Schwester heißt Lisa, sie ist 22 und ist Studentin. Unsere Eltern wohnen in Hamburg."*

### Key Sentence Connectors

| German | English | Usage |
|:---:|:---:|:---|
| **und** | and | connects similar ideas |
| **aber** | but | contrasts ideas (Ich bin 25, *aber* mein Bruder ist 30) |
| **auch** | also | adds info (Meine Schwester ist *auch* Studentin) |
| **schon** | already | time progress (Er ist *schon* 60) |
| **noch** | still | ongoing state (Ich wohne *noch* zu Hause) |
""",
                "fillIns": [
                    {"q": "Ich bin ___ (only child).", "a": "Einzelkind"},
                    {"q": "Wir wohnen ___ (together) in München.", "a": "zusammen"},
                    {"q": "Ich habe zwei ___ (siblings).", "a": "Geschwister"},
                    {"q": "Mein Bruder ist ___ (already) 30 Jahre alt.", "a": "schon"},
                    {"q": "Ich wohne ___ (still) bei den Eltern.", "a": "noch"}
                ],
                "quiz": [
                    {"question": "What is 'Einzelkind'?", "answer": "only child", "options": ["single child", "only child", "first child", "youngest child"]},
                    {"question": "What word means 'together'?", "answer": "zusammen", "options": ["allein", "zusammen", "schon", "noch"]},
                    {"question": "Translate: 'I still live in Berlin.'", "answer": "Ich wohne noch in Berlin.", "options": ["Ich wohne schon in Berlin.", "Ich wohne noch in Berlin.", "Ich wohne allein in Berlin.", "Ich wohne zusammen in Berlin."]},
                    {"question": "What does 'Geschwister' mean?", "answer": "siblings", "options": ["parents", "grandparents", "siblings", "children"]}
                ],
                "checkpoints": [
                    "I can write a 5-sentence paragraph describing my family",
                    "I can use connectors like und, aber, auch, schon, noch",
                    "I know terms like Einzelkind and Geschwister",
                    "I can state ages and jobs of multiple people"
                ],
                "tomorrow": "Week 2 Review and Speaking Practice!"
            },
            {
                "dayNum": 14,
                "isReview": True,
                "title": "Week 2 Review & Speaking Practice",
                "reviewCards": [
                    {"german": "die Mutter", "english": "mother", "example": "Das ist meine Mutter."},
                    {"german": "der Vater", "english": "father", "example": "Mein Vater heißt Klaus."},
                    {"german": "die Eltern", "english": "parents", "example": "Meine Eltern wohnen in Berlin."},
                    {"german": "mein / meine", "english": "my (m/f)", "example": "mein Bruder, meine Schwester"},
                    {"german": "dein / deine", "english": "your (m/f)", "example": "dein Opa, deine Oma"},
                    {"german": "sein / seine", "english": "his (m/f)", "example": "sein Sohn, seine Tochter"},
                    {"german": "ihr / ihre", "english": "her (m/f)", "example": "ihr Mann, ihre Frau"},
                    {"german": "verheiratet", "english": "married", "example": "Sie ist verheiratet."},
                    {"german": "ledig", "english": "single", "example": "Ich bin ledig."},
                    {"german": "der Beruf", "english": "job / profession", "example": "Was ist dein Beruf?"},
                    {"german": "der Arzt / die Ärztin", "english": "doctor (m/f)", "example": "Er ist Arzt."},
                    {"german": "dreißig / fünfzig", "english": "30 / 50", "example": "Sie ist fünfzig Jahre alt."},
                    {"german": "einundzwanzig", "english": "21", "example": "Ich bin einundzwanzig."},
                    {"german": "zusammen", "english": "together", "example": "Wir wohnen zusammen."},
                    {"german": "Geschwister", "english": "siblings", "example": "Ich habe zwei Geschwister."}
                ],
                "grammarSummary": """
### Week 2 Master Summary

1. **haben (to have):** ich habe, du hast, er/sie/es hat, wir haben, ihr habt, sie haben
2. **Accusative after haben:** Ich habe *einen* Bruder (m), *eine* Schwester (f), *ein* Kind (n).
3. **Possessives (Nominative):**
   - ich → mein / meine
   - du → dein / deine
   - er → sein / seine
   - sie → ihr / ihre
   - wir → unser / unsere
4. **Professions:** NO ARTICLE after *sein* or *arbeiten als*! Add *-in* for feminine forms (Lehrer → Lehrerin).
5. **Numbers 21–99:** Spoken backwards! *einundzwanzig* (21), *fünfunddreißig* (35).
""",
                "quiz": [
                    {"question": "What is the accusative form of 'ein Bruder' after haben?", "answer": "einen Bruder", "options": ["ein Bruder", "einen Bruder", "eine Bruder", "einem Bruder"]},
                    {"question": "Which possessive means 'her father'?", "answer": "ihr Vater", "options": ["sein Vater", "ihr Vater", "ihre Vater", "seine Vater"]},
                    {"question": "How do you say 'My sister is a female teacher'?", "answer": "Meine Schwester ist Lehrerin.", "options": ["Meine Schwester ist ein Lehrerin.", "Meine Schwester ist Lehrerin.", "Mein Schwester ist Lehrer.", "Meine Schwester hat Lehrerin."]},
                    {"question": "How do you say 46 in German?", "answer": "sechsundvierzig", "options": ["vierzigundsechs", "sechsundvierzig", "sechzehnvierzig", "viersechs"]},
                    {"question": "What is the opposite of 'verheiratet'?", "answer": "ledig", "options": ["geschieden", "ledig", "zusammen", "alt"]},
                    {"question": "Conjugate: Wir ___ (haben) zwei Kinder.", "answer": "haben", "options": ["habe", "hast", "hat", "haben"]},
                    {"question": "What does 'meine Großeltern' mean?", "answer": "my grandparents", "options": ["my parents", "my grandparents", "my grandchildren", "my uncles"]},
                    {"question": "Translate: 'Ich bin Einzelkind.'", "answer": "I am an only child.", "options": ["I have one child.", "I am an only child.", "I am single.", "I live alone."]}
                ],
                "speakingPrompt": """
### 🗣️ Speaking Exercise — Introduce Your Family

Read this script aloud and record yourself or practice with a partner:

> *"Hallo! Ich heiße [Name]. Ich bin [Age] Jahre alt. Ich bin [ledig / verheiratet]. Ich arbeite als [Job / Student]. Ich habe [Number] Geschwister: [einen Bruder / eine Schwester]. Mein Vater heißt [Name] und meine Mutter heißt [Name]. Wir wohnen in [City]."*
""",
                "checkpoints": [
                    "I can conjugate haben in all forms",
                    "I know possessives for ich, du, er, sie, wir",
                    "I can count to 100 in German",
                    "I can give a 1-minute spoken family presentation"
                ]
            }
        ]
    }
]

print("Script framework loaded successfully.")
