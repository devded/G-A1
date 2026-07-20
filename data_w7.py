# Week 7 Data

w7 = {
    "weekNum": 7,
    "title": "Food, Drinks & Shopping",
    "level": "A1.2",
    "goal": "Name food and drinks, master the Accusative case (der → den, ein → einen), express quantities, and conduct a full supermarket shopping dialogue.",
    "days": [
        {
            "dayNum": 43, "title": "Food Vocabulary & Uncountable Nouns",
            "vocab": [
                {"word": "das Brot", "article": "das", "badge": "noun", "translation": "the bread", "ipa": "/bʁoːt/", "ex": "Das Brot ist frisch.", "exEn": "The bread is fresh."},
                {"word": "das Fleisch", "article": "das", "badge": "noun", "translation": "the meat", "ipa": "/flaɪʃ/", "ex": "Ich esse kein Fleisch.", "exEn": "I eat no meat."},
                {"word": "das Gemüse", "article": "das", "badge": "noun", "translation": "the vegetables", "ipa": "/ɡəˈmyːzə/", "ex": "Gemüse ist gesund.", "exEn": "Vegetables are healthy."},
                {"word": "das Obst", "article": "das", "badge": "noun", "translation": "the fruit", "ipa": "/oːpst/", "ex": "Ich kaufe frisches Obst.", "exEn": "I buy fresh fruit."},
                {"word": "der Käse", "article": "der", "badge": "noun", "translation": "the cheese", "ipa": "/ˈkɛːzə/", "ex": "Der Käse schmeckt gut.", "exEn": "The cheese tastes good."},
                {"word": "die Wurst", "article": "die", "badge": "noun", "translation": "the sausage / cold cuts", "ipa": "/vʊʁst/", "ex": "Die Wurst ist lecker.", "exEn": "The sausage is delicious."},
                {"word": "das Ei", "article": "das", "badge": "noun", "translation": "the egg (pl: Eier)", "ipa": "/aɪ/", "ex": "Ich esse morgens ein Ei.", "exEn": "I eat an egg in the morning."},
                {"word": "der Reis", "article": "der", "badge": "noun", "translation": "the rice", "ipa": "/ʁaɪs/", "ex": "Reis ist billig.", "exEn": "Rice is cheap."}
            ],
            "grammarTitle": "Food Nouns & General Food Expressions",
            "grammarContent": """
### General Statements (No Article!)

When talking about food in general (without specifying a particular item), **do not use an article**:

• *Ich esse gerne* **Brot**. (I like eating bread.)  
• *Ich esse kein* **Fleisch**. (I eat no meat.)  
• **Obst und Gemüse** *sind gesund.* (Fruit and vegetables are healthy.)

### Collective Nouns in German

• **das Obst** = fruit in general (singular only!)  
• **das Gemüse** = vegetables in general (singular only!)
""",
            "fillIns": [
                {"q": "Ich esse morgens frisches ___ (bread).", "a": "Brot"},
                {"q": "Er isst kein ___ (meat), er ist Vegetarier.", "a": "Fleisch"},
                {"q": "___ (Fruit) und Gemüse sind sehr gesund.", "a": "Obst"},
                {"q": "Ich kaufe ___ (cheese) und Wurst.", "a": "Käse"},
                {"q": "Zum Mittagessen esse ich ___ (rice).", "a": "Reis"}
            ],
            "quiz": [
                {"question": "What is the article for 'Brot'?", "answer": "das", "options": ["der", "die", "das", "den"]},
                {"question": "What is the article for 'Käse'?", "answer": "der", "options": ["der", "die", "das", "den"]},
                {"question": "What are collective food nouns like 'Obst' and 'Gemüse' in German?", "answer": "singular neuter (das)", "options": ["plural (die)", "singular neuter (das)", "masculine (der)", "feminine (die)"]},
                {"question": "Translate: 'Ich esse kein Fleisch.'", "answer": "I eat no meat.", "options": ["I eat meat.", "I eat no meat.", "I like meat.", "I buy meat."]}
            ],
            "checkpoints": [
                "I know 8 fundamental food vocabulary terms",
                "I know that general food statements don't use articles",
                "I know that das Obst and das Gemüse are singular neuter nouns",
                "I can state basic food preferences"
            ],
            "tomorrow": "Drinks & breakfast vocabulary with 'möchten'!"
        },
        {
            "dayNum": 44, "title": "Drinks, Breakfast & Verb möchten",
            "vocab": [
                {"word": "der Kaffee", "article": "der", "badge": "noun", "translation": "the coffee", "ipa": "/ˈkafe/", "ex": "Ich trinke morgens Kaffee.", "exEn": "I drink coffee in the morning."},
                {"word": "der Tee", "article": "der", "badge": "noun", "translation": "the tea", "ipa": "/teː/", "ex": "Möchtest du Tee?", "exEn": "Would you like tea?"},
                {"word": "das Wasser", "article": "das", "badge": "noun", "translation": "the water", "ipa": "/ˈvasɐ/", "ex": "Ein Glas Wasser, bitte.", "exEn": "A glass of water, please."},
                {"word": "der Saft", "article": "der", "badge": "noun", "translation": "the juice", "ipa": "/zaft/", "ex": "Ich trinke Orangensaft.", "exEn": "I drink orange juice."},
                {"word": "die Milch", "article": "die", "badge": "noun", "translation": "the milk", "ipa": "/mɪlç/", "ex": "Kaffee mit Milch, bitte.", "exEn": "Coffee with milk, please."},
                {"word": "das Bier", "article": "das", "badge": "noun", "translation": "the beer", "ipa": "/biːɐ/", "ex": "Ein Bier, bitte!", "exEn": "A beer, please!"},
                {"word": "der Wein", "article": "der", "badge": "noun", "translation": "the wine", "ipa": "/vaɪn/", "ex": "Der Rotwein ist gut.", "exEn": "The red wine is good."},
                {"word": "das Frühstück", "article": "das", "badge": "noun", "translation": "the breakfast", "ipa": "/ˈfʁyːʃtʏk/", "ex": "Das Frühstück ist fertig.", "exEn": "The breakfast is ready."}
            ],
            "grammarTitle": "The Polite Verb: möchten (would like)",
            "grammarContent": """
### Conjugation: **möchten** (would like)

Used in ordering and polite requests. Notice that **ich** and **er/sie/es** share the exact same form (**möchte**)!

| Pronoun | Form | Example |
|:---:|:---:|:---|
| ich | möch**te** | Ich *möchte* einen Kaffee. |
| du | möch**test** | Was *möchtest* du trinken? |
| er/sie/es | möch**te** | Er *möchte* ein Bier. |
| wir | möch**ten** | Wir *möchten* bestellen. |
| ihr | möch**tet** | Was *möchtet* ihr essen? |
| Sie/sie | möch**ten** | Was *möchten* Sie, bitte? |

> <Icon name="target" /> **Accusative Reminder:**  
> • der Kaffee → Ich möchte **einen** Kaffee. (masculine → einen)  
> • das Wasser → Ich möchte **ein** Wasser. (neuter → ein)  
> • die Milch → Ich möchte **eine** Milch. (feminine → eine)
""",
            "fillIns": [
                {"q": "Ich ___ (would like) einen Kaffee, bitte.", "a": "möchte"},
                {"q": "Was ___ (would like) du trinken?", "a": "möchtest"},
                {"q": "Wir ___ (would like) bestellen.", "a": "möchten"},
                {"q": "Ich möchte einen Kaffee mit ___ (milk).", "a": "Milch"},
                {"q": "Kaffee: der → Ich möchte ___ (a, m) Kaffee.", "a": "einen"}
            ],
            "quiz": [
                {"question": "What is the 'ich' form of möchten?", "answer": "ich möchte", "options": ["ich möcht", "ich möchte", "ich möchtest", "ich mag"]},
                {"question": "What is the accusative of 'der Kaffee' after möchte?", "answer": "einen Kaffee", "options": ["ein Kaffee", "einen Kaffee", "eine Kaffee", "dem Kaffee"]},
                {"question": "How do you politely order a water in German?", "answer": "Ich möchte ein Wasser, bitte.", "options": ["Ich möchte ein Wasser, bitte.", "Ich will Wasser.", "Gib mir Wasser.", "Ich bin Wasser."]},
                {"question": "What is 'das Frühstück'?", "answer": "the breakfast", "options": ["the lunch", "the dinner", "the breakfast", "the snack"]}
            ],
            "checkpoints": [
                "I know 7 common drinks and 'das Frühstück'",
                "I can conjugate the polite verb möchten",
                "I know that ich and er/sie/es forms of möchte are identical",
                "I can order drinks politely using möchte + Accusative"
            ],
            "tomorrow": "Deep dive into the Accusative Case (kaufen, brauchen, essen)!"
        },
        {
            "dayNum": 45, "title": "The Accusative Case Deep Dive",
            "vocab": [
                {"word": "kaufen", "article": "", "badge": "verb", "translation": "to buy", "ipa": "/ˈkaʊfən/", "ex": "Ich kaufe einen Apfel.", "exEn": "I buy an apple."},
                {"word": "bestellen", "article": "", "badge": "verb", "translation": "to order (food/goods)", "ipa": "/bəˈʃtɛlən/", "ex": "Wir bestellen eine Pizza.", "exEn": "We are ordering a pizza."},
                {"word": "brauchen", "article": "", "badge": "verb", "translation": "to need", "ipa": "/ˈbʁaʊxən/", "ex": "Ich brauche einen Tisch.", "exEn": "I need a table."},
                {"word": "nehmen", "article": "", "badge": "verb", "translation": "to take (e → i/imm)", "ipa": "/ˈneːmən/", "ex": "Er nimmt einen Salat.", "exEn": "He takes a salad."},
                {"word": "bezahlen", "article": "", "badge": "verb", "translation": "to pay for", "ipa": "/bəˈtsaːlən/", "ex": "Ich bezahle die Rechnung.", "exEn": "I pay the bill."},
                {"word": "suchen", "article": "", "badge": "verb", "translation": "to search for / look for", "ipa": "/ˈzuːxən/", "ex": "Ich suche den Supermarkt.", "exEn": "I am looking for the supermarket."},
                {"word": "trinken", "article": "", "badge": "verb", "translation": "to drink", "ipa": "/ˈtʁɪŋkən/", "ex": "Er trinkt einen Saft.", "exEn": "He drinks a juice."},
                {"word": "essen", "article": "", "badge": "verb", "translation": "to eat (e → i)", "ipa": "/ˈɛsən/", "ex": "Sie isst ein Brot.", "exEn": "She eats a bread."}
            ],
            "grammarTitle": "Master Accusative Case Table (All Articles)",
            "grammarContent": """
### The Accusative Case: Direct Object of an Action

The Accusative case receives the action of the verb (*kaufen, bestellen, brauchen, nehmen, trinken, essen*).  
<Icon name="arrow-right" /> **ONLY MASCULINE CHANGES!** Everything else is identical to Nominative!

| Gender | Definite (the) | Indefinite (a / an) | Negative (no / none) | Possessive (my) |
|:---:|:---:|:---:|:---:|:---:|
| **Masculine** | **den** | **einen** | **keinen** | **meinen** |
| **Feminine** | **die** | **eine** | **keine** | **meine** |
| **Neuter** | **das** | **ein** | **kein** | **mein** |
| **Plural** | **die** | **—** | **keine** | **meine** |

> <Icon name="target" /> **Examples:**  
> • der Apfel → Ich esse **den** Apfel / **einen** Apfel / **keinen** Apfel.  
> • die Banane → Ich esse **die** Banane / **eine** Banane.  
> • das Ei → Ich esse **das** Ei / **ein** Ei.
""",
            "fillIns": [
                {"q": "der Apfel: Ich kaufe ___ (a, m) Apfel.", "a": "einen"},
                {"q": "der Fisch: Er isst ___ (no, m) Fisch.", "a": "keinen"},
                {"q": "die Pizza: Wir bestellen ___ (a, f) Pizza.", "a": "eine"},
                {"q": "das Brot: Sie braucht ___ (a, n) Brot.", "a": "ein"},
                {"q": "der Schlüssel: Ich suche ___ (my, m) Schlüssel.", "a": "meinen"}
            ],
            "quiz": [
                {"question": "What is the accusative definite article for masculine nouns?", "answer": "den", "options": ["der", "die", "das", "den"]},
                {"question": "What is the accusative indefinite article for masculine nouns?", "answer": "einen", "options": ["ein", "einen", "eine", "einem"]},
                {"question": "Conjugate: er + nehmen (to take)", "answer": "er nimmt", "options": ["er nehmst", "er nimmt", "er nehmte", "er nahm"]},
                {"question": "Translate: 'I need a table' (der Tisch)", "answer": "Ich brauche einen Tisch.", "options": ["Ich brauche ein Tisch.", "Ich brauche einen Tisch.", "Ich brauche der Tisch.", "Ich brauche eine Tisch."]}
            ],
            "checkpoints": [
                "I know that only masculine articles change in the accusative case",
                "I know der → den, ein → einen, kein → keinen, mein → meinen",
                "I know high-frequency verbs that take accusative (kaufen, brauchen, nehmen)",
                "I can form correct accusative sentences effortlessly"
            ],
            "tomorrow": "Food items & quantity expressions (Kilo, Flasche, Stück)!"
        },
        {
            "dayNum": 46, "title": "Food Items & Quantity Expressions",
            "vocab": [
                {"word": "der Apfel", "article": "der", "badge": "noun", "translation": "the apple (pl: Äpfel)", "ipa": "/ˈapfəl/", "ex": "Ich esse einen Apfel.", "exEn": "I am eating an apple."},
                {"word": "die Tomate", "article": "die", "badge": "noun", "translation": "the tomato (pl: Tomaten)", "ipa": "/toˈmaːtə/", "ex": "Ich brauche vier Tomaten.", "exEn": "I need four tomatoes."},
                {"word": "die Kartoffel", "article": "die", "badge": "noun", "translation": "the potato (pl: Kartoffeln)", "ipa": "/kaʁˈtɔfəl/", "ex": "Ich kaufe ein Kilo Kartoffeln.", "exEn": "I buy a kilo of potatoes."},
                {"word": "das Hähnchen", "article": "das", "badge": "noun", "translation": "the chicken", "ipa": "/ˈhɛːnçən/", "ex": "Hähnchen mit Reis, bitte.", "exEn": "Chicken with rice, please."},
                {"word": "der Fisch", "article": "der", "badge": "noun", "translation": "the fish (pl: Fische)", "ipa": "/fɪʃ/", "ex": "Ich esse keinen Fisch.", "exEn": "I eat no fish."},
                {"word": "das Kilo", "article": "das", "badge": "noun", "translation": "the kilo (kilogram)", "ipa": "/ˈkiːlo/", "ex": "Ein Kilo Äpfel, bitte.", "exEn": "A kilo of apples, please."},
                {"word": "die Flasche", "article": "die", "badge": "noun", "translation": "the bottle", "ipa": "/ˈflaʃə/", "ex": "Eine Flasche Wasser, bitte.", "exEn": "A bottle of water, please."},
                {"word": "das Stück", "article": "das", "badge": "noun", "translation": "the piece / slice", "ipa": "/ʃtʏk/", "ex": "Ein Stück Kuchen, bitte.", "exEn": "A piece of cake, please."}
            ],
            "grammarTitle": "Quantity Expressions in German",
            "grammarContent": """
### Quantities: No Preposition Needed!

In English, you say "a kilo **of** apples" or "a bottle **of** water". In German, **do NOT use 'von'**! Just put the quantity right before the item:

• **ein Kilo Äpfel** = a kilo of apples  
• **eine Flasche Wasser** = a bottle of water  
• **ein Stück Kuchen** = a piece of cake  
• **eine Packung Reis** = a packet of rice  
• **ein Glas Saft** = a glass of juice

> <Icon name="target" /> **Plural of Quantities:**  
> • Units of measurement stay **singular** after numbers: *zwei Kilo Äpfel* (NOT *zwei Kilos*), *drei Glas Wasser*!
""",
            "fillIns": [
                {"q": "Ein Kilo ___ (apples), bitte.", "a": "Äpfel"},
                {"q": "Eine ___ (bottle) Wasser, bitte.", "a": "Flasche"},
                {"q": "Ein ___ (piece) Kuchen, bitte.", "a": "Stück"},
                {"q": "Ich brauche zwei ___ (kilos) Kartoffeln.", "a": "Kilo"},
                {"q": "Ich esse ___ (a, m) Apfel.", "a": "einen"}
            ],
            "quiz": [
                {"question": "How do you say 'a bottle of water' in German?", "answer": "eine Flasche Wasser", "options": ["eine Flasche von Wasser", "eine Flasche Wasser", "ein Flasche Wasser", "eine Flaschen Wasser"]},
                {"question": "Does German use a preposition (like 'of') after quantity words?", "answer": "no, no preposition is used", "options": ["yes, use 'von'", "yes, use 'aus'", "no, no preposition is used", "yes, use 'mit'"]},
                {"question": "What is 'das Stück'?", "answer": "the piece / slice", "options": ["the bottle", "the kilo", "the piece / slice", "the glass"]},
                {"question": "What is the plural of 'der Apfel'?", "answer": "die Äpfel", "options": ["die Apfeln", "die Äpfel", "die Apfels", "die Apfe"]}
            ],
            "checkpoints": [
                "I know 8 food items and quantity units",
                "I know that German quantity phrases do NOT use 'von'",
                "I know measurement units like Kilo stay singular after numbers",
                "I can order food by weight, bottle, or piece"
            ],
            "tomorrow": "Prices, currency, and asking 'Was kostet das?'!"
        },
        {
            "dayNum": 47, "title": "Supermarket Prices & 'Was kostet das?'",
            "vocab": [
                {"word": "der Euro", "article": "der", "badge": "noun", "translation": "the euro (pl: Euro)", "ipa": "/ˈɔʏʁo/", "ex": "Das kostet 2 Euro.", "exEn": "That costs 2 euros."},
                {"word": "der Cent", "article": "der", "badge": "noun", "translation": "the cent (pl: Cent)", "ipa": "/tsɛnt/", "ex": "50 Cent, bitte.", "exEn": "50 cents, please."},
                {"word": "die Kasse", "article": "die", "badge": "noun", "translation": "the checkout / till", "ipa": "/ˈkasə/", "ex": "Wo ist die Kasse?", "exEn": "Where is the checkout?"},
                {"word": "teuer", "article": "", "badge": "adj", "translation": "expensive", "ipa": "/ˈtɔʏɐ/", "ex": "Das Fleisch ist sehr teuer.", "exEn": "The meat is very expensive."},
                {"word": "billig / günstig", "article": "", "badge": "adj", "translation": "cheap / affordable", "ipa": "/ˈbɪlɪç/", "ex": "Äpfel sind heute günstig.", "exEn": "Apples are affordable today."},
                {"word": "das Sonderangebot", "article": "das", "badge": "noun", "translation": "special offer / sale", "ipa": "/ˈzɔndɐ̯ʔanɡəˌboːt/", "ex": "Das ist ein Sonderangebot!", "exEn": "That is a special offer!"},
                {"word": "der Preis", "article": "der", "badge": "noun", "translation": "the price", "ipa": "/pʁaɪs/", "ex": "Der Preis ist gut.", "exEn": "The price is good."},
                {"word": "kosten", "article": "", "badge": "verb", "translation": "to cost", "ipa": "/ˈkɔstən/", "ex": "Was kostet das?", "exEn": "How much does that cost?"}
            ],
            "grammarTitle": "Saying Prices & Money in German",
            "grammarContent": """
### Price Question Formulas

1. **Was kostet das?** (What does that cost?)  
2. **Wie viel kostet [Item]?** (How much does [Item] cost?)  
3. **Wie viel kosten [Plural Items]?** (How much do [Items] cost?)

### Reading Prices Out Loud (Decimals)

In Germany, decimals use a **comma (,)** instead of a point (.)!

• **1,50 €** → *ein Euro fünfzig* (or *eins fünfzig*)  
• **3,99 €** → *drei Euro neunundneunzig*  
• **0,50 €** → *fünfzig Cent*

> <Icon name="lightbulb" /> **Notice:** The word *Euro* stays singular after numbers! (*zwei Euro*, NOT *zwei Euros*).
""",
            "fillIns": [
                {"q": "Was ___ (costs) das?", "a": "kostet"},
                {"q": "Das kostet zwei ___ (euros) fünfzig.", "a": "Euro"},
                {"q": "Das ist sehr ___ (expensive)!", "a": "teuer"},
                {"q": "Wo ist die ___ (checkout/till)?", "a": "Kasse"},
                {"q": "Heute ist das ein ___ (special offer).", "a": "Sonderangebot"}
            ],
            "quiz": [
                {"question": "How do you ask 'How much does that cost?' in German?", "answer": "Was kostet das?", "options": ["Wie teuer ist das?", "Was kostet das?", "Wie viel ist das Preis?", "Was bezahle das?"]},
                {"question": "How do you read '2,99 €' out loud?", "answer": "zwei Euro neunundneunzig", "options": ["zwei Euros neunundneunzig", "zwei Euro neunundneunzig", "zwei Punkte neunundneunzig", "zweihundertneunundneunzig Cent"]},
                {"question": "Does the word 'Euro' take a plural -s after numbers in German?", "answer": "no, it stays 'Euro'", "options": ["yes, add -s", "no, it stays 'Euro'", "yes, add -en", "depends on gender"]},
                {"question": "What is the opposite of 'teuer'?", "answer": "billig / günstig", "options": ["groß", "billig / günstig", "gemütlich", "lecker"]}
            ],
            "checkpoints": [
                "I can ask prices using 'Was kostet das?' and 'Wie viel kosten...?'",
                "I know how to pronounce price tags in euros and cents",
                "I know words like Kasse, Sonderangebot, teuer, billig",
                "I know Euro stays singular after numbers"
            ],
            "tomorrow": "Full supermarket shopping dialogue & interaction!"
        },
        {
            "dayNum": 48, "title": "Supermarket Shopping Dialogue",
            "vocab": [
                {"word": "der Einkauf", "article": "der", "badge": "noun", "translation": "the shopping / purchase", "ipa": "/ˈaɪnkaʊf/", "ex": "Ich mache den Wocheneinkauf.", "exEn": "I am doing the weekly shopping."},
                {"word": "die Einkaufsliste", "article": "die", "badge": "noun", "translation": "the shopping list", "ipa": "/ˈaɪnkaʊfsˌlɪstə/", "ex": "Ich habe meine Einkaufsliste vergessen.", "exEn": "I forgot my shopping list."},
                {"word": "der Einkaufswagen", "article": "der", "badge": "noun", "translation": "the shopping trolley", "ipa": "/ˈaɪnkaʊfsˌvaːɡən/", "ex": "Ich brauche einen Einkaufswagen.", "exEn": "I need a shopping trolley."},
                {"word": "das Regal", "article": "das", "badge": "noun", "translation": "the shelf", "ipa": "/ʁeˈɡaːl/", "ex": "Die Milch ist im Regal links.", "exEn": "The milk is on the shelf on the left."},
                {"word": "wiegen", "article": "", "badge": "verb", "translation": "to weigh", "ipa": "/ˈviːɡən/", "ex": "Ich muss die Äpfel wiegen.", "exEn": "I must weigh the apples."},
                {"word": "das Pfand", "article": "das", "badge": "noun", "translation": "bottle deposit", "ipa": "/pfant/", "ex": "Vergiss das Pfand nicht!", "exEn": "Don't forget the bottle deposit!"},
                {"word": "Bio", "article": "", "badge": "adj", "translation": "organic", "ipa": "/ˈbiːo/", "ex": "Ich kaufe nur Bio-Eier.", "exEn": "I only buy organic eggs."},
                {"word": "die Tüte", "article": "die", "badge": "noun", "translation": "the plastic/paper bag", "ipa": "/ˈtyːtə/", "ex": "Brauchen Sie eine Tüte?", "exEn": "Do you need a bag?"}
            ],
            "grammarTitle": "Full Supermarket Checkout Dialogue",
            "grammarContent": """
### Typical German Supermarket Conversation

> **Kassiererin (Cashier):** *Guten Tag! Haben Sie eine Kundenkarte?*  
> **Kunde (Customer):** *Nein, habe ich nicht.*  
> **Kassiererin:** *Das macht zusammen 14 Euro 80, bitte.*  
> **Kunde:** *Kann ich mit Karte zahlen?*  
> **Kassiererin:** *Ja, natürlich. Bitte auf das Terminal auflegen.*  
> **Kassiererin:** *Brauchen Sie den Kassenbon?*  
> **Kunde:** *Nein, danke. Schönen Tag noch!*  
> **Kassiererin:** *Danke, gleichfalls! Tschüss!*

### Useful Shopping Phrases
• **Kann ich mit Karte zahlen?** (Can I pay by card?)  
• **Brauchen Sie eine Tüte?** (Do you need a bag?)  
• **Brauchen Sie den Kassenbon / die Quittung?** (Do you need the receipt?)
""",
            "fillIns": [
                {"q": "Brauchen Sie eine ___ (bag)?", "a": "Tüte"},
                {"q": "Kann ich mit ___ (card) zahlen?", "a": "Karte"},
                {"q": "Das macht ___ (together) 12 Euro 50.", "a": "zusammen"},
                {"q": "Ich habe meine ___ (shopping list) dabei.", "a": "Einkaufsliste"},
                {"q": "Wo ist der ___ (bottle deposit) Automat?", "a": "Pfand"}
            ],
            "quiz": [
                {"question": "How do you ask 'Can I pay by card?'", "answer": "Kann ich mit Karte zahlen?", "options": ["Kann ich Karten bezahlen?", "Kann ich mit Karte zahlen?", "Habe ich Karte zahlen?", "Bezahle ich Karte?"]},
                {"question": "What is 'der Kassenbon'?", "answer": "the receipt", "options": ["the shopping bag", "the receipt", "the special offer", "the cash"]},
                {"question": "What does 'Pfand' refer to in Germany?", "answer": "bottle deposit system", "options": ["discount coupon", "bottle deposit system", "membership card", "plastic bag"]},
                {"question": "Translate: 'Brauchen Sie eine Tüte?'", "answer": "Do you need a bag?", "options": ["Do you have a receipt?", "Do you need a bag?", "Do you pay cash?", "Do you have a trolley?"]}
            ],
            "checkpoints": [
                "I know supermarket terms like Pfand, Tüte, Kassenbon, Einkaufswagen",
                "I can ask to pay by card (mit Karte zahlen)",
                "I understand typical cashier questions and greetings",
                "I can conduct a full checkout conversation"
            ],
            "tomorrow": "Week 7 Review and Speaking Practice!"
        },
        {
            "dayNum": 49, "isReview": True, "title": "Week 7 Review & Speaking Practice",
            "reviewCards": [
                {"german": "das Brot / das Fleisch", "english": "bread / meat", "example": "Ich kaufe Brot und Fleisch."},
                {"german": "das Obst / das Gemüse", "english": "fruit / vegetables", "example": "Obst und Gemüse sind gesund."},
                {"german": "der Kaffee / der Tee", "english": "coffee / tea", "example": "Ich möchte einen Kaffee."},
                {"german": "das Wasser / das Bier", "english": "water / beer", "example": "Ein Glas Wasser, bitte."},
                {"german": "möchten (ich möchte)", "english": "would like", "example": "Ich möchte bestellen."},
                {"german": "kaufen / brauchen / nehmen", "english": "buy / need / take", "example": "Ich brauche einen Apfel."},
                {"german": "Accusative masculine", "english": "den / einen / keinen", "example": "einen Apfel, keinen Fisch"},
                {"german": "der Apfel (pl: Äpfel)", "english": "apple", "example": "Ein Kilo Äpfel, bitte."},
                {"german": "ein Kilo / eine Flasche", "english": "a kilo / a bottle (no 'von')", "example": "eine Flasche Wasser"},
                {"german": "Was kostet das?", "english": "How much does that cost?", "example": "Was kostet das Brot?"},
                {"german": "teuer / günstig", "english": "expensive / affordable", "example": "Das Fleisch ist teuer."},
                {"german": "die Kasse", "english": "checkout", "example": "Wo ist die Kasse?"},
                {"german": "mit Karte zahlen", "english": "pay by card", "example": "Kann ich mit Karte zahlen?"},
                {"german": "die Tüte / der Kassenbon", "english": "bag / receipt", "example": "Ich brauche keine Tüte."},
                {"german": "das Pfand", "english": "bottle deposit", "example": "25 Cent Pfand."}
            ],
            "grammarSummary": """
### Week 7 Master Summary

1. **Uncountable / General Food:** No article used when stating general food preferences (*Ich esse Brot, ich trinke Wasser*).
2. **Polite Verb möchten:** *ich möchte, du möchtest, er/sie/es möchte, wir möchten*.
3. **Accusative Case Master Rule:** ONLY masculine changes!
   - Nom: *der / ein / kein / mein*
   - Acc: **den / einen / keinen / meinen**
4. **Quantities:** Do NOT use 'von'! (*ein Kilo Äpfel, eine Flasche Wasser, ein Stück Kuchen*).
5. **Prices & Supermarket:** *Was kostet das?* Prices read: *2,50 € = zwei Euro fünfzig*. Pay by card: *Kann ich mit Karte zahlen?*
""",
            "quiz": [
                {"question": "Accusative form of 'ein Apfel' after kaufen:", "answer": "einen Apfel", "options": ["ein Apfel", "einen Apfel", "eine Apfel", "einem Apfel"]},
                {"question": "Do quantity expressions like 'ein Kilo' take the preposition 'von' in German?", "answer": "no, no preposition", "options": ["yes, use von", "no, no preposition", "yes, use aus", "yes, use mit"]},
                {"question": "How do you ask 'Can I pay by card?'", "answer": "Kann ich mit Karte zahlen?", "options": ["Kann ich mit Karte zahlen?", "Zahle ich mit Karte?", "Kann ich Karte bezahlen?", "Habe ich Karte zahlen?"]},
                {"question": "Conjugate: er + möchten", "answer": "er möchte", "options": ["er möchtet", "er möchte", "er mag", "er möchten"]},
                {"question": "What is 'das Stück'?", "answer": "piece / slice", "options": ["bottle", "kilo", "piece / slice", "bag"]},
                {"question": "How do you say 'How much does that cost?'", "answer": "Was kostet das?", "options": ["Wie viel ist das?", "Was kostet das?", "Was ist der Preis?", "Wie teuer bezahle ich?"]},
                {"question": "What is the article for 'Brot'?", "answer": "das", "options": ["der", "die", "das", "den"]},
                {"question": "What does 'teuer' mean?", "answer": "expensive", "options": ["cheap", "fresh", "expensive", "tasty"]}
            ],
            "speakingPrompt": """
### Speaking Exercise — At the Supermarket / Grocery Store

Read this script aloud and record yourself or practice with a partner:

> *"Guten Tag! Ich brauche ein Kilo Äpfel, eine Flasche Wasser und ein Stück Käse. Was kostet das Kilo Äpfel? 2 Euro 50? Das ist günstig! Ich nehme auch noch ein Brot. Wo ist die Kasse? Ah, danke. Ich möchte gerne mit Karte zahlen. Ich brauche keinen Kassenbon. Vielen Dank und einen schönen Tag!"*
""",
            "checkpoints": [
                "I know 15+ food and drink vocabulary words",
                "I can form accusative masculine objects (einen, keinen, den)",
                "I can state quantity expressions without 'von'",
                "I can conduct a full shopping and checkout conversation"
            ]
        }
    ]
}

print("Week 7 data populated.")
