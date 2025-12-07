# Video Prompt Format Examples

This shows how the app will generate different prompts based on whether you select "Images" or "Videos".

## Key Difference for Video Mode:
- **Scenes are LIMITED to 20-25 words** (to fit Pika's 10-second max)
- You'll get **MORE scenes** (20-30+ instead of 6-16)
- Each scene includes **camera movement + ambient sounds**

---

## Example Scene Text (SHORT for video):
"The weight settles. I breathe, but the air feels thin."

**Word count:** 11 words
**Estimated duration:** ~4.4 seconds ✅ Fits in 10s

---

## VIDEO MODE Output:

```json
{
  "scene_number": 1,
  "text": "The weight settles. I breathe, but the air feels thin.",
  "video_prompt": "Abstract stones sinking through dark water, heavy descent through gradient blues. Slow drift downward. Ambient sounds: deep underwater resonance, muffled pressure, subtle bubbling."
}
```

**What you get:**
- Visual description
- **Camera movement:** "Slow drift downward"
- **Ambient sounds:** "deep underwater resonance, muffled pressure, subtle bubbling"
- **NO dialogue** (won't conflict with ElevenLabs narration)

---

## UI Features for Video Mode:

The app now shows:

```
📊 11 words (~4.4s estimated duration)
```

If a scene exceeds 25 words, you'll see:
```
⚠️ 32 words (~12.8s) - May exceed 10-second Pika limit. Consider splitting this scene.
```

**Summary stats at top:**
```
Total Scenes: 28
Estimated Total Duration: 186.4s
Scenes >25 words: 0 ✅ All fit in 10s
```

---

## Example: TOO LONG Scene

**BAD:**
```json
{
  "text": "The weight settles in my chest like stones in deep water, pulling me down into darkness I can't escape from, suffocating and endless."
  // 24 words - right at limit, but sentence is incomplete
}
```

**BETTER - Split into 2 scenes:**
```json
{
  "scene_number": 1,
  "text": "The weight settles in my chest like stones in deep water."
  // 12 words - fits easily
},
{
  "scene_number": 2,
  "text": "Pulling me down into darkness. Suffocating and endless."
  // 9 words - fits easily
}
```

---

## How to Use This:

1. Select "**Videos**" as media type
2. Click "**Break Into Scenes**"
3. Review the word counts - make sure most are under 25 words
4. **Copy each video_prompt** one by one
5. Paste into **Pika Labs** interface
6. Pika generates with visuals + camera movement + ambient sounds
7. Download and layer your **ElevenLabs voiceover** in CapCut

The ambient sounds WON'T conflict with narration - they complement it.