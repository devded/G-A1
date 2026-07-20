#!/usr/bin/env python3
"""
German A1 Audio Generator - Human-Female Neural TTS
Powered by Microsoft Edge TTS (SeraphinaMultilingualNeural)

VOICE PROFILES:
  seraphina  -> de-DE-SeraphinaMultilingualNeural  (Primary: Modern, natural, Duolingo-like)
  amala      -> de-DE-AmalaNeural                  (Alt: Clear, warm, excellent for learners)
  katja      -> de-DE-KatjaNeural                  (Classic: solid German RP)
  leni       -> de-CH-LeniNeural                   (Swiss variant)

USAGE:
  python3 generate_audio.py               # full run (all 84 days)
  python3 generate_audio.py --week 3      # only Week 3
  python3 generate_audio.py --day 22      # only Day 22
  python3 generate_audio.py --voice amala # use AmalaNeural instead
  python3 generate_audio.py --slow        # generate slow-mode variants too
  python3 generate_audio.py --dry-run     # show what would be generated
  python3 generate_audio.py --manifest-only  # just rebuild manifest.json
"""

import asyncio
import re
import json
import hashlib
import argparse
import sys
from pathlib import Path

# ── Configuration ────────────────────────────────────────────

VOICES = {
    "seraphina": "de-DE-SeraphinaMultilingualNeural",
    "amala":     "de-DE-AmalaNeural",
    "katja":     "de-DE-KatjaNeural",
    "leni":      "de-CH-LeniNeural",
}

DEFAULT_VOICE = "seraphina"
AUDIO_DIR     = Path("public/audio")
MANIFEST_PATH = AUDIO_DIR / "manifest.json"
NORMAL_RATE   = "-5%"
SLOW_RATE     = "-25%"

# ── Helpers ──────────────────────────────────────────────────

def slugify(text):
    if not text:
        return ""
    t = text.lower().strip()
    t = t.replace("ae", "ae2")
    t = t.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    t = t.replace("á","a").replace("é","e").replace("ó","o").replace("ú","u")
    t = re.sub(r"[^a-z0-9]+", "_", t)
    t = t.strip("_")
    if len(t) > 80:
        h = hashlib.md5(text.encode()).hexdigest()[:8]
        t = t[:70] + "_" + h
    return t

def audio_path(text, variant="normal", voice_key=DEFAULT_VOICE):
    slug = slugify(text)
    suffix = "" if variant == "normal" else "_" + variant
    vsuffix = "" if voice_key == DEFAULT_VOICE else "_" + voice_key
    return AUDIO_DIR / f"{slug}{suffix}{vsuffix}.mp3"

# ── Core Generator ───────────────────────────────────────────

async def generate_one(text, out_path, voice_key=DEFAULT_VOICE, rate=NORMAL_RATE, dry_run=False):
    if not text or not text.strip():
        return False
    if out_path.exists():
        return True
    if dry_run:
        print(f"  [DRY] {out_path.name[:60]} <- '{text[:50]}'")
        return True
    try:
        import edge_tts
        voice_name = VOICES.get(voice_key, VOICES[DEFAULT_VOICE])
        comm = edge_tts.Communicate(text, voice_name, rate=rate)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        await comm.save(str(out_path))
        return True
    except Exception as e:
        print(f"  ERR '{text[:35]}': {e}")
        return False

# ── Data Loading ─────────────────────────────────────────────

