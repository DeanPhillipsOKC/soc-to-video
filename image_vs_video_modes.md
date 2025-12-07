# Image Mode vs Video Mode - Scene Requirements

## TL;DR
- **Images:** 8-16 scenes, 30-60 words each, contemplative pacing
- **Videos:** 20-30+ scenes, 20-25 words each, fast cuts (for Pika's 10-second limit)

---

## IMAGE MODE (Default - What You Probably Want)

### Scene Count:
**8-16 scenes** (flexible based on content)

### Scene Length:
**30-60 words per scene** - No strict limit
- Scenes can be longer and more contemplative
- Multiple related thoughts in one scene is fine
- Break at major tonal shifts

### Example Scene:
```json
{
  "scene_number": 1,
  "text": "The weight settles in my chest like stones in deep water. I breathe, but the air feels thin, insufficient. Each morning I wake expecting her voice.",
  "image_prompt": "Abstract stones sinking through dark water, minimalist composition, muted blues."
}
```

**Word count:** 27 words (totally fine for images)

### When to Use:
- You're generating static images
- You want contemplative pacing
- You're doing CapCut editing anyway
- You don't need 30 separate files to manage

---

## VIDEO MODE (For Pika/Video APIs)

### Scene Count:
**20-30+ scenes** (possibly more for long narratives)

### Scene Length:
**20-25 words MAX per scene**
- Keeps videos under 10 seconds (Pika's limit)
- Faster cuts, more dynamic
- Each beat is its own scene

### Example Scene:
```json
{
  "scene_number": 1,
  "text": "The weight settles in my chest like stones.",
  "video_prompt": "Abstract stones sinking through dark water. Slow drift downward. Ambient sounds: deep underwater resonance, muffled pressure."
}
```

**Word count:** 10 words (~4 seconds of video)

### When to Use:
- You're using Pika Labs or similar (10-second max)
- You want video prompts with camera movement + ambient sounds
- You're okay with lots of short clips to stitch together

---

## Comparison Table

| Aspect | Image Mode | Video Mode |
|--------|------------|------------|
| **Scenes** | 8-16 | 20-30+ |
| **Words/Scene** | 30-60 (flexible) | 20-25 (strict) |
| **Pacing** | Contemplative | Fast cuts |
| **Prompt Type** | `image_prompt` | `video_prompt` (includes camera + audio) |
| **Best For** | Static slideshow, CapCut editing | Pika video generation |
| **File Management** | Easier (fewer files) | More files to track |

---

## What Changed (Fixed)

### Before:
Both modes were getting "Create MORE scenes rather than fewer" instruction → Image mode was over-segmenting

### After:
- **Image mode:** "Create as many scenes as needed (typically 8-16). Scenes can be longer and more contemplative."
- **Video mode:** "Create 20-30+ scenes (each limited to 20-25 words)"

---

## Recommendation

**Use IMAGE mode unless:**
- You specifically need video prompts for Pika
- You want camera movement + ambient sound descriptions
- You're committed to the 10-second clip workflow

For most grief narrative work with images + CapCut editing, **IMAGE mode** will give you better pacing and fewer files to manage.