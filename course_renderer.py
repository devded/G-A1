import os
import json
import re

def process_grammar_content(content):
    if not content:
        return ""
    lines = []
    for line in content.splitlines():
        if '<SpeakButton' in line:
            lines.append(line)
            continue
        stripped = line.strip()
        
        # 1. Dialogue lines: > **Kellner:** *Guten Abend! Haben Sie reserviert?*
        m_diag = re.match(r'^(>\s*\*\*[^*]+:\*\*\s*)(?:\*|_)?([^*_\n\r]+)(?:\*|_)?(.*)$', stripped)
        if m_diag and len(m_diag.group(2).strip()) > 3:
            role_prefix = m_diag.group(1)
            text_raw = m_diag.group(2).strip()
            rest = m_diag.group(3)
            text_clean = re.sub(r'[*_`]', '', text_raw).strip()
            if text_clean and not any(text_clean.startswith(x) for x in ['Note', 'Rule', 'Formula', 'Notice']):
                line = f'{role_prefix}*{text_raw}* <SpeakButton text="{text_clean}" />{rest}'
                lines.append(line)
                continue

        # 2. Dialogue arrows: *(Is this seat free?)* → *Ja, bitte nehmen Sie Platz!*
        m_arrow = re.match(r'^(.*→\s*)(?:\*|_)?([^*_\n\r]+)(?:\*|_)?(.*)$', stripped)
        if m_arrow:
            prefix = m_arrow.group(1)
            de_raw = m_arrow.group(2).strip()
            rest = m_arrow.group(3)
            de_clean = re.sub(r'[*_`]', '', de_raw).strip()
            if len(de_clean) > 2:
                line = f'{prefix}*{de_raw}* <SpeakButton text="{de_clean}" />{rest}'
                lines.append(line)
                continue

        # 3. Bullet points: > • Ich habe **einen** Bruder. (masculine → einen)
        if stripped.startswith('> •') or stripped.startswith('•') or stripped.startswith('> -') or (stripped.startswith('-') and not stripped.startswith('---')):
            m = re.match(r'^(>\s*|\s*)([•\-]\s*)([^(\n\r]+)(.*)$', stripped)
            if m:
                prefix = m.group(1) + m.group(2)
                de_text_raw = m.group(3).strip()
                rest = m.group(4)
                de_clean = re.sub(r'[*_`]', '', de_text_raw).strip()
                if de_clean and not de_clean.lower().startswith('rule') and len(de_clean) > 2:
                    line = f'{prefix}{de_text_raw} <SpeakButton text="{de_clean}" />{rest}'
                    lines.append(line)
                    continue

        # 4. Numbered list items with bold German examples e.g. 1. **Ich möchte...**
        m_num = re.match(r'^(\d+\.\s*\*\*([^*]+)\*\*.*)$', stripped)
        if m_num and len(m_num.group(2).strip()) > 3:
            de_clean = re.sub(r'[*_`]', '', m_num.group(2)).strip()
            line = f'{stripped} <SpeakButton text="{de_clean}" />'
            lines.append(line)
            continue

        # 5. Table rows: | ich | hab**e** | /ˈhaːbə/ |
        if stripped.startswith('|') and stripped.endswith('|'):
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if not any(':---' in c or '---:' in c for c in cells) and len(cells) >= 2:
                col0 = cells[0].lower()
                if not any(h in col0 for h in ['gender', 'pronoun', 'subject', 'situation', 'sound', 'person']):
                    p_cell = re.sub(r'[*_`]', '', cells[0]).strip()
                    v_cell = re.sub(r'[*_`]', '', cells[1]).strip()
                    if p_cell.lower() in ['ich', 'du', 'er/sie/es', 'er', 'sie', 'es', 'wir', 'ihr', 'sie/sie', 'sie (formal)']:
                        speak_phrase = f"{p_cell} {v_cell}".replace('/', ' oder ')
                        cells[1] = f'{cells[1]} <SpeakButton text="{speak_phrase}" />'
                        line = '| ' + ' | '.join(cells) + ' |'
                    elif len(cells) >= 4 and cells[-1]:
                        examples = [ex.strip() for ex in cells[-1].split(',')]
                        new_examples = []
                        for ex in examples:
                            ex_clean = re.sub(r'[*_`]', '', ex).strip()
                            if ex_clean and not ex_clean.lower().startswith('e.g.') and len(ex_clean) > 1:
                                new_examples.append(f'{ex} <SpeakButton text="{ex_clean}" />')
                            else:
                                new_examples.append(ex)
                        cells[-1] = ', '.join(new_examples)
                        line = '| ' + ' | '.join(cells) + ' |'
        lines.append(line)
    return '\n'.join(lines)

