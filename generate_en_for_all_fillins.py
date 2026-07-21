import re
from run_build_all import all_weeks

# Helper function to generate clean English translation for German A1 fill-in sentences
def get_translation(q_str, ans, full_sent_clean):
    de = re.sub(r'\s*\([^)]*\)', '', full_sent_clean).strip()
    
    # Check parens hint in q_str
    hints = re.findall(r'\(([^)]+)\)', q_str)
    hint = hints[0] if hints else ""
    
    # Common A1 pattern translations
    # Greetings & intro
    if "Wie heißt du" in de: return f"{de} → 'Hello! What is your name?'" if "Hallo" in de else f"'{de}' (What is your name?)"
    if "Ich bin" in de and "Jahre alt" in de: return f"I am {ans} years old."
    if "Wie alt" in de: return "How old are you?"
    if "Deutschland" in de and "aus" in de: return "We are from Germany."
    if "sehr nett" in de: return "You are very nice."
    if "mein Freund" in de: return "He is my friend."
    if "Wie heißen Sie" in de: return "What is your name? (formal)"
    if "Ein Kaffee, bitte" in de: return "A coffee, please."
    if "bis morgen" in de: return "Bye, see you tomorrow!"
    if "Guten Tag" in de: return "Good day! I am Anna."
    if "Guten Abend" in de: return "Good evening! How are you?"
    
    # Generic clean fallback
    return f"Meaning: {de}"

print("Translator logic ready.")
