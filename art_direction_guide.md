# Art Direction Feature - How It Works

## What It Does

The art direction text box lets you define a visual style that automatically gets appended to **every single scene prompt**. This ensures all your scenes have a consistent look and feel without manually editing each one.

---

## Example: Hazy Dreamlike Style

### Your Art Direction Input:
```
16mm film grain, hazy atmosphere, muted desaturated colors, 
dreamlike soft focus, vintage 1970s aesthetic, melancholic mood, 
analog texture, light leaks, gentle vignetting
```

### Scene Without Art Direction:
```json
{
  "scene_number": 1,
  "text": "The weight settles. I breathe, but the air feels thin.",
  "image_prompt": "Abstract stones sinking through dark water, heavy descent through gradient blues"
}
```

### Scene WITH Art Direction:
```json
{
  "scene_number": 1,
  "text": "The weight settles. I breathe, but the air feels thin.",
  "image_prompt": "Abstract stones sinking through dark water, heavy descent through gradient blues. Style: 16mm film grain, hazy atmosphere, muted desaturated colors, dreamlike soft focus, vintage 1970s aesthetic, melancholic mood, analog texture, light leaks, gentle vignetting"
}
```

**Result:** Instead of vibrant sci-fi blues, you get muted, hazy, dreamlike imagery with analog texture.

---

## Example Style Guides

### Hazy Dream:
```
soft focus, hazy atmosphere, muted colors, dreamlike quality, 
gentle fog, low contrast, ethereal mood
```

### Vintage Film:
```
16mm film grain, light leaks, dust particles, analog texture, 
warm color cast, vintage aesthetic, scratches and imperfections
```

### Dark Moody:
```
deep shadows, high contrast, noir lighting, dramatic atmosphere, 
dark tones, minimal color, cinematic mood
```

### VHS Nostalgia:
```
VHS tape artifacts, tracking errors, chromatic aberration, 
low resolution aesthetic, vintage 1990s, analog video noise
```

### Ethereal Fog:
```
heavy fog, atmospheric haze, soft diffusion, volumetric lighting, 
minimal contrast, ghostly presence, dreamlike blur
```

### Abstract Minimalist:
```
minimal composition, negative space, geometric forms, 
stark contrast, limited color palette, modernist aesthetic
```

---

## Pro Tips

**1. Start Simple**
Don't overload with 20 different style terms. Pick 5-7 key descriptors that define the vibe.

**2. Test and Iterate**
Generate a few scenes, see how Imagen interprets your direction, adjust.

**3. Mix and Match**
Combine technical terms (16mm, grain) with mood terms (melancholic, ethereal).

**4. Works for Video Too**
The same art direction applies to video prompts. Your style stays consistent whether you're generating images or video.

**5. Leave Blank for Defaults**
If you don't fill it in, Claude will generate prompts based purely on the emotional content of each scene.

---

## How to Use

1. Open the "🎨 Style Guide / Art Direction" expander
2. Paste or type your style description
3. Click "Break Into Scenes"
4. Every scene prompt now includes: `[scene description]. Style: [your art direction]`
5. Generate images/videos - they'll all match your aesthetic

---

## Real-World Workflow

**Problem:** "My images are too vibrant and sci-fi. I want hazy, muted, dreamlike."

**Solution:**
```
Art Direction: 
hazy atmosphere, muted desaturated colors, dreamlike soft focus, 
melancholic mood, gentle fog, low saturation, vintage aesthetic
```

**Result:** All 20-30 scenes now have consistent hazy, dreamlike, muted aesthetic instead of vibrant defaults.