def load_week1():
    return [{
        "dayNum": 1, "_week": 1, "title": "Greetings and Alphabet",
        "vocab": [
            {"word": "Hallo", "ex": "Hallo! Wie heißt du?"},
            {"word": "Guten Morgen", "ex": "Guten Morgen! Wie geht es Ihnen?"},
            {"word": "Guten Tag", "ex": "Guten Tag, ich bin Anna."},
            {"word": "Guten Abend", "ex": "Guten Abend!"},
            {"word": "Tschüss", "ex": "Tschüss, bis morgen!"},
            {"word": "Auf Wiedersehen", "ex": "Auf Wiedersehen, Frau Müller!"},
            {"word": "Bitte", "ex": "Ein Kaffee, bitte."},
            {"word": "Danke", "ex": "Danke schön!"},
        ]
    }, {
        "dayNum": 2, "_week": 1, "title": "Introducing Yourself",
        "vocab": [
            {"word": "Ich heiße", "ex": "Ich heiße Maria."},
            {"word": "Wie heißen Sie", "ex": "Wie heißen Sie, bitte?"},
            {"word": "Woher kommen Sie", "ex": "Woher kommen Sie?"},
            {"word": "Ich komme aus", "ex": "Ich komme aus Deutschland."},
            {"word": "Wie alt sind Sie", "ex": "Wie alt sind Sie?"},
            {"word": "Ich bin", "ex": "Ich bin dreißig Jahre alt."},
            {"word": "Freut mich", "ex": "Freut mich, Sie kennenzulernen!"},
            {"word": "Ich spreche Deutsch", "ex": "Ich spreche ein bisschen Deutsch."},
        ]
    }, {
        "dayNum": 3, "_week": 1, "title": "Numbers 1 to 20",
        "vocab": [
            {"word": "eins", "ex": "Ich habe eins."},
            {"word": "zwei", "ex": "Zwei Kaffee, bitte."},
            {"word": "drei", "ex": "Drei Äpfel, bitte."},
            {"word": "vier", "ex": "Vier Personen."},
            {"word": "fünf", "ex": "Fünf Euro."},
            {"word": "zehn", "ex": "Zehn Minuten."},
            {"word": "zwanzig", "ex": "Zwanzig Jahre alt."},
            {"word": "null", "ex": "Null Fehler!"},
        ]
    }, {
        "dayNum": 4, "_week": 1, "title": "Days and Colors",
        "vocab": [
            {"word": "Montag", "ex": "Am Montag lerne ich Deutsch."},
            {"word": "Dienstag", "ex": "Am Dienstag gehe ich einkaufen."},
            {"word": "Mittwoch", "ex": "Mittwoch ist mein Lieblingstag."},
            {"word": "Donnerstag", "ex": "Am Donnerstag habe ich frei."},
            {"word": "Freitag", "ex": "Am Freitag gehe ich ins Kino."},
            {"word": "rot", "ex": "Das Auto ist rot."},
            {"word": "blau", "ex": "Der Himmel ist blau."},
            {"word": "grün", "ex": "Das Gras ist grün."},
        ]
    }, {
        "dayNum": 5, "_week": 1, "title": "Articles der die das",
        "vocab": [
            {"word": "der Mann", "ex": "Der Mann heißt Thomas."},
            {"word": "die Frau", "ex": "Die Frau heißt Maria."},
            {"word": "das Kind", "ex": "Das Kind spielt."},
            {"word": "der Tisch", "ex": "Der Tisch ist groß."},
            {"word": "die Tür", "ex": "Die Tür ist offen."},
            {"word": "das Buch", "ex": "Das Buch ist interessant."},
            {"word": "ein Kaffee", "ex": "Ich trinke einen Kaffee."},
            {"word": "eine Flasche", "ex": "Eine Flasche Wasser, bitte."},
        ]
    }, {
        "dayNum": 6, "_week": 1, "title": "sein and haben",
        "vocab": [
            {"word": "ich bin", "ex": "Ich bin müde."},
            {"word": "du bist", "ex": "Du bist nett."},
            {"word": "er ist", "ex": "Er ist Lehrer."},
            {"word": "wir sind", "ex": "Wir sind Freunde."},
            {"word": "ich habe", "ex": "Ich habe Hunger."},
            {"word": "du hast", "ex": "Du hast eine Katze."},
            {"word": "sie hat", "ex": "Sie hat ein Auto."},
            {"word": "wir haben", "ex": "Wir haben Zeit."},
        ]
    }]

def load_all_days(filter_week=None, filter_day=None):
    all_days = []

    # Week 1
    if filter_week is None or filter_week == 1:
        w1_days = load_week1()
        for d in w1_days:
            d["_week"] = 1
        all_days.extend(w1_days)

    for wn in range(2, 13):
        if filter_week and filter_week != wn:
            continue
        try:
            mod = __import__(f"data_w{wn}")
            weeks_to_process = []
            if hasattr(mod, "weeks_data"):
                weeks_to_process.extend(mod.weeks_data)
            elif hasattr(mod, "weeks_3_to_6"):
                weeks_to_process.extend(mod.weeks_3_to_6)
            elif hasattr(mod, f"w{wn}"):
                weeks_to_process.append(getattr(mod, f"w{wn}"))

            for week_dict in weeks_to_process:
                w_num = week_dict.get("weekNum", wn)
                if filter_week and filter_week != w_num:
                    continue
                for d in week_dict.get("days", []):
                    d["_week"] = w_num
                    all_days.append(d)
        except Exception as e:
            print(f"  WARN: Could not load data_w{wn}: {e}")

    if filter_day:
        all_days = [d for d in all_days if d.get("dayNum") == filter_day]

    return all_days