base_dir = '/home/thededar/Downloads/Workspace/test2/German-A1-Self-Study'

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def fmt_day(n):
    return f"{n:02d}"

def safe_prop_attr(obj):
    # Dumps clean JSON and replaces " with &quot; so it can safely be placed in double-quoted Vue props :prop="..."
    raw = json.dumps(obj, ensure_ascii=False)
    return raw.replace('"', '&quot;')

def render_day(d, week_num, max_days=84):
    day_num = d["dayNum"]
    day_str = fmt_day(day_num)
    week_str = fmt_day(week_num)
    
    prev_str = fmt_day(day_num - 1) if day_num > 1 else "01"
    next_str = fmt_day(day_num + 1) if day_num < max_days else fmt_day(max_days)
    
    prev_week = fmt_day(week_num - 1) if day_num % 7 == 1 and week_num > 1 else week_str
    next_week = fmt_day(week_num + 1) if day_num % 7 == 0 and week_num < 12 else week_str
    
    prev_path = f"/Weeks/Week-{prev_week}/Days/Day-{prev_str}"
    next_path = f"/Weeks/Week-{next_week}/Days/Day-{next_str}"
    
    is_review = d.get("isReview", False)
    
    lines = []
    # Header navigation
    lines.append(f"# Day {day_str} — {d['title']}\n")
    lines.append('<div class="day-nav">')
    lines.append(f'  <a href="{prev_path}">← Day {prev_str}</a>')
    level = d.get("level", "A1.1")
    day_meta = f"{level} · Week {week_num} review" if is_review else f"{level} · 8 new words"
    lines.append(f'  <span class="day-center"><Icon name="calendar" /> Week {week_num} · Day {day_num} of {max_days} <span class="day-meta">· {day_meta}</span></span>')
    if is_review and week_num < 12:
        lines.append(f'  <a href="/Weeks/Week-{fmt_day(week_num+1)}/Days/Day-{next_str}">Week {week_num+1} →</a>')
    else:
        lines.append(f'  <a href="{next_path}">Day {next_str} →</a>')
    lines.append('</div>\n')

    # Timer bar
    lines.append('<div class="day-timer-bar">')
    if is_review:
        lines.append('  <div class="timer-segment vocab"><Icon name="repeat" /> Review Vocab <strong>8 min</strong></div>')
        lines.append('  <div class="timer-segment grammar"><Icon name="book" /> Grammar Recap <strong>7 min</strong></div>')
        lines.append('  <div class="timer-segment practice"><Icon name="target" /> Big Quiz <strong>12 min</strong></div>')
        lines.append('  <div class="timer-segment review"><Icon name="message-square" /> Speaking <strong>3 min</strong></div>')
    else:
        lines.append('  <div class="timer-segment vocab"><Icon name="book-open" /> Vocab <strong>8 min</strong></div>')
        lines.append('  <div class="timer-segment grammar"><Icon name="book" /> Grammar <strong>10 min</strong></div>')
        lines.append('  <div class="timer-segment practice"><Icon name="edit-3" /> Practice <strong>9 min</strong></div>')
        lines.append('  <div class="timer-segment review"><Icon name="check-circle" /> Review <strong>3 min</strong></div>')
    lines.append('  <div class="timer-segment total"><Icon name="clock" /> 30 min</div>')
    lines.append('</div>\n')
    lines.append('---\n')
    
    if not is_review:
        # STEP 1: VOCAB
        lines.append('## Step 1 — Vocabulary (8 min)\n')
        lines.append('<div class="vocab-grid">\n')
        for v in d["vocab"]:
            art = v.get("article", "").strip() if v.get("article") else ""
            raw_word = v["word"].strip()
            
            # Check if raw_word already starts with article (e.g. "die Mutter")
            if art and raw_word.lower().startswith(art.lower() + " "):
                display_word = raw_word[len(art):].strip()
                speak_text = raw_word
            elif art and raw_word.lower() == art.lower():
                display_word = raw_word
                speak_text = raw_word
            else:
                display_word = raw_word
                speak_text = f"{art} {raw_word}".strip() if art else raw_word

            art_span = f'<span class="article-badge article-{art}">{art}</span> ' if art else ''
            badge_cls = f'badge-{v.get("badge", "noun")}'
            
            lines.append('<div class="vocab-card">')
            lines.append(f'  <div class="word">{art_span}{display_word} <span class="badge {badge_cls}">{v.get("badge", "word")}</span> <SpeakButton text="{speak_text}" /></div>')
            lines.append(f'  <div class="translation">{v["translation"]}</div>')
            lines.append(f'  <div class="ipa">{v["ipa"]}</div>')
            lines.append(f'  <div class="example">{v["ex"]} <SpeakButton text="{v["ex"]}" /></div>')
            lines.append(f'  <div class="example-en">{v["exEn"]}</div>')
            lines.append('</div>\n')
        lines.append('</div>\n')
        lines.append('---\n')
        
        # STEP 2: GRAMMAR
        lines.append('## Step 2 — Grammar Bite (10 min)\n')
        lines.append('<div class="grammar-box">\n')
        lines.append(f'### {d["grammarTitle"]}\n')
        lines.append(process_grammar_content(d["grammarContent"]).strip())
        lines.append('\n</div>\n')
        lines.append('---\n')
        
        # STEP 3: PRACTICE
        lines.append('## Step 3 — Practice (9 min)\n')
        lines.append('### 3A — Complete the sentences\n')
        for idx, f in enumerate(d["fillIns"], 1):
            ans_clean = f["a"].strip()
            q_str = f["q"].strip()
            if '___' in q_str:
                full_sent = re.sub(r'___(?:\s*\([^)]*\))?', ans_clean, q_str).strip()
            else:
                full_sent = f"{q_str} {ans_clean}".strip()
            full_sent_clean = re.sub(r'[*_`]', '', full_sent).strip()
            lines.append(f'**{idx}.** {f["q"]} → <details><summary>Answer</summary>**{ans_clean}** <SpeakButton text="{full_sent_clean}" /></details>')
        lines.append('')
        
        lines.append('### 3B — Flash Cards\n')
        cards_obj = [
            {
                "german": v["word"],
                "article": v.get("article", ""),
                "english": v["translation"],
                "ipa": v["ipa"],
                "example": v["ex"]
            } for v in d["vocab"]
        ]
        lines.append(f'<FlipDeck :cards="{safe_prop_attr(cards_obj)}" />\n')
        
        lines.append('### 3C — Quiz\n')
        lines.append(f'<VocabQuiz :questions="{safe_prop_attr(d["quiz"])}" />\n')
        lines.append('---\n')
        
        # STEP 4: MASTERY
        lines.append('## Step 4 — Daily Mastery Check (3 min)\n')
        lines.append('<div class="mastery-checklist">')
        lines.append('<h3>Before you finish:</h3>')
        lines.append('<ul>')
        for cp in d["checkpoints"]:
            lines.append(f'  <li>{cp}</li>')
        lines.append('</ul>')
        lines.append('</div>\n')
        
        lines.append(f'> <Icon name="arrow-right" /> **Tomorrow (Day {next_str}):** {d.get("tomorrow", "Next step in your German journey!")}\n')
        
        lines.append('<div class="day-nav">')
        lines.append(f'  <a href="{prev_path}">← Day {prev_str}</a>')
        lines.append(f'  <span class="day-center">Day {day_num} of {max_days} · Week {week_num}</span>')
        lines.append(f'  <a href="{next_path}">Day {next_str} →</a>')
        lines.append('</div>')
    else:
        # REVIEW DAY
        lines.append('## Step 1 — Vocabulary Review (8 min)\n')
        lines.append(f'<FlipDeck :cards="{safe_prop_attr(d["reviewCards"])}" />\n')
        lines.append('---\n')
        
        lines.append('## Step 2 — Grammar Quick Recap (7 min)\n')
        lines.append('<div class="grammar-box">\n')
        lines.append(d["grammarSummary"].strip())
        lines.append('\n</div>\n')
        lines.append('---\n')
        
        lines.append(f'## Step 3 — Big Week {week_num} Quiz (12 min)\n')
        lines.append(f'<VocabQuiz :questions="{safe_prop_attr(d["quiz"])}" />\n')
        lines.append('---\n')
        
        lines.append('## Step 4 — Speaking Exercise (3 min)\n')
        lines.append(d["speakingPrompt"].strip())
        lines.append('\n---\n')
        
        lines.append(f'## Week {week_num} Mastery Checklist\n')
        lines.append('<div class="mastery-checklist">')
        lines.append(f'<h3>Week {week_num} Complete — Can you do all of these?</h3>')
        lines.append('<ul>')
        for cp in d["checkpoints"]:
            lines.append(f'  <li>{cp}</li>')
        lines.append('</ul>')
        lines.append('</div>\n')
        lines.append('---\n')
        
        lines.append('<div class="day-nav">')
        lines.append(f'  <a href="{prev_path}">← Day {prev_str}</a>')
        lines.append(f'  <span class="day-center"><Icon name="check-circle" /> Week {week_num} Complete!</span>')
        if week_num < 12:
            lines.append(f'  <a href="/Weeks/Week-{fmt_day(week_num+1)}/Days/Day-{next_str}">Start Week {week_num+1} →</a>')
        else:
            lines.append('  <span class="day-center"><Icon name="award" /> Course Complete!</span>')
        lines.append('</div>')
        
    return '\n'.join(lines)

