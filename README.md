# Grief Video Generator

Streamlit app to transform stream of consciousness into video-ready assets for CapCut.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt --break-system-packages
```

2. Create a `.env` file in the same directory as the script:
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your actual API keys
```

Your `.env` file should look like:
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
GOOGLE_API_KEY=your-google-key-here
ELEVENLABS_API_KEY=your-elevenlabs-key-here
OPENAI_API_KEY=sk-your-openai-key-here  # Optional - for future features
```

3. (Optional) Create a `characters.txt` file for character descriptions:
```bash
# Copy the example file
cp characters.txt.example characters.txt

# Edit characters.txt and add your character descriptions
```

Your `characters.txt` file should look like:
```
Kristina: Woman in her late 40s with brown hair
Dean: Man in his 50s
Sophia: 3-year-old granddaughter with curly hair
```

4. Run the app:
```bash
streamlit run grief_video_generator.py
```

5. Open in browser (usually `http://localhost:8501`)

**Note:** The API keys from `.env` will auto-populate in the sidebar. You can still override them in the UI if needed.

## Configuration Needed

All API keys are loaded from the `.env` file - just fill that in and you're ready to go!

## Workflow

1. Paste your raw thoughts into the text area
2. (Optional) Add character descriptions in the expandable section
3. Enter your API keys in the sidebar
4. Click "Generate Narrative" - review the poetic version (editable)
5. Click "Break Into Scenes" - see the scene breakdown
6. Click "Generate All Assets" - creates images + one continuous audio file
7. (Optional) Regenerate individual images with custom prompts if you don't like them
8. Output folder appears in `/mnt/user-data/outputs/video_TIMESTAMP/`
9. Import into CapCut and sync the continuous audio with your image timeline

### Character Information (Optional)

You can provide physical descriptions of people mentioned in your narrative. Create a `characters.txt` file in the same directory as the script, and it will automatically load when you start the app. Alternatively, you can type/paste character info directly in the expandable section.

Example `characters.txt`:
```
Kristina: Woman in her late 40s with brown hair
Dean: Man in his 50s
Sophia: 3-year-old girl with curly hair
```

When the AI creates image generation prompts, it will reference these descriptions to ensure accuracy. The AI will only use these descriptions when relevant - not every image will feature these characters.

### Audio Generation

The app generates the entire narrative as one continuous audio file, which preserves natural prosody, emotional flow, and prevents the robotic/disjointed quality of generating scenes separately. You'll manually sync this with your images in CapCut, giving you full creative control over timing and pacing.

### Image Regeneration

After generating all assets, you can regenerate individual images with custom prompts:

1. Select the scene number you want to regenerate
2. View the current prompt and image (optional - for reference)
3. Enter a new custom prompt
4. Click "Regenerate This Image"

The new image will overwrite the old one in your output folder. This lets you iterate on specific images without regenerating everything.

## Output Structure

```
video_20241205_143022/
├── narrative.txt          # Full script
├── character_info.txt     # Character descriptions (if provided)
├── scenes.json           # Scene data for reference
├── full_narrative.mp3    # Complete audio file
├── scene_01.png          # First image
├── scene_02.png          # Second image
└── ...
```

## Next Steps / Improvements

- Add ability to regenerate individual scenes
- Add image/audio preview before saving
- Add scene reordering
- Add custom voice selection dropdown
- Save API keys securely (not in sidebar)
- Better error handling
- Add style presets for different video moods

## Notes

- API keys are loaded from `.env` file and auto-populate in the sidebar
- **IMPORTANT:** Never commit your `.env` file to git - it's already in `.gitignore`
- You can still manually enter/override keys in the sidebar if needed
- Scenes are numbered sequentially for easy timeline arrangement
- The narrative step is separate so you can review before committing to scene breakdown
- All processing happens locally except API calls