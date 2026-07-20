# Weeks 3 to 6 Data

weeks_3_to_6 = []

# --- WEEK 3 ---
weeks_3_to_6.append({
    "weekNum": 3,
    "title": "Home, Rooms & Furniture",
    "level": "A1.1",
    "goal": "Name house rooms, describe furniture, use 'es gibt' with accusative, understand plural noun patterns, and use basic location prepositions.",
    "days": [
        {
            "dayNum": 15, "title": "House Rooms & 'es gibt'",
            "vocab": [
                {"word": "die Wohnung", "article": "die", "badge": "noun", "translation": "the apartment", "ipa": "/ˈvoːnʊŋ/", "ex": "Ich habe eine kleine Wohnung.", "exEn": "I have a small apartment."},
                {"word": "das Haus", "article": "das", "badge": "noun", "translation": "the house", "ipa": "/haʊs/", "ex": "Wir wohnen in einem Haus.", "exEn": "We live in a house."},
                {"word": "die Küche", "article": "die", "badge": "noun", "translation": "the kitchen", "ipa": "/ˈkʏçə/", "ex": "Die Küche ist groß.", "exEn": "The kitchen is big."},
                {"word": "das Badezimmer", "article": "das", "badge": "noun", "translation": "the bathroom", "ipa": "/ˈbaːdəˌtsɪmɐ/", "ex": "Das Badezimmer ist sauber.", "exEn": "The bathroom is clean."},
                {"word": "das Schlafzimmer", "article": "das", "badge": "noun", "translation": "the bedroom", "ipa": "/ˈʃlaːfˌtsɪmɐ/", "ex": "Mein Schlafzimmer ist ruhig.", "exEn": "My bedroom is quiet."},
                {"word": "das Wohnzimmer", "article": "das", "badge": "noun", "translation": "the living room", "ipa": "/ˈvoːnˌtsɪmɐ/", "ex": "Das Wohnzimmer ist gemütlich.", "exEn": "The living room is cosy."},
                {"word": "das Zimmer", "article": "das", "badge": "noun", "translation": "the room", "ipa": "/ˈtsɪmɐ/", "ex": "Wie viele Zimmer hat die Wohnung?", "exEn": "How many rooms does the apartment have?"},
                {"word": "der Balkon", "article": "der", "badge": "noun", "translation": "the balcony", "ipa": "/balˈkɔŋ/", "ex": "Wir haben einen Balkon.", "exEn": "We have a balcony."}
            ],
            "grammarTitle": "The Structure: es gibt + Accusative",
            "grammarContent": """
### Expression: **es gibt** (there is / there are)

In German, *es gibt* means both "there is" and "there are".  
<Icon name="arrow-right" /> **Crucial Rule:** The object after *es gibt* is ALWAYS in the **accusative case**!

| Gender | Positive (a / an) | Negative (no / not a) | Example |
|:---:|:---:|:---:|:---|
| **Masculine** | es gibt **einen** | es gibt **keinen** | Es gibt *einen* Balkon. |
| **Feminine** | es gibt **eine** | es gibt **keine** | Es gibt *eine* Küche. |
| **Neuter** | es gibt **ein** | es gibt **kein** | Es gibt *ein* Bad. |
| **Plural** | es gibt | es gibt **keine** | Es gibt *drei* Zimmer. |

> <Icon name="message-square" /> **Asking questions:**  
> • *Gibt es einen Balkon?* → Ja, es gibt einen Balkon. / Nein, es gibt keinen Balkon.
""",
            "fillIns": [
                {"q": "In der Wohnung gibt es ___ (a, m) Balkon.", "a": "einen"},
                {"q": "Es gibt ___ (no, f) Küche.", "a": "keine"},
                {"q": "___ (there is) ein großes Wohnzimmer.", "a": "Es gibt"},
                {"q": "Gibt es ___ (a, n) Badezimmer?", "a": "ein"},
                {"q": "Es gibt ___ (no, m) Garten.", "a": "keinen"}
            ],
            "quiz": [
                {"question": "What case follows 'es gibt'?", "answer": "accusative", "options": ["nominative", "accusative", "dative", "genitive"]},
                {"question": "How do you say 'There is a balcony'?", "answer": "Es gibt einen Balkon.", "options": ["Es gibt ein Balkon.", "Es gibt einen Balkon.", "Es ist der Balkon.", "Es gibt der Balkon."]},
                {"question": "What is 'die Küche'?", "answer": "the kitchen", "options": ["the bedroom", "the kitchen", "the bathroom", "the cellar"]},
                {"question": "How do you say 'there is no bathroom'?", "answer": "Es gibt kein Badezimmer.", "options": ["Es gibt nicht Badezimmer.", "Es gibt kein Badezimmer.", "Es gibt keine Badezimmer.", "Es gibt keinen Badezimmer."]}
            ],
            "checkpoints": [
                "I know the names of all main rooms in a house",
                "I understand that es gibt triggers the accusative case",
                "I know that der Balkon becomes einen Balkon after es gibt",
                "I can describe what rooms an apartment has"
            ],
            "tomorrow": "Furniture vocabulary and accusative with haben!"
        },
        {
            "dayNum": 16, "title": "Furniture & haben + Accusative",
            "vocab": [
                {"word": "der Tisch", "article": "der", "badge": "noun", "translation": "the table", "ipa": "/tɪʃ/", "ex": "Der Tisch steht in der Küche.", "exEn": "The table stands in the kitchen."},
                {"word": "der Stuhl", "article": "der", "badge": "noun", "translation": "the chair", "ipa": "/ʃtuːl/", "ex": "Ich habe vier Stühle.", "exEn": "I have four chairs."},
                {"word": "das Bett", "article": "das", "badge": "noun", "translation": "the bed", "ipa": "/bɛt/", "ex": "Das Bett ist sehr bequem.", "exEn": "The bed is very comfortable."},
                {"word": "der Schrank", "article": "der", "badge": "noun", "translation": "the wardrobe / cupboard", "ipa": "/ʃʁaŋk/", "ex": "Der Schrank ist neu.", "exEn": "The wardrobe is new."},
                {"word": "das Sofa", "article": "das", "badge": "noun", "translation": "the sofa", "ipa": "/ˈzoːfa/", "ex": "Das Sofa ist grün.", "exEn": "The sofa is green."},
                {"word": "die Lampe", "article": "die", "badge": "noun", "translation": "the lamp", "ipa": "/ˈlampə/", "ex": "Die Lampe ist schön.", "exEn": "The lamp is nice."},
                {"word": "der Spiegel", "article": "der", "badge": "noun", "translation": "the mirror", "ipa": "/ˈʃpiːɡəl/", "ex": "Der Spiegel ist im Bad.", "exEn": "The mirror is in the bathroom."},
                {"word": "das Regal", "article": "das", "badge": "noun", "translation": "the shelf / bookcase", "ipa": "/ʁeˈɡaːl/", "ex": "Das Regal ist aus Holz.", "exEn": "The shelf is made of wood."}
            ],
            "grammarTitle": "The Accusative Case with haben",
            "grammarContent": """
### Accusative Case Summary (Direct Object)

Only **masculine** articles change in the accusative case! Feminine, neuter, and plural stay identical to nominative.

| Gender | Nominative (Subject) | Accusative (Object) | Example |
|:---:|:---:|:---:|:---|
| **Masculine** | **der / ein / kein** | **den / einen / keinen** | Ich habe *einen* Tisch. |
| **Feminine** | **die / eine / keine** | **die / eine / keine** | Ich habe *eine* Lampe. |
| **Neuter** | **das / ein / kein** | **das / ein / kein** | Ich habe *ein* Bett. |
| **Plural** | **die / - / keine** | **die / - / keine** | Ich habe *zwei* Stühle. |

> <Icon name="target" /> **Key takeaway:**  
> • der Tisch → Ich brauche **den** Tisch / Ich kaufe **einen** Tisch.
""",
            "fillIns": [
                {"q": "Ich kaufe ___ (a, m) Schrank.", "a": "einen"},
                {"q": "Wir haben ___ (a, n) großes Bett.", "a": "ein"},
                {"q": "Ich suche ___ (the, f) Lampe.", "a": "die"},
                {"q": "Er hat ___ (no, m) Tisch.", "a": "keinen"},
                {"q": "Brauchst du ___ (the, m) Spiegel?", "a": "den"}
            ],
            "quiz": [
                {"question": "Which gender changes in the accusative case?", "answer": "masculine only", "options": ["feminine only", "neuter only", "masculine only", "all genders"]},
                {"question": "How do you say 'I have a wardrobe'?", "answer": "Ich habe einen Schrank.", "options": ["Ich habe ein Schrank.", "Ich habe einen Schrank.", "Ich habe der Schrank.", "Ich habe eine Schrank."]},
                {"question": "What is 'das Regal'?", "answer": "the shelf", "options": ["the table", "the chair", "the shelf", "the mirror"]},
                {"question": "What is the accusative of 'der Stuhl' after haben?", "answer": "einen Stuhl", "options": ["ein Stuhl", "einen Stuhl", "eine Stuhl", "einem Stuhl"]}
            ],
            "checkpoints": [
                "I can name 8 common pieces of furniture",
                "I understand that der changes to den/einen in accusative",
                "I know that das and die remain unchanged in accusative",
                "I can list what furniture is in my room"
            ],
            "tomorrow": "German plural noun patterns!"
        },
        {
            "dayNum": 17, "title": "German Plural Noun Patterns",
            "vocab": [
                {"word": "das Buch", "article": "das", "badge": "noun", "translation": "the book (pl: Bücher)", "ipa": "/buːx/", "ex": "Ich lese ein Buch.", "exEn": "I am reading a book."},
                {"word": "das Fenster", "article": "das", "badge": "noun", "translation": "the window (pl: Fenster)", "ipa": "/ˈfɛnstɐ/", "ex": "Das Fenster ist offen.", "exEn": "The window is open."},
                {"word": "die Tür", "article": "die", "badge": "noun", "translation": "the door (pl: Türen)", "ipa": "/tyːɐ/", "ex": "Die Tür ist zu.", "exEn": "The door is closed."},
                {"word": "die Wand", "article": "die", "badge": "noun", "translation": "the wall (pl: Wände)", "ipa": "/vant/", "ex": "Die Wand ist weiß.", "exEn": "The wall is white."},
                {"word": "der Boden", "article": "der", "badge": "noun", "translation": "the floor (pl: Böden)", "ipa": "/ˈboːdən/", "ex": "Der Boden ist aus Holz.", "exEn": "The floor is made of wood."},
                {"word": "das Licht", "article": "das", "badge": "noun", "translation": "the light (pl: Lichter)", "ipa": "/lɪçt/", "ex": "Das Licht ist an.", "exEn": "The light is on."},
                {"word": "die Pflanze", "article": "die", "badge": "noun", "translation": "the plant (pl: Pflanzen)", "ipa": "/ˈpflanzə/", "ex": "Ich habe viele Pflanzen.", "exEn": "I have many plants."},
                {"word": "der Teppich", "article": "der", "badge": "noun", "translation": "the carpet (pl: Teppiche)", "ipa": "/ˈtɛpɪç/", "ex": "Der Teppich ist blau.", "exEn": "The carpet is blue."}
            ],
            "grammarTitle": "The 5 German Plural Rules",
            "grammarContent": """
### All Plural Nouns use **die**!

| Pattern | Singular → Plural | Ending | Example |
|:---:|:---:|:---:|:---|
| **1. No change** | das Fenster → die **Fenster** | - | -er / -el / -en endings |
| **2. Add -e** | der Tisch → die **Tische** | **-e** | most masculine nouns |
| **3. Add -er (+ Umlaut)** | das Buch → die **Bücher** | **-er** | most short neuter nouns |
| **4. Add -(e)n** | die Tür → die **Türen** | **-(e)n** | 90% of feminine nouns |
| **5. Add -s** | das Sofa → die **Sofas** | **-s** | foreign words & acronyms |

> <Icon name="lightbulb" /> **Golden Rule:** When learning a new noun, ALWAYS learn: **Article + Singular + Plural**  
> Example: *das Buch, die Bücher*
""",
            "fillIns": [
                {"q": "Singular: das Fenster → Plural: die ___.", "a": "Fenster"},
                {"q": "Singular: der Tisch → Plural: die ___.", "a": "Tische"},
                {"q": "Singular: das Buch → Plural: die ___.", "a": "Bücher"},
                {"q": "Singular: die Tür → Plural: die ___.", "a": "Türen"},
                {"q": "Singular: das Sofa → Plural: die ___.", "a": "Sofas"}
            ],
            "quiz": [
                {"question": "What article do ALL plural nouns take in the nominative?", "answer": "die", "options": ["der", "die", "das", "den"]},
                {"question": "What is the plural of 'das Buch'?", "answer": "die Bücher", "options": ["die Buche", "die Bücher", "die Büchern", "die Buchs"]},
                {"question": "What is the plural of 'die Tür'?", "answer": "die Türen", "options": ["die Türe", "die Türen", "die Türs", "die Türen"]},
                {"question": "Which plural pattern applies to foreign words like 'das Sofa'?", "answer": "add -s", "options": ["add -e", "add -er", "add -n", "add -s"]}
            ],
            "checkpoints": [
                "I know the 5 main plural formation rules",
                "I know that all plural nouns take 'die'",
                "I can form plurals for common room objects",
                "I know to learn article + singular + plural together"
            ],
            "tomorrow": "Describing rooms with adjectives!"
        },
        {
            "dayNum": 18, "title": "Describing Rooms & Adjectives",
            "vocab": [
                {"word": "groß", "article": "", "badge": "adj", "translation": "big / large", "ipa": "/ɡʁoːs/", "ex": "Mein Zimmer ist sehr groß.", "exEn": "My room is very big."},
                {"word": "klein", "article": "", "badge": "adj", "translation": "small", "ipa": "/klaɪn/", "ex": "Das Bad ist klein.", "exEn": "The bathroom is small."},
                {"word": "hell", "article": "", "badge": "adj", "translation": "bright / light", "ipa": "/hɛl/", "ex": "Die Küche ist sehr hell.", "exEn": "The kitchen is very bright."},
                {"word": "dunkel", "article": "", "badge": "adj", "translation": "dark", "ipa": "/ˈdʊŋkəl/", "ex": "Das Schlafzimmer ist dunkel.", "exEn": "The bedroom is dark."},
                {"word": "modern", "article": "", "badge": "adj", "translation": "modern", "ipa": "/moˈdɛʁn/", "ex": "Die Wohnung ist modern.", "exEn": "The apartment is modern."},
                {"word": "gemütlich", "article": "", "badge": "adj", "translation": "cosy / comfortable", "ipa": "/ɡəˈmyːtlɪç/", "ex": "Das Wohnzimmer ist sehr gemütlich.", "exEn": "The living room is very cosy."},
                {"word": "sauber", "article": "", "badge": "adj", "translation": "clean", "ipa": "/ˈzaʊbɐ/", "ex": "Das Badezimmer ist sauber.", "exEn": "The bathroom is clean."},
                {"word": "ordentlich", "article": "", "badge": "adj", "translation": "tidy / neat", "ipa": "/ˈɔʁdn̩tlɪç/", "ex": "Mein Zimmer ist ordentlich.", "exEn": "My room is tidy."}
            ],
            "grammarTitle": "Adjectives after sein (Predicate Adjectives)",
            "grammarContent": """
### Good News: No Adjective Endings After *sein*!

When an adjective comes **after** the verb *sein* (is/are), it **does not take any ending**! It remains in its base dictionary form regardless of gender or number!

• *Der Tisch ist* **groß**. (masculine)  
• *Die Küche ist* **groß**. (feminine)  
• *Das Bett ist* **groß**. (neuter)  
• *Die Zimmer sind* **groß**. (plural)

> <Icon name="lightbulb" /> **Comparison Words:**  
> • *sehr* = very (sehr groß)  
> • *ziemlich* = quite (ziemlich dunkel)  
> • *zu* = too (zu klein)
""",
            "fillIns": [
                {"q": "Das Wohnzimmer ist sehr ___ (cosy).", "a": "gemütlich"},
                {"q": "Die Küche ist ___ (bright) und sauber.", "a": "hell"},
                {"q": "Das Schlafzimmer ist zu ___ (dark).", "a": "dunkel"},
                {"q": "Mein Zimmer ist nicht groß, es ist ___ (small).", "a": "klein"},
                {"q": "Ist die Wohnung ___ (modern)?", "a": "modern"}
            ],
            "quiz": [
                {"question": "Do adjectives take endings when placed after 'ist' or 'sind'?", "answer": "no, they stay unchanged", "options": ["yes, add -e", "yes, add -en", "no, they stay unchanged", "depends on gender"]},
                {"question": "What does 'gemütlich' mean?", "answer": "cosy / comfortable", "options": ["dark", "tidy", "cosy / comfortable", "clean"]},
                {"question": "Translate: 'The kitchen is too small.'", "answer": "Die Küche ist zu klein.", "options": ["Die Küche ist sehr klein.", "Die Küche ist zu klein.", "Die Küche ist ziemlich klein.", "Die Küche ist klein zu."]},
                {"question": "What is the opposite of 'hell' (bright)?", "answer": "dunkel", "options": ["groß", "klein", "dunkel", "sauber"]}
            ],
            "checkpoints": [
                "I know 8 adjectives to describe rooms and furniture",
                "I understand predicate adjectives take NO endings after sein",
                "I know the modifiers sehr (very), ziemlich (quite), zu (too)",
                "I can describe my own room in 3 sentences"
            ],
            "tomorrow": "Location prepositions: links, rechts, neben, zwischen!"
        },
        {
            "dayNum": 19, "title": "Location Expressions & Prepositions",
            "vocab": [
                {"word": "links", "article": "", "badge": "phrase", "translation": "on the left", "ipa": "/lɪŋks/", "ex": "Das Bad ist links.", "exEn": "The bathroom is on the left."},
                {"word": "rechts", "article": "", "badge": "phrase", "translation": "on the right", "ipa": "/ʁɛçts/", "ex": "Die Küche ist rechts.", "exEn": "The kitchen is on the right."},
                {"word": "geradeaus", "article": "", "badge": "phrase", "translation": "straight ahead", "ipa": "/ɡəˈʁaːdəˈaʊs/", "ex": "Geradeaus ist das Wohnzimmer.", "exEn": "Straight ahead is the living room."},
                {"word": "oben", "article": "", "badge": "phrase", "translation": "upstairs / above", "ipa": "/ˈoːbən/", "ex": "Das Schlafzimmer ist oben.", "exEn": "The bedroom is upstairs."},
                {"word": "unten", "article": "", "badge": "phrase", "translation": "downstairs / below", "ipa": "/ˈʊntən/", "ex": "Das Wohnzimmer ist unten.", "exEn": "The living room is downstairs."},
                {"word": "neben", "article": "", "badge": "prep", "translation": "next to", "ipa": "/ˈneːbən/", "ex": "Das Bad ist neben der Küche.", "exEn": "The bathroom is next to the kitchen."},
                {"word": "zwischen", "article": "", "badge": "prep", "translation": "between", "ipa": "/ˈtsvɪʃən/", "ex": "Der Tisch steht zwischen dem Sofa und der Tür.", "exEn": "The table stands between the sofa and the door."},
                {"word": "gegenüber", "article": "", "badge": "prep", "translation": "opposite", "ipa": "/ˈɡeːɡənˌyːbɐ/", "ex": "Das Bad ist gegenüber dem Schlafzimmer.", "exEn": "The bathroom is opposite the bedroom."}
            ],
            "grammarTitle": "Describing Locations & Positions",
            "grammarContent": """
### Key Location Adverbs

| Direction | German | Example |
|:---:|:---:|:---|
| ⬅️ **Left** | **links** | Das Bad ist *links*. |
| ➡️ **Right** | **rechts** | Die Küche ist *rechts*. |
| ⬆️ **Straight** | **geradeaus** | Gehen Sie *geradeaus*. |
| ↗️ **Upstairs** | **oben** | Das Zimmer ist *oben*. |
| ↘️ **Downstairs** | **unten** | Der Keller ist *unten*. |

### Fixed Preposition Phrases (Location)

• **auf dem Tisch** = on the table  
• **im Regal** (in dem) = on / in the shelf  
• **an der Wand** = on the wall  
• **neben dem Bett** = next to the bed
""",
            "fillIns": [
                {"q": "Das Badezimmer ist ___ (on the left).", "a": "links"},
                {"q": "Die Küche ist ___ (on the right).", "a": "rechts"},
                {"q": "Das Schlafzimmer ist ___ (upstairs).", "a": "oben"},
                {"q": "Der Tisch steht ___ (next to) dem Bett.", "a": "neben"},
                {"q": "Gehen Sie ___ (straight ahead).", "a": "geradeaus"}
            ],
            "quiz": [
                {"question": "What is 'links'?", "answer": "on the left", "options": ["on the right", "on the left", "straight ahead", "upstairs"]},
                {"question": "What is 'geradeaus'?", "answer": "straight ahead", "options": ["downstairs", "between", "straight ahead", "next to"]},
                {"question": "Translate: 'The bedroom is upstairs.'", "answer": "Das Schlafzimmer ist oben.", "options": ["Das Schlafzimmer ist unten.", "Das Schlafzimmer ist oben.", "Das Schlafzimmer ist links.", "Das Schlafzimmer ist rechts."]},
                {"question": "Which preposition means 'between'?", "answer": "zwischen", "options": ["neben", "gegenüber", "zwischen", "auf"]}
            ],
            "checkpoints": [
                "I know directions: links, rechts, geradeaus",
                "I know position words: oben, unten",
                "I know prepositions: neben, zwischen, gegenüber",
                "I can give basic directions inside a house"
            ],
            "tomorrow": "Apartment hunting dialogue and vocabulary!"
        },
        {
            "dayNum": 20, "title": "Apartment Hunting & Rental Terms",
            "vocab": [
                {"word": "die Miete", "article": "die", "badge": "noun", "translation": "the rent", "ipa": "/ˈmiːtə/", "ex": "Wie hoch ist die Miete?", "exEn": "How high is the rent?"},
                {"word": "der Quadratmeter", "article": "der", "badge": "noun", "translation": "the square metre", "ipa": "/kvaˈdʁaːtˌmeːtɐ/", "ex": "Die Wohnung hat 60 Quadratmeter.", "exEn": "The apartment has 60 square metres."},
                {"word": "die Adresse", "article": "die", "badge": "noun", "translation": "the address", "ipa": "/aˈdʁɛsə/", "ex": "Was ist Ihre Adresse?", "exEn": "What is your address?"},
                {"word": "das Erdgeschoss", "article": "das", "badge": "noun", "translation": "the ground floor", "ipa": "/ˈeːɐtɡəˌʃɔs/", "ex": "Die Wohnung ist im Erdgeschoss.", "exEn": "The apartment is on the ground floor."},
                {"word": "die Etage", "article": "die", "badge": "noun", "translation": "the floor / storey", "ipa": "/eˈtaːʒə/", "ex": "Sie wohnt in der 2. Etage.", "exEn": "She lives on the 2nd floor."},
                {"word": "der Aufzug", "article": "der", "badge": "noun", "translation": "the lift / elevator", "ipa": "/ˈaʊftsuːk/", "ex": "Gibt es einen Aufzug?", "exEn": "Is there an elevator?"},
                {"word": "möbliert", "article": "", "badge": "adj", "translation": "furnished", "ipa": "/møˈbliːɐt/", "ex": "Die Wohnung ist möbliert.", "exEn": "The apartment is furnished."},
                {"word": "frei", "article": "", "badge": "adj", "translation": "vacant / available", "ipa": "/fʁaɪ/", "ex": "Wann ist die Wohnung frei?", "exEn": "When is the apartment available?"}
            ],
            "grammarTitle": "Apartment Inquiries & Key Phrases",
            "grammarContent": """
### Key Questions for Apartment Hunting

| Question | Meaning | Sample Answer |
|:---|:---|:---|
| **Wie groß ist die Wohnung?** | How big is the apartment? | Sie hat 75 Quadratmeter. |
| **Wie hoch ist die Miete?** | How high is the rent? | Die Miete ist 800 Euro. |
| **Wie viele Zimmer gibt es?** | How many rooms are there? | Es gibt drei Zimmer. |
| **Gibt es einen Balkon?** | Is there a balcony? | Ja, es gibt einen Balkon. |
| **Wann ist sie frei?** | When is it vacant? | Ab 1. Oktober. |
| **Ist die Wohnung möbliert?** | Is the apartment furnished? | Ja, sie ist komplett möbliert. |
""",
            "fillIns": [
                {"q": "Wie hoch ist die ___ (rent)?", "a": "Miete"},
                {"q": "Die Wohnung hat 50 ___ (square metres).", "a": "Quadratmeter"},
                {"q": "Ist die Wohnung ___ (furnished)?", "a": "möbliert"},
                {"q": "Gibt es einen ___ (lift)?", "a": "Aufzug"},
                {"q": "Wann ist das Zimmer ___ (vacant)?", "a": "frei"}
            ],
            "quiz": [
                {"question": "How do you ask 'How high is the rent?'", "answer": "Wie hoch ist die Miete?", "options": ["Wie viel ist die Miete?", "Wie hoch ist die Miete?", "Was kostet der Haus?", "Wie groß ist die Miete?"]},
                {"question": "What is 'Erdgeschoss'?", "answer": "ground floor", "options": ["attic", "basement", "ground floor", "balcony"]},
                {"question": "What does 'möbliert' mean?", "answer": "furnished", "options": ["empty", "furnished", "renovated", "expensive"]},
                {"question": "Translate: 'The apartment has 60 square metres.'", "answer": "Die Wohnung hat 60 Quadratmeter.", "options": ["Die Wohnung ist 60 Quadratmeter.", "Die Wohnung hat 60 Quadratmeter.", "Die Miete ist 60 Quadratmeter.", "Das Haus hat 60 Meter."]}
            ],
            "checkpoints": [
                "I know key apartment hunting terms (Miete, Quadratmeter, Aufzug)",
                "I can ask how big an apartment is and what the rent costs",
                "I know floor terms (Erdgeschoss, 1. Etage)",
                "I can read a basic German apartment listing"
            ],
            "tomorrow": "Week 3 Review and Speaking Practice!"
        },
        {
            "dayNum": 21, "isReview": True, "title": "Week 3 Review & Speaking Practice",
            "reviewCards": [
                {"german": "die Wohnung", "english": "apartment", "example": "Ich suche eine Wohnung."},
                {"german": "das Zimmer", "english": "room", "example": "Die Wohnung hat drei Zimmer."},
                {"german": "die Küche", "english": "kitchen", "example": "Die Küche ist hell."},
                {"german": "der Tisch", "english": "table", "example": "Der Tisch ist aus Holz."},
                {"german": "das Bett", "english": "bed", "example": "Das Bett ist groß."},
                {"german": "der Schrank", "english": "wardrobe", "example": "Ich brauche einen Schrank."},
                {"german": "groß / klein", "english": "big / small", "example": "Das Bad ist klein."},
                {"german": "hell / dunkel", "english": "bright / dark", "example": "Das Zimmer ist hell."},
                {"german": "gemütlich", "english": "cosy", "example": "Das Sofa ist gemütlich."},
                {"german": "links / rechts", "english": "left / right", "example": "Das Bad ist links."},
                {"german": "oben / unten", "english": "upstairs / downstairs", "example": "Das Schlafzimmer ist oben."},
                {"german": "die Miete", "english": "rent", "example": "Die Miete ist 600 Euro."},
                {"german": "möbliert", "english": "furnished", "example": "Die Wohnung ist möbliert."},
                {"german": "es gibt", "english": "there is / are", "example": "Es gibt einen Balkon."},
                {"german": "die Bücher (pl)", "english": "books", "example": "Die Bücher stehen im Regal."}
            ],
            "grammarSummary": """
### Week 3 Master Summary

1. **es gibt + Accusative:** *Es gibt einen Balkon (m) / eine Küche (f) / ein Bad (n).*
2. **haben + Accusative:** Only masculine changes! *der Tisch → den/einen/keinen Tisch.*
3. **Plural Patterns:** 
   - No change (das Fenster → die Fenster)
   - Add -e (der Tisch → die Tische)
   - Add -er + Umlaut (das Buch → die Bücher)
   - Add -(e)n (die Tür → die Türen)
   - Add -s (das Sofa → die Sofas)
4. **Adjectives after sein:** NO ENDINGS! *Das Zimmer ist groß / hell / gemütlich.*
5. **Location Adverbs:** *links, rechts, geradeaus, oben, unten.*
""",
            "quiz": [
                {"question": "Which form follows 'es gibt' for masculine nouns?", "answer": "einen", "options": ["ein", "einen", "eine", "einem"]},
                {"question": "What is the plural of 'das Buch'?", "answer": "die Bücher", "options": ["die Buche", "die Bücher", "die Büchern", "die Buchs"]},
                {"question": "Do adjectives take endings after 'ist'?", "answer": "no, never", "options": ["yes, -e", "yes, -en", "no, never", "only for feminine"]},
                {"question": "Translate: 'The bathroom is upstairs on the left.'", "answer": "Das Bad ist oben links.", "options": ["Das Bad ist unten rechts.", "Das Bad ist oben links.", "Das Bad ist geradeaus unten.", "Das Bad ist neben rechts."]},
                {"question": "What is 'die Miete'?", "answer": "the rent", "options": ["the apartment", "the rent", "the furniture", "the key"]},
                {"question": "Accusative of 'der Schrank' after haben:", "answer": "einen Schrank", "options": ["ein Schrank", "einen Schrank", "eine Schrank", "dem Schrank"]},
                {"question": "What does 'gemütlich' mean?", "answer": "cosy / comfortable", "options": ["noisy", "expensive", "cosy / comfortable", "dark"]},
                {"question": "What is 'Erdgeschoss'?", "answer": "ground floor", "options": ["attic", "basement", "ground floor", "balcony"]}
            ],
            "speakingPrompt": """
### Speaking Exercise — Describe Your Home

Read this script aloud and record yourself or practice with a partner:

> *"Ich wohne in [einer Wohnung / einem Haus] in [City]. Meine Wohnung hat [Number] Zimmer. Es gibt ein Wohnzimmer, ein Schlafzimmer, eine Küche und ein Bad. Mein Lieblingszimmer ist das [Wohnzimmer]. Es ist [groß / hell / gemütlich]. Im Wohnzimmer gibt es ein Sofa, einen Tisch und ein Regal. Die Miete ist [Amount] Euro."*
""",
            "checkpoints": [
                "I can name 8 rooms and 8 furniture items",
                "I can use 'es gibt' with correct accusative articles",
                "I can describe a room using 5 adjectives",
                "I can give a 1-minute spoken description of my home"
            ]
        }
    ]
})

print("Week 3 data populated.")
