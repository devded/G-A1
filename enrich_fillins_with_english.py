import re, glob

# Let's inspect how fillIns are stored in Day-01.md to Day-84.md
day_files = sorted(glob.glob('Weeks/Week-*/Days/Day-*.md'))

updated_count = 0

for filepath in day_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match fillIn lines in markdown
    # Format: **1.** ___! Wie heißt du? → <details><summary>Answer</summary>**Hallo** <SpeakButton text="Hallo! Wie heißt du?" /></details>
    lines = content.split('\n')
    new_lines = []
    modified = False
    
    for line in lines:
        if line.startswith('**') and '→ <details><summary>Answer</summary>' in line and '<span class="ans-meaning">' not in line:
            # Extract full_sent_clean from SpeakButton
            match = re.search(r'<SpeakButton text="([^"]+)" />', line)
            if match:
                full_sent = match.group(1)
                # Create clean English translation based on full_sent and question text
                # Extract question part
                q_part = line.split('→')[0].strip()
                # Remove **1.**
                q_part = re.sub(r'^\*\*\d+\.\*\*\s*', '', q_part)
                
                # Check for English hint in parens in q_part e.g. ___ (On) Montag... -> On
                hints = re.findall(r'\(([^)]+)\)', q_part)
                
                # Construct simple English translation
                # Let's clean full_sent
                clean_de = re.sub(r'\s*\([^)]*\)', '', full_sent).strip()
                
                # We can generate a readable English translation placeholder or exact translation
                # Example: for "Am Montag habe ich Deutschunterricht." -> "On Monday I have German class."
                # Add english translation span before </details>
                # E.g. <br/><span class="ans-meaning">"{clean_de}"</span>
            new_lines.append(line)
        else:
            new_lines.append(line)

print("Check completed.")
