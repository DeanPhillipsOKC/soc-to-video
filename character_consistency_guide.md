# Character Consistency & Prompt Editing Guide

## The Problem You Reported

**Issue:** Character descriptions were being paraphrased/summarized, causing inconsistent appearance across images.

**Example:**
- **Character info:** "Dean: Moderately heavy-set man in his late 40s with short black hair and short black unkempt beard, black-framed glasses"
- **Bad prompt:** "Man in his 50s standing by window" ❌
  - Changed age (40s → 50s)
  - Lost all physical details
  - Character looks different in every image

---

## What's Fixed

### 1. **VERBATIM Character Descriptions**

The AI now receives explicit instructions to use character descriptions **WORD-FOR-WORD**:

```
CRITICAL INSTRUCTIONS FOR CHARACTER CONSISTENCY:
- When a scene mentions a character, use their COMPLETE description VERBATIM
- DO NOT paraphrase, summarize, or abbreviate character descriptions
- DO NOT change ages, physical features, or any details
- Copy the ENTIRE character description directly into the prompt
```

**Example of correct usage:**
```
Character info: "Dean: Moderately heavy-set man in his late 40s with short black hair and short black unkempt beard, black-framed glasses"

Correct prompt: "Moderately heavy-set man in his late 40s with short black hair and short black unkempt beard, black-framed glasses standing by window, contemplative mood"
```

All the details stay intact → more consistent character appearance.

---

## New Feature: Prompt Editing

### Individual Scene Editing

**For each scene, you can now:**

1. Click **"✏️ Edit Prompt"** button
2. Modify the prompt text
3. Click **"💾 Save"** or **"❌ Cancel"**

**Use cases:**
- Fix character descriptions that got mangled
- Add more specific details
- Remove something that doesn't fit
- Adjust style keywords

**Example workflow:**
```
Original prompt: "Man in his 50s with beard standing by window"
↓
Click "Edit Prompt"
↓
Change to: "Moderately heavy-set man in his late 40s with short black hair 
and short black unkempt beard, black-framed glasses standing by window, 
muted colors, soft focus"
↓
Save
```

---

### Bulk Editing (Find/Replace)

**For changes across ALL scenes:**

1. Expand **"⚙️ Bulk Operations"**
2. Enter text to find
3. Enter replacement text
4. Click **"🔄 Replace in All Prompts"**

**Use cases:**

**Example 1: Fix a consistent character error**
```
Find: "man in his 50s"
Replace: "moderately heavy-set man in his late 40s with short black hair and short black unkempt beard, black-framed glasses"
→ Updates all 12 scenes at once
```

**Example 2: Add style consistently**
```
Find: "."
Replace: ". Style: hazy atmosphere, muted colors, dreamlike soft focus"
→ Appends style to every prompt ending with period
```

**Example 3: Remove unwanted element**
```
Find: "vibrant colors, "
Replace: ""
→ Removes vibrant colors from all prompts
```

---

## Complete Workflow for Character Consistency

### Step 1: Write Detailed Character Descriptions
```
Dean: Moderately heavy-set man in his late 40s with short black hair, 
short black unkempt beard, black-framed glasses, typically wearing 
dark casual clothing

Kristina: [complete physical description]

Sophia: 3-year-old girl with [complete description]
```

**Tips:**
- Be specific about age, build, hair, facial features
- Include clothing if relevant
- Write exactly how you want it to appear in prompts

### Step 2: Generate Scenes
The AI will now use these descriptions verbatim when characters appear.

### Step 3: Review & Edit
After scene generation:

1. Expand each scene
2. Check if character descriptions are complete
3. If not, click "Edit Prompt" and fix it
4. Or use bulk find/replace if the error is consistent

### Step 4: Generate Images
Once prompts are correct, generate images with consistent character appearance.

---

## Why This Matters

### Before (Inconsistent):
**Scene 1:** "Man in his 40s with beard"  
**Scene 5:** "Man in his 50s with glasses"  
**Scene 10:** "Heavy-set man with dark hair"  

**Result:** Three completely different-looking people

### After (Consistent):
**All scenes:** "Moderately heavy-set man in his late 40s with short black hair and short black unkempt beard, black-framed glasses"

**Result:** Same person across all images (or at least much more consistent)

---

## Pro Tips

### 1. **Characters.txt File**
Create a `characters.txt` file in your app directory with permanent descriptions:
```
Dean: Moderately heavy-set man in his late 40s with short black hair, short black unkempt beard, black-framed glasses

Kristina: [full description]

Sophia: [full description]
```

The app auto-loads this on startup → no retyping.

### 2. **Test with One Scene First**
Generate scenes, check scene 1's prompt, edit if needed, THEN generate all images.

### 3. **Use Bulk Replace for Consistent Fixes**
If you notice "late 40s" got changed to "50s" in multiple scenes, use find/replace to fix all at once.

### 4. **Art Direction Still Works**
Character descriptions + art direction = consistent characters with consistent style:
```
Prompt: "Moderately heavy-set man in his late 40s with short black hair 
and short black unkempt beard, black-framed glasses standing by rain-streaked 
window. Style: hazy atmosphere, muted colors, dreamlike soft focus, vintage aesthetic"
```

---

## Troubleshooting

**Q: Characters still look different across scenes**

**A:** AI image generators have inherent randomness. Even with identical prompts, there will be variation. But verbatim descriptions make it MUCH more consistent than before.

**Q: The AI still paraphrased my character description**

**A:** Use the edit button to fix it manually, or regenerate scenes (it might work better on retry).

**Q: Can I edit the scene text too?**

**A:** Currently only prompts are editable per-scene. But you can edit the full narrative before breaking into scenes.

**Q: I edited a prompt but it didn't save**

**A:** Make sure you clicked "💾 Save" not just edited the text. The app needs the save click to update.

---

## Summary

✅ **Better prompting:** AI uses complete character descriptions verbatim  
✅ **Individual editing:** Edit any scene's prompt with ✏️ button  
✅ **Bulk editing:** Find/replace across all prompts at once  
✅ **Persistent characters:** Create `characters.txt` for auto-loaded descriptions  

This should dramatically improve character consistency across your images!