def collect_texts(all_days, include_slow=False):
    items = []
    seen = set()

    def add(text, variant="normal"):
        t = (text or "").strip()
        if not t:
            return
        k = (t, variant)
        if k in seen:
            return
        seen.add(k)
        items.append((t, variant))

    for day in all_days:
        is_review = day.get("isReview", False)

        if is_review:
            for card in day.get("reviewCards", []):
                add(card.get("german", ""))
                add(card.get("example", ""))
                if include_slow:
                    add(card.get("german", ""), "slow")
        else:
            for v in day.get("vocab", []):
                art  = v.get("article", "").strip() if isinstance(v, dict) else ""
                word = (v.get("word", "") if isinstance(v, dict) else str(v)).strip()
                if art and not word.startswith(art):
                    full = f"{art} {word}"
                else:
                    full = word
                ex   = v.get("ex", "") if isinstance(v, dict) else ""
                add(full)
                add(ex)
                if include_slow:
                    add(full, "slow")
                    add(ex, "slow")

        for q in day.get("quiz", []):
            add(q.get("question", ""))
            add(q.get("answer", ""))
            for opt in q.get("options", []):
                add(opt)

    # Scan all Day markdown files for explicit <SpeakButton text="..." /> tags (e.g. Grammar section examples)
    import glob, re
    md_files = glob.glob("Weeks/Week-*/Days/Day-*.md")
    for fpath in md_files:
        try:
            content = open(fpath, encoding="utf-8").read()
            matches = re.findall(r'<SpeakButton\s+(?:[^>]*?\s+)?text=["\']([^"\']+)["\']', content)
            for m in matches:
                add(m)
                if include_slow:
                    add(m, "slow")
        except Exception:
            pass

    return items

# ── Manifest ─────────────────────────────────────────────────

def build_and_save_manifest():
    manifest = {}
    for mp3 in sorted(AUDIO_DIR.glob("*.mp3")):
        manifest[mp3.stem] = f"/audio/{mp3.name}"
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"Manifest: {MANIFEST_PATH} ({len(manifest)} entries)")
    return manifest

# ── Main ─────────────────────────────────────────────────────

async def run(args):
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    voice_key    = args.voice
    include_slow = args.slow
    dry_run      = args.dry_run
    filter_week  = args.week
    filter_day   = args.day

    print(f"\nGerman A1 Audio Generator")
    print(f"  Voice : {VOICES[voice_key]}")
    print(f"  Rate  : {NORMAL_RATE}  (slow: {SLOW_RATE})")
    print(f"  Output: {AUDIO_DIR.resolve()}\n")

    all_days = load_all_days(filter_week, filter_day)
    texts    = collect_texts(all_days, include_slow)

    print(f"Days: {len(all_days)}  |  Audio items: {len(texts)}\n")

    done = skipped = errors = 0
    total = len(texts)

    for i, (text, variant) in enumerate(texts, 1):
        rate = SLOW_RATE if variant == "slow" else NORMAL_RATE
        path = audio_path(text, variant, voice_key)

        if path.exists():
            skipped += 1
            continue

        ok = await generate_one(text, path, voice_key, rate, dry_run)
        if ok:
            done += 1
            if done <= 5 or done % 25 == 0:
                print(f"  [{i}/{total}] OK: {path.name[:55]}")
        else:
            errors += 1
            print(f"  [{i}/{total}] ERR: {text[:40]}")

        if not dry_run and done % 30 == 0:
            await asyncio.sleep(0.5)

    print(f"\nDone={done}  Skipped={skipped}  Errors={errors}")

    if not dry_run:
        build_and_save_manifest()
        print(f"Total MP3 files: {len(list(AUDIO_DIR.glob('*.mp3')))}")
    print("\nAudio generation complete!")

def main():
    p = argparse.ArgumentParser(description="German A1 Neural Audio Generator")
    p.add_argument("--week",          type=int, default=None)
    p.add_argument("--day",           type=int, default=None)
    p.add_argument("--voice",         default=DEFAULT_VOICE, choices=list(VOICES.keys()))
    p.add_argument("--slow",          action="store_true")
    p.add_argument("--dry-run",       action="store_true", dest="dry_run")
    p.add_argument("--manifest-only", action="store_true", dest="manifest_only")
    args = p.parse_args()

    if args.manifest_only:
        build_and_save_manifest()
        return

    asyncio.run(run(args))

if __name__ == "__main__":
    main()
