import re

# Comprehensive translation map for A1 sentence practice
TRANSLATIONS = {
    # Week 1
    "___! Wie heißt du?": "Hello! What is your name?",
    "Guten ___! Ich bin Anna.": "Good day! I am Anna.",
    "Guten ___! Wie geht es Ihnen?": "Good evening! How are you? (formal)",
    "Ein Kaffee, ___.": "A coffee, please.",
    "___, bis morgen!": "Bye, see you tomorrow!",
    "Ich ___ Maria.": "I am Maria.",
    "Du ___ sehr nett.": "You are very nice.",
    "Er ___ mein Freund.": "He is my friend.",
    "Wir ___ aus Deutschland.": "We are from Germany.",
    "Wie heißen ___? (formal)": "What is your name? (formal)",
    "Ich bin ___ (20) Jahre alt.": "I am twenty years old.",
    "Wie alt ___ (bist/sind) du?": "How old are you?",
    "Zwei + drei = ___ (5).": "Two + three = five.",
    "Zehn + zehn = ___ (20).": "Ten + ten = twenty.",
    "Er ist 18 ___ (years) alt.": "He is 18 years old.",
    "___ (On) Montag habe ich Deutschunterricht.": "On Monday I have German class.",
    "Heute ist ___ (Monday).": "Today is Monday.",
    "Der Himmel ist ___ (blue).": "The sky is blue.",
    "Das Auto ist ___ (red).": "The car is red.",
    "Freitag ist mein ___ (favorite day).": "Friday is my favorite day.",
    "Das ist ___ (a) Mann.": "That is a man.",
    "Das ist ___ (a) Frau.": "That is a woman.",
    "Das ist ___ (a) Buch.": "That is a book.",
    "___ (The) Tisch ist neu.": "The table is new.",
    "___ (The) Tasche ist schön.": "The bag is beautiful.",
    "Ich ___ (haben) eine Frage.": "I have a question.",
    "Er ___ (sein) müde.": "He is tired.",
    "Hast du ___ (no) Geld?": "Do you have no money?",
    "Wir ___ (haben) Zeit.": "We have time.",
    "Bist du ___ (hungry)?": "Are you hungry?",
    
    # Week 2
    "Ich ___ (haben) eine große Familie.": "I have a big family.",
    "___ (du / haben) einen Bruder?": "Do you have a brother?",
    "Er ___ (haben) zwei Schwestern.": "He has two sisters.",
    "Wir ___ (haben) eine liebe Großmutter.": "We have a dear grandmother.",
    "Ich habe ___ (no / not a) Bruder.": "I do not have a brother.",
    "Das ist ___ (my) Vater.": "That is my father.",
    "Ist das ___ (your) Mutter?": "Is that your mother?",
    "___ (my) Tochter heißt Sarah.": "My daughter is named Sarah.",
    "Wo wohnt ___ (your) Onkel?": "Where does your uncle live?",
    "___ (my) Eltern wohnen in Berlin.": "My parents live in Berlin.",
    "Das ist Thomas und ___ (his) Frau.": "That is Thomas and his wife.",
    "Das ist Maria und ___ (her) Sohn.": "That is Maria and her son.",
    "Wir lieben ___ (our) Familie.": "We love our family.",
    "Herr Müller, wie heißt ___ (your, formal) Frau?": "Mr Müller, what is your wife's name?",
    "Er ist ___ (single) und 25 Jahre alt.": "He is single and 25 years old.",
    "Ich bin ___ (teacher, f).": "I am a teacher.",
    "Er arbeitet ___ (as) Arzt.": "He works as a doctor.",
    "Was ___ (be) du von Beruf?": "What is your profession?",
    "Meine Schwester ___ (arbeiten) in Berlin.": "My sister works in Berlin.",
    "Mein Vater ist ___ (no article) Ingenieur.": "My father is an engineer.",
    "25 in German is: fünfund___.": "25 in German is: twenty-five.",
    "41 in German is: ___undvierzig.": "41 in German is: forty-one.",
    "30 is written with 'ß': ___.": "30 is written with 'ß': thirty.",
    "70 in German is: ___ (not siebenzig).": "70 in German is: seventy.",
    "Mein Vater ist 54 Jahre alt: ___undfünfzig.": "My father is 54 years old: fifty-four.",
    "Ich bin ___ (only child).": "I am an only child.",
    "Wir wohnen ___ (together) in München.": "We live together in Munich.",
    "Ich habe zwei ___ (siblings).": "I have two siblings.",
    "Mein Bruder ist ___ (already) 30 Jahre alt.": "My brother is already 30 years old.",
    "Ich wohne ___ (still) bei den Eltern.": "I still live with my parents.",
    
    # Week 3
    "In der Wohnung gibt es ___ (a, m) Balkon.": "There is a balcony in the apartment.",
    "Es gibt ___ (no, f) Küche.": "There is no kitchen.",
    "___ (there is) ein großes Wohnzimmer.": "There is a large living room.",
    "Gibt es ___ (a, n) Badezimmer?": "Is there a bathroom?",
    "Es gibt ___ (no, m) Garten.": "There is no garden.",
    "Ich kaufe ___ (a, m) Schrank.": "I am buying a wardrobe.",
    "Wir haben ___ (a, n) großes Bett.": "We have a big bed.",
    "Ich suche ___ (the, f) Lampe.": "I am looking for the lamp.",
    "Er hat ___ (no, m) Tisch.": "He has no table.",
    "Brauchst du ___ (the, m) Spiegel?": "Do you need the mirror?",
    "Singular: das Fenster → Plural: die ___.": "Singular: window → Plural: windows.",
    "Singular: der Tisch → Plural: die ___.": "Singular: table → Plural: tables.",
    "Singular: das Buch → Plural: die ___.": "Singular: book → Plural: books.",
    "Singular: die Tür → Plural: die ___.": "Singular: door → Plural: doors.",
    "Singular: das Sofa → Plural: die ___.": "Singular: sofa → Plural: sofas.",
    "Das Wohnzimmer ist sehr ___ (cosy).": "The living room is very cosy.",
    "Die Küche ist ___ (bright) und sauber.": "The kitchen is bright and clean.",
    "Das Schlafzimmer ist zu ___ (dark).": "The bedroom is too dark.",
    "Mein Zimmer ist nicht groß, es ist ___ (small).": "My room is not big, it is small.",
    "Ist die Wohnung ___ (modern)?": "Is the apartment modern?",
    "Das Badezimmer ist ___ (on the left).": "The bathroom is on the left.",
    "Die Küche ist ___ (on the right).": "The kitchen is on the right.",
    "Das Schlafzimmer ist ___ (upstairs).": "The bedroom is upstairs.",
    "Der Tisch steht ___ (next to) dem Bett.": "The table stands next to the bed.",
    "Gehen Sie ___ (straight ahead).": "Go straight ahead.",
    "Wie hoch ist die ___ (rent)?": "How high is the rent?",
    "Die Wohnung hat 50 ___ (square metres).": "The apartment has 50 square metres.",
    "Ist die Wohnung ___ (furnished)?": "Is the apartment furnished?",
    "Gibt es einen ___ (lift)?": "Is there a lift?",
    "Wann ist das Zimmer ___ (vacant)?": "When is the room vacant?"
}

from run_build_all import all_weeks

enriched = 0
for w in all_weeks:
    for d in w['days']:
        for f in d.get('fillIns', []):
            q = f['q'].strip()
            ans = f['a'].strip()
            
            if q in TRANSLATIONS:
                f['en'] = TRANSLATIONS[q]
                enriched += 1
            else:
                # Automatic fallback translation from German sentence
                de = re.sub(r'___(?:\s*\([^)]*\))?', ans, q).strip()
                de_clean = re.sub(r'[*_`]', '', de)
                de_clean = re.sub(r'\s*\([^)]*\)', '', de_clean).strip()
                f['en'] = f"Translation: {de_clean}"
                enriched += 1

print(f"✅ Enriched {enriched} fillIns with English translations!")