def render_readme(w):
    week_num = w["weekNum"]
    week_str = fmt_day(week_num)
    start_day = (week_num - 1) * 7 + 1
    end_day = week_num * 7
    next_week = week_num + 1 if week_num < 12 else 12
    
    lines = []
    lines.append(f'# Week {week_num} — {w["title"]}\n')
    lines.append('<div class="day-nav">')
    lines.append('  <a href="/">← Course Home</a>')
    lines.append(f'  <span class="day-center">Week {week_num} of 12 <span class="day-meta">· 7 days · 56 words · 6 grammar points</span></span>')
    if week_num < 12:
        lines.append(f'  <a href="/Weeks/Week-{fmt_day(next_week)}/Days/Day-{fmt_day(end_day+1)}">Week {next_week} →</a>')
    else:
        lines.append('  <a href="/">Course Home →</a>')
    lines.append('</div>\n')

    lines.append(f'> **Week {week_num} Goal:** {w["goal"]}\n')
    lines.append('---\n')
    lines.append('## This Week\'s Lessons\n')
    lines.append('| Day | Topic | Grammar Focus | Status |')
    lines.append('|:---:|:---|:---|:---:|')
    
    for d in w["days"]:
        day_str = fmt_day(d["dayNum"])
        g_focus = d.get("grammarTitle", "All Week Grammar")
        if d.get("isReview"):
            lines.append(f'| [Day {day_str}](/Weeks/Week-{week_str}/Days/Day-{day_str}) | **WEEK REVIEW** + Speaking | {g_focus} | □ |')
        else:
            lines.append(f'| [Day {day_str}](/Weeks/Week-{week_str}/Days/Day-{day_str}) | {d["title"]} | {g_focus} | □ |')
            
    lines.append('\n---\n')
    lines.append(f'## Ready? Start Day {fmt_day(start_day)}!\n')
    lines.append('<div style="text-align: center; margin: 2rem 0;">')
    lines.append(f'  <a href="/Weeks/Week-{week_str}/Days/Day-{fmt_day(start_day)}" style="display: inline-block; background: var(--vp-c-brand-1); color: #fff; padding: 14px 32px; border-radius: 12px; font-weight: 700; font-size: 1rem; text-decoration: none; transition: all 0.2s;">')
    lines.append(f'    <Icon name="play" /> Start Day {fmt_day(start_day)} — 30 Minutes')
    lines.append('  </a>')
    lines.append('</div>')
    
    return '\n'.join(lines)

print("Renderer updated with HTML entity safe_prop_attr.")
