# Quick Reference: Editing Prompts

## Individual Scene Editing

### How It Works:

```
┌─────────────────────────────────────────┐
│ Scene 3                            ▼    │
├─────────────────────────────────────────┤
│ Text: I stand at her empty closet...   │
│ 📊 15 words (~6.0s)                     │
│                                         │
│ Image Prompt: Man in his 50s with      │
│ beard standing at closet               │
│                                         │
│ [✏️ Edit Prompt]                        │
└─────────────────────────────────────────┘
```

**Click "Edit Prompt" →**

```
┌─────────────────────────────────────────┐
│ Scene 3                            ▼    │
├─────────────────────────────────────────┤
│ Text: I stand at her empty closet...   │
│ 📊 15 words (~6.0s)                     │
│                                         │
│ Image Prompt:                           │
│ ┌─────────────────────────────────────┐ │
│ │Moderately heavy-set man in his    │ │
│ │late 40s with short black hair and │ │
│ │short black unkempt beard, black-  │ │
│ │framed glasses standing at closet, │ │
│ │contemplative mood, soft lighting  │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ [💾 Save]  [❌ Cancel]                  │
└─────────────────────────────────────────┘
```

**Click "Save" → Prompt updated! ✅**

---

## Bulk Find/Replace

### How It Works:

```
┌──────────────────────────────────────────────┐
│ ⚙️ Bulk Operations                      ▼    │
├──────────────────────────────────────────────┤
│ Quick actions for all scenes:                │
│                                              │
│ Find text in prompts:                        │
│ ┌──────────────────────────────────────────┐ │
│ │man in his 50s                            │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│ Replace with:                                │
│ ┌──────────────────────────────────────────┐ │
│ │moderately heavy-set man in his late 40s  │ │
│ │with short black hair and short black     │ │
│ │unkempt beard, black-framed glasses       │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│ [🔄 Replace in All Prompts]                  │
└──────────────────────────────────────────────┘
```

**Click "Replace" → Updates all matching scenes**

```
✅ Updated 8 scene(s)
```

---

## Common Use Cases

### Fix Character Age Error
```
Find: "in his 50s"
Replace: "in his late 40s"
```

### Add Complete Character Description
```
Find: "man with beard"
Replace: "moderately heavy-set man in his late 40s with short black hair and short black unkempt beard, black-framed glasses"
```

### Add Style to All Scenes
```
Find: "."
Replace: ". Style: hazy atmosphere, muted colors, dreamlike soft focus"
```
*(Appends to all prompts ending with period)*

### Remove Unwanted Element
```
Find: "vibrant colors, "
Replace: ""
```
*(Removes from all scenes that have it)*

### Fix Spelling Error
```
Find: "seperate"
Replace: "separate"
```

---

## Keyboard-Free Workflow

1. Generate scenes
2. Scroll through, find issues
3. Use bulk find/replace for consistent errors
4. Use individual edit for one-off fixes
5. Generate images with corrected prompts

No need to regenerate scenes or manually type the same fix 15 times!