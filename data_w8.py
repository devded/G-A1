# Week 8 Data

w8 = {
    "weekNum": 8,
    "title": "Restaurants & Preferences",
    "level": "A1.2",
    "goal": "Reserve a table, order food and drinks, express food preferences, pay the bill, handle restaurant complaints, and describe basic clothing and colours.",
    "days": [
        {
            "dayNum": 50, "title": "Restaurant Vocabulary & Table Reservations",
            "vocab": [
                {"word": "die Speisekarte", "article": "die", "badge": "noun", "translation": "the menu", "ipa": "/ˈʃpaɪzəˌkaʁtə/", "ex": "Die Speisekarte, bitte!", "exEn": "The menu, please!"},
                {"word": "der Kellner", "article": "der", "badge": "noun", "translation": "the waiter", "ipa": "/ˈkɛlnɐ/", "ex": "Der Kellner ist sehr nett.", "exEn": "The waiter is very nice."},
                {"word": "die Kellnerin", "article": "die", "badge": "noun", "translation": "the waitress", "ipa": "/ˈkɛlnəʁɪn/", "ex": "Die Kellnerin bringt die Karte.", "exEn": "The waitress brings the menu."},
                {"word": "der Tisch", "article": "der", "badge": "noun", "translation": "the table", "ipa": "/tɪʃ/", "ex": "Ein Tisch für zwei Personen.", "exEn": "A table for two people."},
                {"word": "reservieren", "article": "", "badge": "verb", "translation": "to reserve / book", "ipa": "/ʁezɛʁˈviːʁən/", "ex": "Ich möchte einen Tisch reservieren.", "exEn": "I would like to reserve a table."},
                {"word": "der Platz", "article": "der", "badge": "noun", "translation": "the seat / place", "ipa": "/plats/", "ex": "Ist dieser Platz frei?", "exEn": "Is this seat free?"},
                {"word": "das Gericht", "article": "das", "badge": "noun", "translation": "the dish / meal", "ipa": "/ɡəˈʁɪçt/", "ex": "Das Gericht ist sehr lecker.", "exEn": "The dish is very delicious."},
                {"word": "die Portion", "article": "die", "badge": "noun", "translation": "the portion / serving", "ipa": "/pɔʁˈtsi̯oːn/", "ex": "Eine große Portion Pommes.", "exEn": "A large portion of chips."}
            ],
            "grammarTitle": "Reserving a Table & Entering a Restaurant",
            "grammarContent": """
### Key Reservation Formulas

• **Ich möchte einen Tisch für [Number] Personen reservieren.**  
  *(I would like to reserve a table for X people.)*  
• **Für wie viel Uhr?** → *Für 19 Uhr, bitte.*  
• **Auf welchen Namen?** → *Auf den Namen [Surname].*

### Arriving at the Restaurant

• **Guten Abend! Wir haben einen Tisch reserviert.**  
  *(Good evening! We have reserved a table.)*  
• **Ist dieser Platz frei?**  
  *(Is this seat free?)* → *Ja, bitte nehmen Sie Platz!*
""",
            "fillIns": [
                {"q": "Ich möchte einen ___ (table) für zwei Personen reservieren.", "a": "Tisch"},
                {"q": "Die ___ (menu), bitte!", "a": "Speisekarte"},
                {"q": "Ist dieser ___ (seat) frei?", "a": "Platz"},
                {"q": "Auf welchen ___ (name)?", "a": "Namen"},
                {"q": "Der ___ (waiter) bringt das Essen.", "a": "Kellner"}
            ],
            "quiz": [
                {"question": "How do you ask 'Is this seat free?'", "answer": "Ist dieser Platz frei?", "options": ["Ist dieser Tisch voll?", "Ist dieser Platz frei?", "Haben Sie Platz?", "Wo ist mein Platz?"]},
                {"question": "How do you reserve a table for 4 people?", "answer": "Ich möchte einen Tisch für vier Personen reservieren.", "options": ["Ich will vier Tische.", "Ich möchte einen Tisch für vier Personen reservieren.", "Ich kaufe vier Tische.", "Ein Tisch ist vier Personen."]},
                {"question": "What is 'die Speisekarte'?", "answer": "the menu", "options": ["the bill", "the postcard", "the menu", "the recipe"]},
                {"question": "What does 'reservieren' mean?", "answer": "to reserve / book", "options": ["to order", "to reserve / book", "to pay", "to clean"]}
            ],
            "checkpoints": [
                "I know 8 restaurant entrance and booking vocabulary terms",
                "I can make a phone table reservation in German",
                "I can ask if a seat is free upon arrival",
                "I know to ask for 'die Speisekarte'"
            ],
            "tomorrow": "Ordering courses (Vorspeise, Hauptspeise, Nachspeise)!"
        },
        {
            "dayNum": 51, "title": "Ordering Food: Starters, Mains & Desserts",
            "vocab": [
                {"word": "ich möchte", "article": "", "badge": "phrase", "translation": "I would like", "ipa": "/ɪç ˈmøːçtə/", "ex": "Ich möchte bestellen.", "exEn": "I would like to order."},
                {"word": "für mich", "article": "", "badge": "phrase", "translation": "for me", "ipa": "/fyːɐ̯ mɪç/", "ex": "Für mich eine Suppe, bitte.", "exEn": "For me a soup, please."},
                {"word": "die Vorspeise", "article": "die", "badge": "noun", "translation": "the starter / appetizer", "ipa": "/ˈfoːɐ̯ˌʃpaɪzə/", "ex": "Als Vorspeise nehme ich eine Suppe.", "exEn": "As a starter I take a soup."},
                {"word": "die Hauptspeise", "article": "die", "badge": "noun", "translation": "the main course", "ipa": "/ˈhaʊptˌʃpaɪzə/", "ex": "Als Hauptspeise nehme ich ein Schnitzel.", "exEn": "As a main course I take a schnitzel."},
                {"word": "die Nachspeise", "article": "die", "badge": "noun", "translation": "the dessert", "ipa": "/ˈnaːxˌʃpaɪzə/", "ex": "Als Nachspeise möchte ich Eis.", "exEn": "As a dessert I would like ice cream."},
                {"word": "die Suppe", "article": "die", "badge": "noun", "translation": "the soup", "ipa": "/ˈzʊpə/", "ex": "Die Tomatensuppe ist heiβ.", "exEn": "The tomato soup is hot."},
                {"word": "der Salat", "article": "der", "badge": "noun", "translation": "the salad", "ipa": "/zaˈlaːt/", "ex": "Einen kleinen Salat, bitte.", "exEn": "A small salad, please."},
                {"word": "das Schnitzel", "article": "das", "badge": "noun", "translation": "the schnitzel", "ipa": "/ˈʃnɪtsəl/", "ex": "Ein Wiener Schnitzel mit Pommes.", "exEn": "A Viennese schnitzel with chips."}
            ],
            "grammarTitle": "Ordering Patterns: Als Vorspeise / Ich nehme...",
            "grammarContent": """
### 3 Ways to Order Food in German

1. **Ich möchte [Food item + Accusative], bitte.**  
   • *Ich möchte **einen** Salat, bitte.*  
   • *Ich möchte **eine** Tomatensuppe, bitte.*

2. **Ich nehme [Food item + Accusative].**  
   • *Ich nehme **ein** Wiener Schnitzel.*  
   • *Ich nehme **den** Fisch.*

3. **Als [Course] nehme / möchte ich...**  
   • *Als Vorspeise nehme ich eine Suppe.*  
   • *Als Hauptspeise nehme ich das Hähnchen.*  
   • *Als Nachspeise hätte ich gerne ein Eis.*
""",
            "fillIns": [
                {"q": "Als ___ (starter) nehme ich eine Suppe.", "a": "Vorspeise"},
                {"q": "Als ___ (main course) nehme ich das Schnitzel.", "a": "Hauptspeise"},
                {"q": "Als ___ (dessert) möchte ich ein Eis.", "a": "Nachspeise"},
                {"q": "Für ___ (me) ein Wasser, bitte.", "a": "mich"},
                {"q": "Ich nehme ___ (a, m) gemischten Salat.", "a": "einen"}
            ],
            "quiz": [
                {"question": "How do you say 'As a main course I take...'?", "answer": "Als Hauptspeise nehme ich...", "options": ["Als Vorspeise nehme ich...", "Als Hauptspeise nehme ich...", "Als Nachspeise esse ich...", "Als Hauptessen koche ich..."]},
                {"question": "What is 'die Vorspeise'?", "answer": "the starter / appetizer", "options": ["the main course", "the dessert", "the starter / appetizer", "the side dish"]},
                {"question": "What case is used for food items when ordering (nehmen/möchten)?", "answer": "accusative", "options": ["nominative", "accusative", "dative", "genitive"]},
                {"question": "Translate: 'For me a soup, please.'", "answer": "Für mich eine Suppe, bitte.", "options": ["Für mich eine Suppe, bitte.", "Ich bin eine Suppe, bitte.", "Mein ist Suppe, bitte.", "Für mich ein Suppe, bitte."]}
            ],
            "checkpoints": [
                "I know 3 course terms: Vorspeise, Hauptspeise, Nachspeise",
                "I know 3 formulas to order food (Ich möchte..., Ich nehme..., Als...)",
                "I know to use accusative for ordered dishes (einen Salat)",
                "I can order a 3-course meal in German"
            ],
            "tomorrow": "Expressing food preferences with schmecken & lecker!"
        },
        {
            "dayNum": 52, "title": "Food Preferences & Dative Verb schmecken",
            "vocab": [
                {"word": "schmecken", "article": "", "badge": "verb", "translation": "to taste (to someone)", "ipa": "/ˈʃmɛkən/", "ex": "Das Essen schmeckt gut.", "exEn": "The food tastes good."},
                {"word": "lecker", "article": "", "badge": "adj", "translation": "delicious / tasty", "ipa": "/ˈlɛkɐ/", "ex": "Das Schnitzel ist sehr lecker!", "exEn": "The schnitzel is very delicious!"},
                {"word": "köstlich", "article": "", "badge": "adj", "translation": "exquisite / delightful", "ipa": "/ˈkœstlɪç/", "ex": "Der Nachtisch ist köstlich.", "exEn": "The dessert is exquisite."},
                {"word": "das Lieblingsessen", "article": "das", "badge": "noun", "translation": "the favourite food", "ipa": "/ˈliːplɪŋsˌɛsən/", "ex": "Pizza ist mein Lieblingsessen.", "exEn": "Pizza is my favourite food."},
                {"word": "süß", "article": "", "badge": "adj", "translation": "sweet", "ipa": "/zyːs/", "ex": "Der Kuchen ist sehr süß.", "exEn": "The cake is very sweet."},
                {"word": "salzig", "article": "", "badge": "adj", "translation": "salty", "ipa": "/ˈzaltsɪç/", "ex": "Die Suppe ist zu salzig.", "exEn": "The soup is too salty."},
                {"word": "scharf", "article": "", "badge": "adj", "translation": "spicy / hot", "ipa": "/ʃaʁf/", "ex": "Das Curry ist scharf.", "exEn": "The curry is spicy."},
                {"word": "frisch", "article": "", "badge": "adj", "translation": "fresh", "ipa": "/fʁɪʃ/", "ex": "Der Salat ist sehr frisch.", "exEn": "The salad is very fresh."}
            ],
            "grammarTitle": "The Verb schmecken + Dative Pronoun (mir)",
            "grammarContent": """
### Structure of **schmecken** (to taste good to someone)

In German, the **food is the subject**, and the **person is the dative object**!

👉 **Formula: Food (Subject) + schmeckt + Person (Dative Pronoun: mir)**

• *Das Essen schmeckt* **mir** *gut.* (The food tastes good to me = I like the food.)  
• *Die Suppe schmeckt* **mir** *nicht.* (I don't like the soup.)  
• *Wie schmeckt es* **Ihnen**? (How does it taste to you? - formal)  
• *Hat es Ihnen geschmeckt?* (Did you enjoy your meal?)

> 🎯 **Key Adjectives for Food:**  
> • *lecker* (tasty/yummy), *köstlich* (exquisite), *süß* (sweet), *salzig* (salty), *scharf* (spicy).
""",
            "fillIns": [
                {"q": "Das Essen schmeckt ___ (to me) sehr gut.", "a": "mir"},
                {"q": "Die Suppe ist zu ___ (salty).", "a": "salzig"},
                {"q": "Das Schnitzel ist absolut ___ (delicious)!", "a": "lecker"},
                {"q": "Pizza ist mein ___ (favourite food).", "a": "Lieblingsessen"},
                {"q": "Achtung, das Essen ist sehr ___ (spicy)!", "a": "scharf"}
            ],
            "quiz": [
                {"question": "How do you say 'The food tastes good to me'?", "answer": "Das Essen schmeckt mir gut.", "options": ["Ich schmecke das Essen gut.", "Das Essen schmeckt mir gut.", "Das Essen schmeckt mich gut.", "Mein Essen ist schmecken."]},
                {"question": "What is 'das Lieblingsessen'?", "answer": "favourite food", "options": ["favorite drink", "favourite food", "main dish", "dessert"]},
                {"question": "What does 'scharf' mean when describing food?", "answer": "spicy / hot", "options": ["sweet", "salty", "spicy / hot", "sour"]},
                {"question": "What question does a waiter ask to see if you enjoyed your meal?", "answer": "Hat es Ihnen geschmeckt?", "options": ["Wie heißen Sie?", "Hat es Ihnen geschmeckt?", "Bezahlen Sie jetzt?", "Ist das Essen fertig?"]}
            ],
            "checkpoints": [
                "I know how to use 'schmeckt mir gut'",
                "I know taste adjectives: lecker, köstlich, süß, salzig, scharf, frisch",
                "I know terms like Lieblingsessen",
                "I can answer a waiter asking if I enjoyed the food"
            ],
            "tomorrow": "Paying the bill, tipping, and handling restaurant complaints!"
        },
        {
            "dayNum": 53, "title": "Paying the Bill, Tipping & Complaining",
            "vocab": [
                {"word": "die Rechnung", "article": "die", "badge": "noun", "translation": "the bill / check", "ipa": "/ˈʁɛçnʊŋ/", "ex": "Die Rechnung, bitte!", "exEn": "The bill, please!"},
                {"word": "getrennt", "article": "", "badge": "phrase", "translation": "separately (paying)", "ipa": "/ɡəˈtʁɛnt/", "ex": "Wir zahlen getrennt.", "exEn": "We are paying separately."},
                {"word": "zusammen", "article": "", "badge": "phrase", "translation": "together (paying)", "ipa": "/tsuˈzamən/", "ex": "Wir zahlen zusammen.", "exEn": "We are paying together."},
                {"word": "stimmt so", "article": "", "badge": "phrase", "translation": "keep the change!", "ipa": "/ʃtɪmt zoː/", "ex": "20 Euro, stimmt so!", "exEn": "20 euros, keep the change!"},
                {"word": "das Trinkgeld", "article": "das", "badge": "noun", "translation": "the tip (gratuity)", "ipa": "/ˈtʁɪŋkˌɡɛlt/", "ex": "Ich gebe 2 Euro Trinkgeld.", "exEn": "I give a 2 euro tip."},
                {"word": "kalt", "article": "", "badge": "adj", "translation": "cold", "ipa": "/kalt/", "ex": "Die Suppe ist leider kalt.", "exEn": "The soup is unfortunately cold."},
                {"word": "falsch", "article": "", "badge": "adj", "translation": "wrong / incorrect", "ipa": "/falʃ/", "ex": "Das ist das falsche Gericht.", "exEn": "That is the wrong dish."},
                {"word": "fehlen", "article": "", "badge": "verb", "translation": "to be missing / lacking", "ipa": "/ˈfeːlən/", "ex": "Hier fehlt ein Löffel.", "exEn": "A spoon is missing here."}
            ],
            "grammarTitle": "Paying & Tipping Etiquette in Germany",
            "grammarContent": """
### How to Ask for the Bill

• **Zahlen, bitte!** / **Wir möchten bitte bezahlen.**  
• **Die Rechnung, bitte!**

### Together or Separately?
Waiters in Germany will always ask: **Zusammen oder getrennt?**

• **Getrennt, bitte.** = Each person pays for their own food.  
• **Zusammen, bitte.** = One person pays the total bill.

### Tipping Culture in Germany (5–10%)

In Germany, you tell the waiter the **total amount including tip** when handing over cash!

• Bill is 18,20 € → Hand over 20 € bill and say: **"20 Euro, bitte!"** (or **"Stimmt so!"**)  
• The waiter will give you back 0 € change (tipping ~1.80 €).
""",
            "fillIns": [
                {"q": "Wir möchten bitte ___ (pay).", "a": "bezahlen"},
                {"q": "Zusammen oder ___ (separately)?", "a": "getrennt"},
                {"q": "25 Euro, ___ (keep the change)!", "a": "stimmt so"},
                {"q": "Entschuldigung, die Suppe ist ___ (cold).", "a": "kalt"},
                {"q": "Hier ___ (is missing) ein Messer.", "a": "fehlt"}
            ],
            "quiz": [
                {"question": "How do you tell a German waiter to keep the change as a tip?", "answer": "Stimmt so!", "options": ["Danke schön!", "Stimmt so!", "Auf Wiedersehen!", "Kein Problem!"]},
                {"question": "What is the standard question a German waiter asks when bringing the bill?", "answer": "Zusammen oder getrennt?", "options": ["Was möchten Sie?", "Zusammen oder getrennt?", "Hat es geschmeckt?", "Ist das alles?"]},
                {"question": "What is 'das Trinkgeld'?", "answer": "the tip", "options": ["the beverage", "the bill", "the tip", "the receipt"]},
                {"question": "Translate: 'The soup is unfortunately cold.'", "answer": "Die Suppe ist leider kalt.", "options": ["Die Suppe ist sehr lecker.", "Die Suppe ist leider kalt.", "Die Suppe fehlt hier.", "Die Suppe ist zu scharf."]}
            ],
            "checkpoints": [
                "I can ask for the bill (Zahlen bitte / Die Rechnung bitte)",
                "I know the difference between zusammen and getrennt",
                "I know how to tip using 'Stimmt so!'",
                "I can politely point out an issue with food (Die Suppe ist kalt)"
            ],
            "tomorrow": "Full restaurant role-play conversation!"
        },
        {
            "dayNum": 54, "title": "Full Restaurant Role-Play Conversation",
            "vocab": [
                {"word": "Entschuldigung", "article": "", "badge": "phrase", "translation": "excuse me / sorry", "ipa": "/ɛntˈʃʊldɪɡʊŋ/", "ex": "Entschuldigung, bringen Sie uns die Karte?", "exEn": "Excuse me, will you bring us the menu?"},
                {"word": "sofort", "article": "", "badge": "phrase", "translation": "immediately / right away", "ipa": "/zoˈfɔʁt/", "ex": "Ich komme sofort!", "exEn": "I am coming right away!"},
                {"word": "Moment bitte", "article": "", "badge": "phrase", "translation": "one moment please", "ipa": "/moˈmɛnt ˈbɪtə/", "ex": "Einen Moment bitte!", "exEn": "One moment please!"},
                {"word": "empfehlen", "article": "", "badge": "verb", "translation": "to recommend (e → ie)", "ipa": "/ɛmˈpfeːlən/", "ex": "Was empfehlen Sie?", "exEn": "What do you recommend?"},
                {"word": "besonders", "article": "", "badge": "phrase", "translation": "especially / particularly", "ipa": "/bəˈzɔndɐs/", "ex": "Das Schnitzel ist besonders gut.", "exEn": "The schnitzel is especially good."},
                {"word": "frisch", "article": "", "badge": "adj", "translation": "fresh", "ipa": "/fʁɪʃ/", "ex": "Der Fisch ist heute ganz frisch.", "exEn": "The fish is completely fresh today."},
                {"word": "probieren", "article": "", "badge": "verb", "translation": "to try / taste", "ipa": "/pʁoˈbiːʁən/", "ex": "Möchten Sie das Dessert probieren?", "exEn": "Would you like to try the dessert?"},
                {"word": "der Nachtisch", "article": "der", "badge": "noun", "translation": "the dessert (informal)", "ipa": "/ˈnaːxˌtɪʃ/", "ex": "Als Nachtisch nehme ich Eis.", "exEn": "As dessert I take ice cream."}
            ],
            "grammarTitle": "Full Restaurant Master Role-Play Text",
            "grammarContent": """
### Restaurant Conversation Script

> **Kellner:** *Guten Abend! Haben Sie reserviert?*  
> **Gast:** *Guten Abend! Ja, auf den Namen Müller für zwei Personen.*  
> **Kellner:** *Ah ja! Bitte kommen Sie mit. Hier ist Ihr Tisch.*  
> **Gast:** *Danke! Können wir bitte die Speisekarte haben?*  
> **Kellner:** *Gerne, hier ist die Karte. Was möchten Sie trinken?*  
> **Gast:** *Für mich bitte ein Mineralwasser und für meine Frau einen Apfelsaft.*  
> **Kellner:** *Kommt sofort! Und was möchten Sie essen? Was kann ich Ihnen empfehlen?*  
> **Gast:** *Ich nehme als Vorspeise eine Tomatensuppe und als Hauptspeise das Schnitzel.*  
> **Kellner:** *Sehr gute Wahl!*  
> *(After the meal)*  
> **Kellner:** *Hat es Ihnen geschmeckt?*  
> **Gast:** *Ja, es war köstlich! Wir möchten bitte zahlen. Zusammen, bitte.*  
> **Kellner:** *Das macht 34 Euro 50.*  
> **Gast:** *Hier sind 38 Euro, stimmt so!*  
> **Kellner:** *Vielen Dank und einen schönen Abend noch!*
""",
            "fillIns": [
                {"q": "Was ___ (do you recommend) Sie?", "a": "empfehlen"},
                {"q": "Die Getränke kommen ___ (immediately).", "a": "sofort"},
                {"q": "Einen ___ (moment), bitte!", "a": "Moment"},
                {"q": "Als ___ (dessert) nehme ich Kuchen.", "a": "Nachtisch"},
                {"q": "Möchten Sie den Wein ___ (try/taste)?", "a": "probieren"}
            ],
            "quiz": [
                {"question": "How do you ask a waiter 'What do you recommend?'", "answer": "Was empfehlen Sie?", "options": ["Was kochen Sie?", "Was empfehlen Sie?", "Was essen Sie?", "Was haben Sie?"]},
                {"question": "What is 'der Nachtisch'?", "answer": "the dessert", "options": ["the main course", "the starter", "the dessert", "the night table"]},
                {"question": "What does a waiter mean by 'Kommt sofort!'?", "answer": "Coming right away!", "options": ["Coming tomorrow!", "Coming right away!", "We don't have that!", "Please wait 1 hour!"]},
                {"question": "Translate: 'Das ist besonders gut.'", "answer": "That is especially good.", "options": ["That is bad.", "That is especially good.", "That is cheap.", "That is wrong."]}
            ],
            "checkpoints": [
                "I can read and follow a complete restaurant dialogue",
                "I can ask for recommendations (Was empfehlen Sie?)",
                "I can order drinks, starter, main, and dessert fluently",
                "I can pay, tip, and close a restaurant visit smoothly"
            ],
            "tomorrow": "Basic colours & clothing vocabulary!"
        },
        {
            "dayNum": 55, "title": "Colours & Basic Clothing Vocabulary",
            "vocab": [
                {"word": "rot", "article": "", "badge": "adj", "translation": "red", "ipa": "/ʁoːt/", "ex": "Die Tomate ist rot.", "exEn": "The tomato is red."},
                {"word": "blau", "article": "", "badge": "adj", "translation": "blue", "ipa": "/blaʊ/", "ex": "Der Himmel ist blau.", "exEn": "The sky is blue."},
                {"word": "grün", "article": "", "badge": "adj", "translation": "green", "ipa": "/ɡʁyːn/", "ex": "Der Salat ist grün.", "exEn": "The salad is green."},
                {"word": "schwarz", "article": "", "badge": "adj", "translation": "black", "ipa": "/ʃvaʁts/", "ex": "Ich trinke schwarzen Kaffee.", "exEn": "I drink black coffee."},
                {"word": "weiß", "article": "", "badge": "adj", "translation": "white", "ipa": "/vaɪs/", "ex": "Das Hemd ist weiß.", "exEn": "The shirt is white."},
                {"word": "das Hemd", "article": "das", "badge": "noun", "translation": "the shirt (men's)", "ipa": "/hɛmt/", "ex": "Er trägt ein weißes Hemd.", "exEn": "He is wearing a white shirt."},
                {"word": "die Hose", "article": "die", "badge": "noun", "translation": "the trousers / pants", "ipa": "/ˈhoːzə/", "ex": "Die Hose ist blau.", "exEn": "The trousers are blue."},
                {"word": "der Schuh", "article": "der", "badge": "noun", "translation": "the shoe (pl: Schuhe)", "ipa": "/ʃuː/", "ex": "Die Schuhe sind schwarz.", "exEn": "The shoes are black."}
            ],
            "grammarTitle": "Colours & Predicate Adjectives with Clothing",
            "grammarContent": """
### Basic Colours in German

| Colour | German | Example |
|:---:|:---:|:---|
| 🔴 **Red** | **rot** | Das Kleid ist *rot*. |
| 🔵 **Blue** | **blau** | Die Hose ist *blau*. |
| 🟢 **Green** | **grün** | Der Apfel ist *grün*. |
| 🟡 **Yellow** | **gelb** | Die Sonne ist *gelb*. |
| ⚫ **Black** | **schwarz** | Der Schuh ist *schwarz*. |
| ⚪ **White** | **weiß** | Das Hemd ist *weiß*. |
| 🟤 **Brown** | **braun** | Der Koffer ist *braun*. |

> 🎯 **Predicate Adjectives (After sein):**  
> Just like room adjectives, colours placed AFTER *ist* or *sind* take **NO endings**!  
> • *Das Hemd ist weiß.*  
> • *Die Schuhe sind schwarz.*
""",
            "fillIns": [
                {"q": "Die Tomate ist ___ (red).", "a": "rot"},
                {"q": "Die Jeanshose ist ___ (blue).", "a": "blau"},
                {"q": "Das ___ (shirt) ist weiß.", "a": "Hemd"},
                {"q": "Die ___ (trousers) ist grün.", "a": "Hose"},
                {"q": "Meine ___ (shoes) sind schwarz.", "a": "Schuhe"}
            ],
            "quiz": [
                {"question": "What is 'weiß' in English?", "answer": "white", "options": ["black", "yellow", "white", "blue"]},
                {"question": "What is 'die Hose'?", "answer": "trousers / pants", "options": ["house", "trousers / pants", "shirt", "shoe"]},
                {"question": "Do colour adjectives take endings when placed after 'ist' or 'sind'?", "answer": "no, they stay unchanged", "options": ["yes, add -e", "no, they stay unchanged", "yes, add -en", "depends on gender"]},
                {"question": "Translate: 'The shoes are black.'", "answer": "Die Schuhe sind schwarz.", "options": ["Die Schuhe ist schwarz.", "Die Schuhe sind schwarz.", "Der Schuh ist schwarz.", "Die Schuhe sind weiß."]}
            ],
            "checkpoints": [
                "I know 7 basic German colours (rot, blau, grün, gelb, schwarz, weiß, braun)",
                "I know 3 key clothing items (Hemd, Hose, Schuh)",
                "I know colours take no endings when placed after ist/sind",
                "I can describe what someone is wearing by colour"
            ],
            "tomorrow": "Week 8 Review and Speaking Practice!"
        },
        {
            "dayNum": 56, "isReview": True, "title": "Week 8 Review & Speaking Practice",
            "reviewCards": [
                {"german": "die Speisekarte", "english": "the menu", "example": "Die Speisekarte, bitte!"},
                {"german": "der Kellner / die Kellnerin", "english": "waiter / waitress", "example": "Der Kellner bringt die Karte."},
                {"german": "einen Tisch reservieren", "english": "reserve a table", "example": "Ich möchte einen Tisch reservieren."},
                {"german": "Ist dieser Platz frei?", "english": "Is this seat free?", "example": "Ja, bitte nehmen Sie Platz!"},
                {"german": "die Vorspeise", "english": "starter", "example": "Als Vorspeise eine Suppe."},
                {"german": "die Hauptspeise", "english": "main course", "example": "Als Hauptspeise ein Schnitzel."},
                {"german": "die Nachspeise / Nachtisch", "english": "dessert", "example": "Als Nachspeise ein Eis."},
                {"german": "Das Essen schmeckt mir gut.", "english": "The food tastes good to me.", "example": "Wie schmeckt es Ihnen?"},
                {"german": "lecker / köstlich", "english": "delicious", "example": "Das Gericht ist sehr lecker."},
                {"german": "süß / salzig / scharf", "english": "sweet / salty / spicy", "example": "Das Curry ist scharf."},
                {"german": "Zahlen, bitte!", "english": "The bill, please!", "example": "Wir möchten bezahlen."},
                {"german": "zusammen oder getrennt?", "english": "together or separately?", "example": "Getrennt, bitte."},
                {"german": "Stimmt so!", "english": "Keep the change!", "example": "20 Euro, stimmt so!"},
                {"german": "Was empfehlen Sie?", "english": "What do you recommend?", "example": "Was empfehlen Sie heute?"},
                {"german": "rot, blau, grün, schwarz, weiß", "english": "red, blue, green, black, white", "example": "Das Hemd ist weiß."}
            ],
            "grammarSummary": """
### Week 8 Master Summary

1. **Table Reservations:** *Ich möchte einen Tisch für [X] Personen auf den Namen [Name] reservieren.*
2. **Ordering:**  
   - *Ich möchte einen [Item + Accusative], bitte.*  
   - *Als Vorspeise / Hauptspeise / Nachspeise nehme ich...*
3. **Food Preferences & schmecken:**  
   - *Das Essen schmeckt mir gut.* (Person is in Dative: *mir*)  
   - Descriptors: *lecker, köstlich, süß, salzig, scharf, frisch*.
4. **Paying & Tipping:**  
   - *Zusammen oder getrennt?* (Together or separate?)  
   - *Stimmt so!* (Keep the change!). Tipping is 5-10% in Germany.
5. **Colours:** *rot, blau, grün, gelb, schwarz, weiß, braun*. No endings after *ist/sind*!
""",
            "quiz": [
                {"question": "How do you ask for the bill in a restaurant?", "answer": "Zahlen, bitte! / Die Rechnung, bitte!", "options": ["Wo ist das Essen?", "Zahlen, bitte! / Die Rechnung, bitte!", "Ich kaufe das!", "Wie viel Geld haben Sie?"]},
                {"question": "What phrase tells a waiter to keep the change?", "answer": "Stimmt so!", "options": ["Danke vielmals!", "Stimmt so!", "Kein Problem!", "Guten Appetit!"]},
                {"question": "How do you order a starter in German?", "answer": "Als Vorspeise nehme ich...", "options": ["Als Hauptspeise esse ich...", "Als Vorspeise nehme ich...", "Als Nachspeise trinke ich...", "Ich kaufe Vorspeise."]},
                {"question": "Translate: 'The food tastes good to me.'", "answer": "Das Essen schmeckt mir gut.", "options": ["Ich schmecke das Essen gut.", "Das Essen schmeckt mir gut.", "Das Essen ist mir scharf.", "Ich habe gutes Essen."]},
                {"question": "What is 'die Kellnerin'?", "answer": "the waitress", "options": ["the female cook", "the waitress", "the manager", "the customer"]},
                {"question": "What does 'scharf' mean when describing food?", "answer": "spicy", "options": ["sweet", "salty", "spicy", "cold"]},
                {"question": "How do you say 'We are paying separately'?", "answer": "Wir zahlen getrennt.", "options": ["Wir zahlen zusammen.", "Wir zahlen getrennt.", "Wir bezahlen nicht.", "Wir zahlen alleine."]},
                {"question": "What colour is 'weiß'?", "answer": "white", "options": ["black", "yellow", "white", "blue"]}
            ],
            "speakingPrompt": """
### 🗣️ Speaking Exercise — Order a 3-Course Meal & Pay

Read this script aloud and record yourself or practice with a partner:

> *"Guten Abend! Wir haben einen Tisch für zwei Personen auf den Namen Schmidt reserviert. Danke! Als Vorspeise nehme ich eine Tomatensuppe. Als Hauptspeise nehme ich ein Wiener Schnitzel mit Pommes und einen gemischten Salat. Zum Trinken möchte ich ein Mineralwasser. Das Essen ist wirklich lecker und sehr frisch! Wir möchten jetzt zahlen. Getrennt, bitte. Das macht 22 Euro? Hier sind 25 Euro, stimmt so! Auf Wiedersehen!"*
""",
            "checkpoints": [
                "I can reserve a table and enter a restaurant in German",
                "I can order a 3-course meal using Vorspeise, Hauptspeise, Nachspeise",
                "I can express taste using schmecken mir and adjectives like lecker/scharf",
                "I can handle paying, splitting the bill, tipping, and leaving"
            ]
        }
    ]
}

print("Week 8 data populated.")
