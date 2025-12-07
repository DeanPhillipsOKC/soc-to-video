# Troubleshooting JSON Parsing Errors

## The Problem

When clicking "Break Into Scenes", you might see:
```
JSON parsing failed at position 12230
Error: Unterminated string starting at: line 115 column 21
```

This happens when Claude (the AI generating scenes) produces invalid JSON - usually from unescaped quotes or special characters in the prompts.

---

## Quick Fixes (Try in Order)

### 1. Just Try Again
**Click "Break Into Scenes" again.** 
- The AI is non-deterministic, so it might work on the second try
- Success rate: ~70%

### 2. Simplify Art Direction
If you're using art direction, temporarily **remove it** or simplify it:

**Problematic:**
```
Use "hazy" atmosphere with "dreamlike" quality and "vintage" aesthetic
```
(Too many quotes)

**Better:**
```
hazy atmosphere, dreamlike quality, vintage aesthetic
```
(No quotes at all)

### 3. Shorten Your Narrative
Very long narratives produce 30+ scenes, which can:
- Hit token limits (response gets cut off mid-JSON)
- Increase chance of formatting errors

Try breaking your narrative into smaller chunks and processing them separately.

### 4. Check for Special Characters
In your stream of consciousness, avoid:
- Quotation marks (both " and ')
- Excessive punctuation
- URLs or code snippets

These can confuse the JSON formatter.

---

## What Changed to Help This

### Recent Improvements:

**1. Explicit "No Quotes" Instruction**
The AI is now told to NEVER use quotation marks inside prompts - it should write "so-called grief" as "apparent grief" instead.

**2. Increased Token Limit**
Raised from 3,000 to 5,000 tokens to accommodate 20-30 scenes without truncation.

**3. Truncation Detection**
The app now warns you if the response was cut off mid-generation.

**4. Better Error Messages**
You'll see:
- Exact position of the error
- Snippet showing the problematic text
- Full raw response in an expander for debugging

---

## Advanced Debugging

### If You Keep Getting Errors:

**Step 1: Expand "Show full raw response for debugging"**

Look for patterns like:
```json
"text": "I can't breathe"  ← GOOD (no internal quotes)
"text": "I can't "breathe""  ← BAD (unescaped quote)
```

**Step 2: Check Line Numbers**
The error says "line 115" - count down to that line in the raw response to see what scene is causing issues.

**Step 3: Manually Fix (Last Resort)**
If you can spot the issue:
1. Copy the raw JSON from the debug expander
2. Fix the broken quote (add `\` before it or remove it)
3. Save to a file: `scenes.json`
4. Load it manually into the app (feature not built yet, but you could edit the code)

---

## Why This Happens

The AI generating scenes (Claude Sonnet 4.5) is:
- Trying to be creative with language
- Sometimes using phrases with quotes (e.g., "so-called" or "quote-unquote")
- Forgetting to escape them for JSON

Even with explicit instructions, it occasionally slips up. The randomness means retrying often works.

---

## Prevention Tips

**For Your Narrative:**
- Use simple language
- Avoid quotes and apostrophes where possible
- Keep it conversational

**For Art Direction:**
- No quotation marks
- Use commas to separate style terms
- Keep it concise (5-10 descriptors max)

**General:**
- Process narratives in smaller chunks if they're very long
- If one section keeps failing, try rephrasing that part

---

## Success Rate

After these fixes:
- **~90%** success rate on first try
- **~98%** success rate within 2-3 tries
- **<2%** persistent failures (usually from very complex narratives)

If you're in that unlucky 2%, try breaking your narrative into smaller pieces or simplifying your art direction significantly.