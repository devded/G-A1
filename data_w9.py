# Week 9 Data

w9 = {
    "weekNum": 9,
    "title": "City, Transport & Directions",
    "level": "A1.2",
    "goal": "Name city places, ask for and give directions, understand basic Dative location contractions (im, am, beim, zum, zur), and navigate public transport.",
    "days": [
        {
            "dayNum": 57, "title": "City Places & 'es gibt' in the City",
            "vocab": [
                {"word": "der Bahnhof", "article": "der", "badge": "noun", "translation": "the train station", "ipa": "/ˈbaːnˌhoːf/", "ex": "Der Bahnhof ist sehr groß.", "exEn": "The train station is very big."},
                {"word": "die Post", "article": "die", "badge": "noun", "translation": "the post office", "ipa": "/pɔst/", "ex": "Wo ist die Post?", "exEn": "Where is the post office?"},
                {"word": "die Bank", "article": "die", "badge": "noun", "translation": "the bank", "ipa": "/baŋk/", "ex": "Die Bank ist geschlossen.", "exEn": "The bank is closed."},
                {"word": "das Krankenhaus", "article": "das", "badge": "noun", "translation": "the hospital", "ipa": "/ˈkʁaŋkənˌhaʊs/", "ex": "Er ist im Krankenhaus.", "exEn": "He is in the hospital."},
                {"word": "die Apotheke", "article": "die", "badge": "noun", "translation": "the pharmacy", "ipa": "/apoˈteːkə/", "ex": "Die Apotheke ist in der Nähe.", "exEn": "The pharmacy is nearby."},
                {"word": "das Rathaus", "article": "das", "badge": "noun", "translation": "the town hall", "ipa": "/ˈʁaːtˌhaʊs/", "ex": "Das Rathaus steht am Markt.", "exEn": "The town hall stands at the market."},
                {"word": "der Supermarkt", "article": "der", "badge": "noun", "translation": "the supermarket", "ipa": "/ˈzuːpɐˌmaʁkt/", "ex": "Ich gehe in den Supermarkt.", "exEn": "I go to the supermarket."},
                {"word": "das Museum", "article": "das", "badge": "noun", "translation": "the museum", "ipa": "/muˈzeːʊm/", "ex": "Das Museum ist interessant.", "exEn": "The museum is interesting."}
            ],
            "grammarTitle": "City Vocabulary & Accusative after 'es gibt'",
            "grammarContent": """
### Asking About City Places

• **Wo ist [Definite Noun]?**  
  - *Wo ist **der** Bahnhof?*  
  - *Wo ist **die** Apotheke?*  
  - *Wo ist **das** Rathaus?*

• **Gibt es hier [Accusative Noun]?**  
  - *Gibt es hier **einen** Supermarkt?* (masculine → einen)  
  - *Gibt es hier **eine** Bank?* (feminine → eine)  
  - *Gibt es hier **ein** Krankenhaus?* (neuter → ein)
""",
            "fillIns": [
                {"q": "Gibt es hier ___ (a, m) Bahnhof?", "a": "einen"},
                {"q": "Gibt es hier ___ (a, f) Apotheke?", "a": "eine"},
                {"q": "Wo ist ___ (the, n) Krankenhaus?", "a": "das"},
                {"q": "Er arbeitet auf der ___ (post office).", "a": "Post"},
                {"q": "Das ___ (town hall) ist im Zentrum.", "a": "Rathaus"}
            ],
            "quiz": [
                {"question": "What is 'der Bahnhof'?", "answer": "the train station", "options": ["the bus stop", "the train station", "the airport", "the city hall"]},
                {"question": "How do you ask 'Is there a pharmacy here?'", "answer": "Gibt es hier eine Apotheke?", "options": ["Ist hier der Apotheke?", "Gibt es hier eine Apotheke?", "Hat hier ein Apotheke?", "Wo wohnt eine Apotheke?"]},
                {"question": "What is the article for 'Krankenhaus'?", "answer": "das", "options": ["der", "die", "das", "den"]},
                {"question": "Accusative form of 'der Supermarkt' after 'es gibt':", "answer": "einen Supermarkt", "options": ["ein Supermarkt", "einen Supermarkt", "eine Supermarkt", "dem Supermarkt"]}
            ],
            "checkpoints": [
                "I know 8 essential city place nouns with correct articles",
                "I can ask 'Wo ist der/die/das...?'",
                "I can ask 'Gibt es hier einen/eine/ein...?'",
                "I can name places in my own town"
            ],
            "tomorrow": "Asking for and giving directions (geradeaus, links, rechts)!"
        },
        {
            "dayNum": 58, "title": "Asking for & Giving Directions",
            "vocab": [
                {"word": "geradeaus", "article": "", "badge": "phrase", "translation": "straight ahead", "ipa": "/ɡəˈʁaːdəˈaʊs/", "ex": "Gehen Sie immer geradeaus.", "exEn": "Go straight ahead."},
                {"word": "links abbiegen", "article": "", "badge": "phrase", "translation": "turn left", "ipa": "/lɪŋks ˈapˌbiːɡən/", "ex": "Biegen Sie links ab.", "exEn": "Turn left."},
                {"word": "rechts abbiegen", "article": "", "badge": "phrase", "translation": "turn right", "ipa": "/ʁɛçts ˈapˌbiːɡən/", "ex": "Biegen Sie an der Ampel rechts ab.", "exEn": "Turn right at the traffic lights."},
                {"word": "die Kreuzung", "article": "die", "badge": "noun", "translation": "the junction / intersection", "ipa": "/ˈkʁɔʏtsʊŋ/", "ex": "An der Kreuzung geradeaus.", "exEn": "Straight ahead at the junction."},
                {"word": "die Straße", "article": "die", "badge": "noun", "translation": "the street / road", "ipa": "/ˈʃtʁaːsə/", "ex": "Nehmen Sie die erste Straße links.", "exEn": "Take the first street on the left."},
                {"word": "die Ampel", "article": "die", "badge": "noun", "translation": "the traffic lights", "ipa": "/ˈampl̩/", "ex": "An der Ampel rechts.", "exEn": "Right at the traffic lights."},
                {"word": "wie weit", "article": "", "badge": "phrase", "translation": "how far", "ipa": "/viː vaɪt/", "ex": "Wie weit ist es zum Bahnhof?", "exEn": "How far is it to the station?"},
                {"word": "zu Fuß", "article": "", "badge": "phrase", "translation": "on foot / walking", "ipa": "/tsuː fuːs/", "ex": "Das ist 5 Minuten zu Fuß.", "exEn": "That is 5 minutes on foot."}
            ],
            "grammarTitle": "Asking & Giving Directions (Imperative & Imperative Polite)",
            "grammarContent": """
### Asking for Directions

• **Entschuldigung, wie komme ich zum Bahnhof / zur Apotheke?**  
  *(Excuse me, how do I get to the train station / pharmacy?)*  
• **Wo ist der/die/das [Place], bitte?**  
• **Wie weit ist es zu Fuß?** *(How far is it on foot?)*

### Giving Directions (Polite Formal: Sie)

| Command | Meaning |
|:---|:---|
| **Gehen Sie geradeaus.** | Walk straight ahead. |
| **Biegen Sie links / rechts ab.** | Turn left / right. |
| **Nehmen Sie die erste / zweite Straße links.** | Take the 1st / 2nd street on the left. |
| **An der Ampel / Kreuzung...** | At the traffic lights / junction... |
| **Es ist auf der linken / rechten Seite.** | It is on the left / right side. |
""",
            "fillIns": [
                {"q": "Gehen Sie immer ___ (straight ahead).", "a": "geradeaus"},
                {"q": "Biegen Sie an der Ampel ___ (left) ab.", "a": "links"},
                {"q": "Nehmen Sie die erste ___ (street) rechts.", "a": "Straße"},
                {"q": "Das ist nur 10 Minuten ___ (on foot).", "a": "zu Fuß"},
                {"q": "An der ___ (traffic lights) biegen Sie ab.", "a": "Ampel"}
            ],
            "quiz": [
                {"question": "How do you say 'Turn right' politely?", "answer": "Biegen Sie rechts ab.", "options": ["Gehen Sie rechts.", "Biegen Sie rechts ab.", "Drehen Sie rechts.", "Laufen Sie rechts."]},
                {"question": "What is 'die Ampel'?", "answer": "the traffic lights", "options": ["the lamp", "the junction", "the traffic lights", "the street"]},
                {"question": "How do you ask 'How do I get to the train station?'", "answer": "Wie komme ich zum Bahnhof?", "options": ["Wo fährt der Bahnhof?", "Wie komme ich zum Bahnhof?", "Was ist der Bahnhof?", "Wie weit kommt der Bahnhof?"]},
                {"question": "Translate: 'That is 5 minutes on foot.'", "answer": "Das ist 5 Minuten zu Fuß.", "options": ["Das ist 5 Minuten mit Fuß.", "Das ist 5 Minuten zu Fuß.", "Das ist 5 Minuten per Fuß.", "Das ist 5 Minuten an Fuß."]}
            ],
            "checkpoints": [
                "I can ask for directions politely using 'Wie komme ich zum/zur...?'",
                "I can give directions using geradeaus, links, rechts abbiegen",
                "I know key traffic terms: Ampel, Kreuzung, Straße",
                "I know the expression 'zu Fuß'"
            ],
            "tomorrow": "Basic Dative location contractions (im, am, beim, zum, zur)!"
        },
        {
            "dayNum": 59, "title": "Basic Dative Case Location Contractions",
            "vocab": [
                {"word": "im", "article": "", "badge": "prep", "translation": "in the (in + dem)", "ipa": "/ɪm/", "ex": "Er ist im Supermarkt.", "exEn": "He is in the supermarket."},
                {"word": "am", "article": "", "badge": "prep", "translation": "at/on the (an + dem)", "ipa": "/am/", "ex": "Das Rathaus ist am Markt.", "exEn": "The town hall is at the market."},
                {"word": "beim", "article": "", "badge": "prep", "translation": "at the / near (bei + dem)", "ipa": "/baɪm/", "ex": "Ich bin beim Arzt.", "exEn": "I am at the doctor's."},
                {"word": "vom", "article": "", "badge": "prep", "translation": "from the (von + dem)", "ipa": "/fɔm/", "ex": "Ich komme vom Bahnhof.", "exEn": "I am coming from the station."},
                {"word": "zum", "article": "", "badge": "prep", "translation": "to the (m/n: zu + dem)", "ipa": "/tsʊm/", "ex": "Wie komme ich zum Bahnhof?", "exEn": "How do I get to the station?"},
                {"word": "zur", "article": "", "badge": "prep", "translation": "to the (f: zu + der)", "ipa": "/tsuːɐ̯/", "ex": "Wie komme ich zur Apotheke?", "exEn": "How do I get to the pharmacy?"},
                {"word": "gegenüber von", "article": "", "badge": "prep", "translation": "opposite to", "ipa": "/ˈɡeːɡənˌyːbɐ fɔn/", "ex": "Die Bank ist gegenüber vom Bahnhof.", "exEn": "The bank is opposite the station."},
                {"word": "in der Nähe von", "article": "", "badge": "phrase", "translation": "in the vicinity / near to", "ipa": "/ɪn dɛːɐ̯ ˈnɛːə fɔn/", "ex": "Die Post ist in der Nähe vom Markt.", "exEn": "The post office is near the market."}
            ],
            "grammarTitle": "The Dative Case: Location Contractions",
            "grammarContent": """
### The Dative Case Changes Noun Articles!

Dative is used for **location (Wo?)** and after direction prepositions like **zu**!

| Gender | Nominative | Dative | Contraction Formula |
|:---:|:---:|:---:|:---|
| **Masculine** | der | **dem** | in + dem = **im** / bei + dem = **beim** / zu + dem = **zum** |
| **Neuter** | das | **dem** | in + dem = **im** / zu + dem = **zum** |
| **Feminine** | die | **der** | zu + der = **zur** / in + der = **in der** |

> <Icon name="target" /> **Master Rule for 'to the' (direction):**  
> • Masculine / Neuter: **zum** (*zum Bahnhof*, *zum Krankenhaus*)  
> • Feminine: **zur** (*zur Apotheke*, *zur Bank*, *zur Post*)
""",
            "fillIns": [
                {"q": "Wie komme ich ___ (to the, m) Bahnhof?", "a": "zum"},
                {"q": "Wie komme ich ___ (to the, f) Apotheke?", "a": "zur"},
                {"q": "Ich bin ___ (at the, m) Arzt.", "a": "beim"},
                {"q": "Er ist ___ (in the, n) Krankenhaus.", "a": "im"},
                {"q": "Die Post ist ___ (opposite) der Bank.", "a": "gegenüber von"}
            ],
            "quiz": [
                {"question": "Which contraction is used for 'to the' with masculine/neuter nouns (zu + dem)?", "answer": "zum", "options": ["zur", "zum", "im", "beim"]},
                {"question": "Which contraction is used for 'to the' with feminine nouns (zu + der)?", "answer": "zur", "options": ["zur", "zum", "im", "beim"]},
                {"question": "What is the contraction 'im' made of?", "answer": "in + dem", "options": ["in + das", "in + dem", "im + dem", "in + der"]},
                {"question": "Translate: 'I am at the doctor's' (der Arzt)", "answer": "Ich bin beim Arzt.", "options": ["Ich bin zum Arzt.", "Ich bin beim Arzt.", "Ich bin im Arzt.", "Ich bin am Arzt."]}
            ],
            "checkpoints": [
                "I know the Dative article changes (der/das → dem, die → der)",
                "I know contractions: im, am, beim, vom, zum, zur",
                "I know to use zum for masculine/neuter and zur for feminine destination",
                "I can ask directions to any city place using zum/zur"
            ],
            "tomorrow": "Public transport vocabulary & buying tickets!"
        },
        {
            "dayNum": 60, "title": "Public Transport Vocabulary & Verbs",
            "vocab": [
                {"word": "der Bus", "article": "der", "badge": "noun", "translation": "the bus", "ipa": "/bʊs/", "ex": "Der Bus kommt um 8 Uhr.", "exEn": "The bus comes at 8 o'clock."},
                {"word": "die U-Bahn", "article": "die", "badge": "noun", "translation": "the underground / metro", "ipa": "/ˈuːˌbaːn/", "ex": "Ich fahre mit der U-Bahn.", "exEn": "I go by metro."},
                {"word": "die S-Bahn", "article": "die", "badge": "noun", "translation": "suburban train", "ipa": "/ˈɛsˌbaːn/", "ex": "Die S-Bahn ist schnell.", "exEn": "The suburban train is fast."},
                {"word": "der Zug", "article": "der", "badge": "noun", "translation": "the train", "ipa": "/tsuːk/", "ex": "Der Zug nach München fährt ab.", "exEn": "The train to Munich leaves."},
                {"word": "das Ticket", "article": "das", "badge": "noun", "translation": "the ticket", "ipa": "/ˈtɪkət/", "ex": "Ich kaufe ein Ticket.", "exEn": "I buy a ticket."},
                {"word": "einsteigen", "article": "", "badge": "verb", "translation": "to board / get on", "ipa": "/ˈaɪnˌʃtaɪɡən/", "ex": "Bitte alle einsteigen!", "exEn": "All aboard please!"},
                {"word": "aussteigen", "article": "", "badge": "verb", "translation": "to get off / alight", "ipa": "/ˈaʊsˌʃtaɪɡən/", "ex": "Wir steigen am Hauptbahnhof aus.", "exEn": "We get off at the central station."},
                {"word": "umsteigen", "article": "", "badge": "verb", "translation": "to change / transfer trains", "ipa": "/ˈʊmˌʃtaɪɡən/", "ex": "Müssen wir umsteigen?", "exEn": "Do we have to change trains?"}
            ],
            "grammarTitle": "Transport Verbs & Preposition 'mit' + Dative",
            "grammarContent": """
### 3 Core Transport Movement Verbs (All Separable!)

1. **einsteigen** = to get on / board  
   • *Ich **steige** in den Bus **ein**.*
2. **aussteigen** = to get off / alight  
   • *Wir **steigen** an der Haltestelle **aus**.*
3. **umsteigen** = to change / transfer lines  
   • *Sie müssen am Marienplatz **umsteigen**.*

### Preposition **mit** (by transport) + Dative!

Always use **mit + Dative** when stating how you travel:

• **mit dem** Bus (masculine)  
• **mit dem** Zug (masculine)  
• **mit dem** Auto (neuter)  
• **mit der** U-Bahn / S-Bahn / Straßenbahn (feminine)
""",
            "fillIns": [
                {"q": "Ich fahre mit ___ (the, f) U-Bahn.", "a": "der"},
                {"q": "Er fährt mit ___ (the, m) Bus.", "a": "dem"},
                {"q": "Wir müssen am Marienplatz ___ (change trains).", "a": "umsteigen"},
                {"q": "Wo steigen wir ___ (get off)?", "a": "aus"},
                {"q": "Bitte alle ___ (board/get on)!", "a": "einsteigen"}
            ],
            "quiz": [
                {"question": "Which preposition means 'by' transport (e.g. by bus)?", "answer": "mit (+ Dative)", "options": ["von", "mit (+ Dative)", "bei", "in"]},
                {"question": "How do you say 'by metro' (die U-Bahn)?", "answer": "mit der U-Bahn", "options": ["mit die U-Bahn", "mit der U-Bahn", "mit dem U-Bahn", "in die U-Bahn"]},
                {"question": "What is 'umsteigen'?", "answer": "to change / transfer trains", "options": ["to get on", "to get off", "to change / transfer trains", "to drive fast"]},
                {"question": "Translate: 'We get off at the central station.'", "answer": "Wir steigen am Hauptbahnhof aus.", "options": ["Wir steigen am Hauptbahnhof ein.", "Wir steigen am Hauptbahnhof aus.", "Wir umsteigen am Hauptbahnhof.", "Wir fahren am Hauptbahnhof."]}
            ],
            "checkpoints": [
                "I know transport types: Bus, U-Bahn, S-Bahn, Zug",
                "I know the 3 transport verbs: einsteigen, aussteigen, umsteigen",
                "I know to use mit + Dative (mit dem Bus, mit der U-Bahn)",
                "I can ask if I need to change trains"
            ],
            "tomorrow": "Timetables, platforms, and buying tickets at an automaton!"
        },
        {
            "dayNum": 61, "title": "Timetables, Platforms & Buying Tickets",
            "vocab": [
                {"word": "die Abfahrt", "article": "die", "badge": "noun", "translation": "the departure", "ipa": "/ˈapˌfaːɐ̯t/", "ex": "Wann ist die Abfahrt?", "exEn": "When is the departure?"},
                {"word": "die Ankunft", "article": "die", "badge": "noun", "translation": "the arrival", "ipa": "/ˈanˌkʊnft/", "ex": "Die Ankunft ist um 14:15 Uhr.", "exEn": "The arrival is at 14:15."},
                {"word": "der Gleis", "article": "der", "badge": "noun", "translation": "the platform / track (pl: Gleise)", "ipa": "/ɡlaɪs/", "ex": "Der Zug fährt von Gleis 4 ab.", "exEn": "The train leaves from platform 4."},
                {"word": "die Verspätung", "article": "die", "badge": "noun", "translation": "the delay", "ipa": "/fɛɐ̯ˈʃpɛːtʊŋ/", "ex": "Der Zug hat 10 Minuten Verspätung.", "exEn": "The train has a 10 minute delay."},
                {"word": "einfach", "article": "", "badge": "phrase", "translation": "one-way (ticket)", "ipa": "/ˈaɪnfax/", "ex": "Ein Ticket einfach, bitte.", "exEn": "A one-way ticket, please."},
                {"word": "hin und zurück", "article": "", "badge": "phrase", "translation": "return / round-trip", "ipa": "/hɪn ʊnt tsuˈʁʏk/", "ex": "Ein Ticket hin und zurück, bitte.", "exEn": "A return ticket, please."},
                {"word": "der Fahrkartenautomat", "article": "der", "badge": "noun", "translation": "ticket machine", "ipa": "/ˈfaːɐ̯kaʁtən_aʊtomaːt/", "ex": "Kaufe die Karte am Automat.", "exEn": "Buy the ticket at the machine."},
                {"word": "entwerten", "article": "", "badge": "verb", "translation": "to validate / stamp ticket", "ipa": "/ɛntˈveːʁtən/", "ex": "Sie müssen die Fahrkarte entwerten.", "exEn": "You must validate your ticket."}
            ],
            "grammarTitle": "Buying Train Tickets & Reading Timetables",
            "grammarContent": """
### At the Ticket Counter / Machine

• **Eine Fahrkarte nach München, bitte.**  
  *(A train ticket to Munich, please.)*  
• **Einfach oder hin und zurück?**  
  - *Einfach, bitte.* (One-way, please.)  
  - *Hin und zurück, bitte.* (Return / round-trip, please.)  
• **Mit oder ohne Sitzplatzreservierung?**  
  *(With or without seat reservation?)*

### Railway Station Announcements & Signs

• **Abfahrt:** 10:15 Uhr — **Gleis 3**  
• **Der ICE nach Frankfurt hat ca. 15 Minuten Verspätung.**  
• **Bitte die Fahrkarten vor Fahrtantritt entwerten!**
""",
            "fillIns": [
                {"q": "Eine Fahrkarte nach Berlin, ___ (one-way), bitte.", "a": "einfach"},
                {"q": "Ich möchte ein Ticket ___ (return).", "a": "hin und zurück"},
                {"q": "Der Zug fährt von ___ (platform) 7 ab.", "a": "Gleis"},
                {"q": "Der ICE hat 20 Minuten ___ (delay).", "a": "Verspätung"},
                {"q": "Wann ist die ___ (departure)?", "a": "Abfahrt"}
            ],
            "quiz": [
                {"question": "What is 'hin und zurück'?", "answer": "return / round-trip", "options": ["one-way", "return / round-trip", "first class", "discounted"]},
                {"question": "What does 'der Gleis' mean?", "answer": "the platform / track", "options": ["the train", "the ticket", "the platform / track", "the station master"]},
                {"question": "What does 'Verspätung' mean?", "answer": "delay", "options": ["on time", "cancellation", "delay", "arrival"]},
                {"question": "Translate: 'Ein Ticket nach Hamburg einfach, bitte.'", "answer": "A one-way ticket to Hamburg, please.", "options": ["A return ticket to Hamburg, please.", "A one-way ticket to Hamburg, please.", "A first class ticket to Hamburg.", "A cheap ticket to Hamburg."]}
            ],
            "checkpoints": [
                "I know station terms: Abfahrt, Ankunft, Gleis, Verspätung",
                "I know ticket terms: einfach, hin und zurück, Fahrkartenautomat",
                "I know to stamp/validate tickets (entwerten)",
                "I can buy a train ticket at a counter or machine"
            ],
            "tomorrow": "Full city navigation & transport dialogue!"
        },
        {
            "dayNum": 62, "title": "Getting Around & Navigation Dialogue",
            "vocab": [
                {"word": "das Ziel", "article": "das", "badge": "noun", "translation": "the destination / goal", "ipa": "/tsiːl/", "ex": "Sie haben Ihr Ziel erreicht.", "exEn": "You have reached your destination."},
                {"word": "verloren", "article": "", "badge": "adj", "translation": "lost", "ipa": "/fɛɐ̯ˈloːʁən/", "ex": "Ich bin verloren! Wo bin ich?", "exEn": "I am lost! Where am I?"},
                {"word": "die Karte", "article": "die", "badge": "noun", "translation": "the map / card", "ipa": "/ˈkaʁtə/", "ex": "Haben Sie einen Stadtplan?", "exEn": "Do you have a city map?"},
                {"word": "ausgerechnet", "article": "", "badge": "phrase", "translation": "of all things / just", "ipa": "/ˈaʊsɡəˌʁɛçnət/", "ex": "Ausgerechnet heute regnet es.", "exEn": "Of all days it is raining today."},
                {"word": "bestimmt", "article": "", "badge": "phrase", "translation": "certainly / definitely", "ipa": "/bəˈʃtɪmt/", "ex": "Das ist bestimmt richtig.", "exEn": "That is definitely correct."},
                {"word": "der Ausgang", "article": "der", "badge": "noun", "translation": "the exit", "ipa": "/ˈaʊsˌɡaŋ/", "ex": "Wo ist der Ausgang?", "exEn": "Where is the exit?"},
                {"word": "der Eingang", "article": "der", "badge": "noun", "translation": "the entrance", "ipa": "/ˈaɪnˌɡaŋ/", "ex": "Der Eingang ist um die Ecke.", "exEn": "The entrance is around the corner."},
                {"word": "um die Ecke", "article": "", "badge": "phrase", "translation": "around the corner", "ipa": "/ʊm diː ˈɛkə/", "ex": "Die Apotheke ist um die Ecke.", "exEn": "The pharmacy is around the corner."}
            ],
            "grammarTitle": "Navigation & Getting Around Conversation",
            "grammarContent": """
### Full Navigation Script

> **Tourist:** *Entschuldigung! Ich bin verloren. Wie komme ich zum Goethe-Institut?*  
> **Passant (Passerby):** *Kein Problem! Das ist gar nicht weit von hier.*  
> **Tourist:** *Kann ich zu Fuß gehen oder muss ich mit der U-Bahn fahren?*  
> **Passant:** *Sie können zu Fuß gehen. Das dauert nur etwa 10 Minuten.*  
> **Tourist:** *Wie ist der Weg?*  
> **Passant:** *Gehen Sie hier die Straße geradeaus bis zur nächsten Kreuzung. Dann biegen Sie rechts ab. Das Goethe-Institut ist auf der linken Seite, direkt gegenüber von der Bank.*  
> **Tourist:** *Super, vielen Dank für die Hilfe!*  
> **Passant:** *Gerne! Schönen Tag noch!*
""",
            "fillIns": [
                {"q": "Ich bin ___ (lost)! Wo ist das Zentrum?", "a": "verloren"},
                {"q": "Wo ist der ___ (exit)?", "a": "Ausgang"},
                {"q": "Der ___ (entrance) ist vorne.", "a": "Eingang"},
                {"q": "Die Post ist gleich ___ (around the corner).", "a": "um die Ecke"},
                {"q": "Sie haben Ihr ___ (destination) erreicht.", "a": "Ziel"}
            ],
            "quiz": [
                {"question": "What is 'der Ausgang'?", "answer": "the exit", "options": ["the entrance", "the exit", "the elevator", "the staircase"]},
                {"question": "What is 'der Eingang'?", "answer": "the entrance", "options": ["the exit", "the entrance", "the hallway", "the door"]},
                {"question": "What does 'um die Ecke' mean?", "answer": "around the corner", "options": ["straight ahead", "around the corner", "across the street", "far away"]},
                {"question": "Translate: 'I am lost!'", "answer": "Ich bin verloren!", "options": ["Ich bin müde!", "Ich bin verloren!", "Ich bin krank!", "Ich bin pünktlich!"]}
            ],
            "checkpoints": [
                "I can ask for help when lost (Ich bin verloren!)",
                "I know navigation landmarks: Ausgang, Eingang, um die Ecke, Ziel",
                "I can follow multi-step spoken directions",
                "I can ask whether to walk or take public transport"
            ],
            "tomorrow": "Week 9 Review and Speaking Practice!"
        },
        {
            "dayNum": 63, "isReview": True, "title": "Week 9 Review & Speaking Practice",
            "reviewCards": [
                {"german": "der Bahnhof", "english": "train station", "example": "Wie komme ich zum Bahnhof?"},
                {"german": "die Apotheke", "english": "pharmacy", "example": "Die Apotheke ist gegenüber."},
                {"german": "geradeaus", "english": "straight ahead", "example": "Gehen Sie geradeaus."},
                {"german": "links / rechts abbiegen", "english": "turn left / right", "example": "Biegen Sie links ab."},
                {"german": "die Ampel / Kreuzung", "english": "traffic lights / junction", "example": "An der Ampel rechts."},
                {"german": "zu Fuß", "english": "on foot", "example": "Das ist 5 Minuten zu Fuß."},
                {"german": "zum (m/n) / zur (f)", "english": "to the (Dative destination)", "example": "zum Bahnhof / zur Post"},
                {"german": "im / am / beim", "english": "in / at / near the", "example": "im Supermarkt, beim Arzt"},
                {"german": "mit dem / mit der", "english": "by (transport + Dative)", "example": "mit dem Bus / mit der U-Bahn"},
                {"german": "einsteigen / aussteigen", "english": "get on / get off", "example": "Wir steigen am Hbf aus."},
                {"german": "umsteigen", "english": "change trains", "example": "Müssen wir umsteigen?"},
                {"german": "einfach / hin und zurück", "english": "one-way / return ticket", "example": "Ein Ticket hin und zurück."},
                {"german": "der Gleis / Verspätung", "english": "platform / delay", "example": "Gleis 4, 10 Min Verspätung."},
                {"german": "der Ausgang / Eingang", "english": "exit / entrance", "example": "Wo ist der Ausgang?"},
                {"german": "um die Ecke", "english": "around the corner", "example": "Die Bank ist um die Ecke."}
            ],
            "grammarSummary": """
### Week 9 Master Summary

1. **Asking & Giving Directions:**  
   - *Wie komme ich zum Bahnhof / zur Apotheke?*  
   - *Gehen Sie geradeaus. Biegen Sie an der Ampel links ab.*  
   - *Es ist 10 Minuten zu Fuß.*
2. **Dative Location Contractions:**  
   - *zu + dem =* **zum** (masc/neut: *zum Bahnhof, zum Krankenhaus*)  
   - *zu + der =* **zur** (fem: *zur Apotheke, zur Post*)  
   - *in + dem =* **im**, *an + dem =* **am**, *bei + dem =* **beim**.
3. **Transport with 'mit' + Dative:**  
   - *mit dem* Bus / Zug / Auto.  
   - *mit der* U-Bahn / S-Bahn / Straßenbahn.
4. **Transport Verbs:** *einsteigen* (get on), *aussteigen* (get off), *umsteigen* (transfer).
5. **Tickets:** *einfach* (one-way) vs. *hin und zurück* (return).
""",
            "quiz": [
                {"question": "Which contraction means 'to the' for a feminine noun (zu + der)?", "answer": "zur", "options": ["zum", "zur", "im", "beim"]},
                {"question": "Which contraction means 'to the' for a masculine noun (zu + dem)?", "answer": "zum", "options": ["zum", "zur", "im", "am"]},
                {"question": "Translate: 'by metro' (die U-Bahn)", "answer": "mit der U-Bahn", "options": ["mit die U-Bahn", "mit der U-Bahn", "mit dem U-Bahn", "zu der U-Bahn"]},
                {"question": "What is 'umsteigen'?", "answer": "to change trains / lines", "options": ["to get on", "to get off", "to change trains / lines", "to buy a ticket"]},
                {"question": "What is 'hin und zurück'?", "answer": "return ticket", "options": ["one-way ticket", "return ticket", "platform number", "delay"]},
                {"question": "Translate: 'Go straight ahead.'", "answer": "Gehen Sie geradeaus.", "options": ["Gehen Sie links.", "Gehen Sie geradeaus.", "Biegen Sie ab.", "Kommen Sie zurück."]},
                {"question": "What does 'Verspätung' mean?", "answer": "delay", "options": ["on time", "delay", "platform", "cancellation"]},
                {"question": "Where is 'der Ausgang'?", "answer": "the exit", "options": ["the entrance", "the exit", "the corner", "the window"]}
            ],
            "speakingPrompt": """
### Speaking Exercise — Give Directions & Buy a Train Ticket

Read this script aloud and record yourself or practice with a partner:

> *"Entschuldigung! Wie komme ich zum Hauptbahnhof? Ach so, gehen Sie hier die Straße geradeaus, dann an der Ampel rechts abbiegen. Der Bahnhof ist direkt um die Ecke, gegenüber von der Post! ... Am Bahnhof: Guten Tag! Ich möchte eine Fahrkarte nach München, bitte. Hin und zurück. Von welchem Gleis fährt der Zug ab? Gleis 5? Hat der Zug Verspätung? Nein, er ist pünktlich. Vielen Dank!"*
""",
            "checkpoints": [
                "I know 10+ city and transport vocabulary words",
                "I can use zum/zur for destinations accurately",
                "I can use mit + Dative for all modes of transport",
                "I can ask for directions and buy train tickets confidently"
            ]
        }
    ]
}

print("Week 9 data populated.")
