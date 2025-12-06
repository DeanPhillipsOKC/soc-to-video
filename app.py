import streamlit as st
import os
from datetime import datetime
from pathlib import Path
import anthropic
from google import genai
from elevenlabs import ElevenLabs
import json
from dotenv import load_dotenv
from openai import OpenAI
import subprocess

# Load environment variables from .env file if it exists
load_dotenv()

# Load character info from file if it exists
character_info_file = Path("characters.txt")
default_character_info = ""
if character_info_file.exists():
    with open(character_info_file, 'r', encoding='utf-8') as f:
        default_character_info = f.read()

# Page config
st.set_page_config(page_title="Grief Video Generator", page_icon="🎬", layout="wide")

# API key inputs in sidebar
st.sidebar.header("API Configuration")
anthropic_key = st.sidebar.text_input(
    "Anthropic API Key", 
    value=os.getenv("ANTHROPIC_API_KEY", ""),
    type="password"
)
google_key = st.sidebar.text_input(
    "Google API Key", 
    value=os.getenv("GOOGLE_API_KEY", ""),
    type="password"
)
elevenlabs_key = st.sidebar.text_input(
    "ElevenLabs API Key", 
    value=os.getenv("ELEVENLABS_API_KEY", ""),
    type="password"
)
openai_key = st.sidebar.text_input(
    "OpenAI API Key (optional - for future features)", 
    value=os.getenv("OPENAI_API_KEY", ""),
    type="password"
)

st.title("🎬 Grief Video Generator")
st.markdown("Transform your stream of consciousness into video-ready content")

# Character info input (optional)
with st.expander("📝 Character Information (Optional)", expanded=False):
    st.markdown("Add descriptions of people who might appear in your narrative. This helps generate accurate image prompts.")
    st.markdown("💡 **Tip:** Create a `characters.txt` file in the same directory as this script to auto-load your character descriptions.")
    character_info = st.text_area(
        "Character Descriptions",
        value=default_character_info,
        height=150,
        placeholder="""Example:
Kristina: Woman in her late 40s, [physical description]
Dean: [description]
Sophia: 3-year-old granddaughter, [description]""",
        help="The AI will reference these descriptions when creating image prompts that feature these people"
    )

# Main input
input_text = st.text_area(
    "Stream of Consciousness",
    height=300,
    placeholder="Write your raw thoughts here..."
)

# Session state for storing results
if 'narrative' not in st.session_state:
    st.session_state.narrative = None
if 'scenes' not in st.session_state:
    st.session_state.scenes = None
if 'output_folder' not in st.session_state:
    st.session_state.output_folder = None

def generate_narrative(raw_text, api_key):
    """Convert stream of consciousness to poetic narrative"""
    client = anthropic.Anthropic(api_key=api_key)
    
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": f"""Transform this stream of consciousness into a poetic, emotionally resonant narrative for a TikTok video about grief and healing. 

Use poetic prose with challenging, abstract language. Don't simplify or dumb down the concepts - embrace complexity and depth. The language should be contemplative and intellectually engaging while maintaining raw emotional authenticity.

Maintain the emotional weight and visceral honesty, but shape it into something that flows well when spoken aloud.

IMPORTANT: Use only simple punctuation (periods, commas, question marks, exclamation points). Do not use em dashes or colons.

Stream of consciousness:
{raw_text}

Return only the narrative, no preamble."""
        }]
    )
    
    return message.content[0].text

def break_into_scenes(narrative, api_key, character_info=None):
    """Break narrative into scenes with image prompts"""
    client = anthropic.Anthropic(api_key=api_key)
    
    # Build the prompt with optional character info
    character_context = ""
    if character_info and character_info.strip():
        character_context = f"""

CHARACTER INFORMATION (use when relevant for image prompts):
{character_info.strip()}

When a scene mentions any of these characters, incorporate their physical descriptions into the image prompt naturally.
"""
    
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=3000,
        messages=[{
            "role": "user",
            "content": f"""Break this narrative into scenes for a video. Make sure that the entire narrative is accounted for. It is important that all text from the narrative land in a scene. 

IMPORTANT: Create as many scenes as the content actually needs. If there are lots of dramatic shifts in tone, subject, or emotion, you should create 10, 12, 15+ scenes. The minimum is 6 scenes, but that should only be used for narratives with very consistent tone. Don't artificially compress multiple ideas into fewer scenes - let each distinct moment breathe.

For each scene, provide:
1. The text to be spoken (use only simple punctuation - periods, commas, question marks, exclamation points. No em dashes or colons)
2. An image generation prompt that captures the emotional tone (abstract, contemplative, emotionally resonant - not literal). CRITICAL: The image should contain NO TEXT OR WORDS. Every concept must be represented through imagery alone, not written language.{character_context}

Return as JSON array with format:
[
  {{
    "scene_number": 1,
    "text": "...",
    "image_prompt": "..."
  }},
  ...
]

Narrative:
{narrative}

Return only the JSON array, no markdown formatting."""
        }]
    )
    
    # Parse JSON from response
    response_text = message.content[0].text.strip()
    # Remove markdown code blocks if present
    if response_text.startswith('```'):
        response_text = response_text.split('```')[1]
        if response_text.startswith('json'):
            response_text = response_text[4:]
    
    return json.loads(response_text.strip())

def generate_image(prompt, api_key, scene_num, output_folder):
    """Generate image using Gemini (nano banana)"""
    client = genai.Client(api_key=api_key)
    
    # Add explicit instruction to avoid text in images
    enhanced_prompt = f"{prompt}. IMPORTANT: Do not include any text, words, letters, or numbers in the image."
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[enhanced_prompt],
    )
    
    # Extract and save image
    image_path = output_folder / f"scene_{scene_num:02d}.png"
    image_saved = False
    
    for part in response.parts:
        if part.inline_data is not None:
            image = part.as_image()
            image.save(str(image_path))
            image_saved = True
            break
    
    if not image_saved:
        raise Exception(f"No image data returned for scene {scene_num}")
    
    return image_path

def generate_full_audio(narrative, api_key, output_folder):
    """Generate complete audio for entire narrative"""
    client = ElevenLabs(api_key=api_key)
    
    # Generate audio using text_to_speech.convert
    audio = client.text_to_speech.convert(
        text=narrative,
        voice_id="2gPFXx8pN3Avh27Dw5Ma",  # Dean's voice
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
    
    # Save full audio
    full_audio_path = output_folder / "full_narrative.mp3"
    with open(full_audio_path, 'wb') as f:
        for chunk in audio:
            f.write(chunk)
    
    return full_audio_path

def get_word_timestamps(audio_path, openai_api_key):
    """Use Whisper to get word-level timestamps"""
    client = OpenAI(api_key=openai_api_key)
    
    with open(audio_path, 'rb') as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="verbose_json",
            timestamp_granularities=["word"]
        )
    
    return transcript

def find_scene_boundaries(scenes, transcript):
    """Match scenes to transcript and find their start/end times"""
    words = transcript.words
    scene_start_times = []
    
    word_index = 0
    
    # First pass: find where each scene actually starts
    for scene in scenes:
        scene_text = scene['text'].lower().strip()
        scene_words = scene_text.split()[:10]  # Use first 10 words for matching
        
        start_time = None
        
        # Search for the scene's starting words
        for i in range(word_index, len(words)):
            # Access word object attributes with dot notation
            transcript_slice = ' '.join([words[j].word.lower().strip('.,!?') for j in range(i, min(i + min(5, len(scene_words)), len(words)))])
            scene_slice = ' '.join(scene_words[:min(5, len(scene_words))])
            
            # Simple fuzzy match - check if most words match
            if len(set(transcript_slice.split()) & set(scene_slice.split())) >= 3:
                start_time = words[i].start
                word_index = i + 1  # Move forward for next search
                break
        
        scene_start_times.append({
            'scene_number': scene['scene_number'],
            'start': start_time
        })
    
    # Second pass: set end times based on next scene's start
    scene_boundaries = []
    for i, scene_time in enumerate(scene_start_times):
        end_time = None
        
        if scene_time['start'] is not None:
            # If there's a next scene, use its start time as this scene's end
            if i + 1 < len(scene_start_times) and scene_start_times[i + 1]['start'] is not None:
                end_time = scene_start_times[i + 1]['start']
            else:
                # Last scene - use the last word's end time
                end_time = words[-1].end
        
        scene_boundaries.append({
            'scene_number': scene_time['scene_number'],
            'start': scene_time['start'],
            'end': end_time
        })
    
    return scene_boundaries

def check_ffmpeg():
    """Check if FFmpeg is available"""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def split_audio_by_scenes(full_audio_path, scene_boundaries, output_folder):
    """Split the full audio file into individual scene files using FFmpeg"""
    
    # Check if FFmpeg is available
    if not check_ffmpeg():
        raise Exception(
            "FFmpeg not found. Please install FFmpeg:\n"
            "Windows: winget install ffmpeg  OR  download from https://ffmpeg.org/\n"
            "Mac: brew install ffmpeg\n"
            "Linux: sudo apt install ffmpeg"
        )
    
    for boundary in scene_boundaries:
        if boundary['start'] is not None and boundary['end'] is not None:
            scene_path = output_folder / f"scene_{boundary['scene_number']:02d}.mp3"
            
            # Calculate duration
            duration = boundary['end'] - boundary['start']
            
            # Use FFmpeg to extract the segment
            # -ss: start time, -t: duration, -acodec copy: copy audio without re-encoding
            cmd = [
                'ffmpeg',
                '-i', str(full_audio_path),
                '-ss', str(boundary['start']),
                '-t', str(duration),
                '-acodec', 'copy',
                '-y',  # Overwrite output file if it exists
                str(scene_path)
            ]
            
            try:
                subprocess.run(cmd, check=True, capture_output=True)
            except subprocess.CalledProcessError as e:
                raise Exception(f"FFmpeg failed for scene {boundary['scene_number']}: {e.stderr.decode()}")


# Generate narrative button
col1, col2 = st.columns([3, 1])
with col1:
    if st.button("Generate Narrative", type="primary", disabled=not (input_text and anthropic_key)):
        with st.spinner("Crafting your narrative..."):
            st.session_state.narrative = generate_narrative(input_text, anthropic_key)
            st.session_state.scenes = None  # Reset scenes when narrative changes

# Show narrative if generated
if st.session_state.narrative:
    st.markdown("---")
    st.subheader("📝 Poetic Narrative")
    
    col1, col2 = st.columns([4, 1])
    with col1:
        # Make the narrative editable
        edited_narrative = st.text_area(
            "Edit the narrative if needed:",
            value=st.session_state.narrative,
            height=300,
            label_visibility="collapsed"
        )
        # Update session state with any edits
        st.session_state.narrative = edited_narrative
    with col2:
        if st.button("🔄 Regenerate Narrative"):
            with st.spinner("Regenerating..."):
                st.session_state.narrative = generate_narrative(input_text, anthropic_key)
                st.session_state.scenes = None
                st.rerun()
    
    # Break into scenes button
    st.markdown("---")
    if st.button("Break Into Scenes", type="primary"):
        with st.spinner("Creating scene breakdown..."):
            st.session_state.scenes = break_into_scenes(
                st.session_state.narrative, 
                anthropic_key,
                character_info if character_info else None
            )

# Show scenes if generated
if st.session_state.scenes:
    st.markdown("---")
    st.subheader("🎬 Scene Breakdown")
    
    for scene in st.session_state.scenes:
        with st.expander(f"Scene {scene['scene_number']}", expanded=False):
            st.markdown(f"**Text:** {scene['text']}")
            st.markdown(f"**Image Prompt:** {scene['image_prompt']}")
    
    # Generate all assets button
    st.markdown("---")
    all_keys_present = anthropic_key and google_key and elevenlabs_key
    
    if st.button("🎨 Generate All Assets", type="primary", disabled=not all_keys_present):
        # Create output folder
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_folder = Path(f"/mnt/user-data/outputs/video_{timestamp}")
        output_folder.mkdir(parents=True, exist_ok=True)
        st.session_state.output_folder = output_folder
        
        # Save narrative
        with open(output_folder / "narrative.txt", 'w') as f:
            f.write(st.session_state.narrative)
        
        # Save character info if provided
        if character_info and character_info.strip():
            with open(output_folder / "character_info.txt", 'w') as f:
                f.write(character_info.strip())
        
        # Save scene data
        with open(output_folder / "scenes.json", 'w') as f:
            json.dump(st.session_state.scenes, f, indent=2)
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Track failures
        failed_images = []
        
        # Step 1: Generate all images
        status_text.text("🎨 Generating images...")
        for i, scene in enumerate(st.session_state.scenes):
            scene_num = scene['scene_number']
            
            status_text.text(f"🎨 Generating image {i+1}/{len(st.session_state.scenes)} (scene {scene_num})...")
            try:
                generate_image(scene['image_prompt'], google_key, scene_num, output_folder)
                progress_bar.progress((i + 1) / (len(st.session_state.scenes) + 3))  # +3 for audio steps
            except Exception as e:
                st.error(f"❌ Error generating image for scene {scene_num}: {str(e)}")
                failed_images.append(scene_num)
                progress_bar.progress((i + 1) / (len(st.session_state.scenes) + 3))
        
        # Step 2: Generate full narrative audio
        status_text.text("🎙️ Generating complete audio narrative...")
        try:
            full_audio_path = generate_full_audio(st.session_state.narrative, elevenlabs_key, output_folder)
            progress_bar.progress(1.0)
            st.success("✅ Audio generated successfully!")
            audio_success = True
        except Exception as e:
            st.error(f"❌ Error generating audio: {str(e)}")
            audio_success = False
        
        status_text.text("✅ Generation complete!")
        
        # Retry failed images
        if failed_images:
            st.warning(f"Retrying {len(failed_images)} failed image(s)...")
            status_text.text("🔄 Retrying failed images...")
            
            retry_failures = []
            for scene_num in failed_images:
                scene = next(s for s in st.session_state.scenes if s['scene_number'] == scene_num)
                status_text.text(f"🔄 Retrying image for scene {scene_num}...")
                try:
                    generate_image(scene['image_prompt'], google_key, scene_num, output_folder)
                    st.success(f"✅ Successfully generated image for scene {scene_num} on retry")
                except Exception as e:
                    st.error(f"❌ Scene {scene_num} failed again: {str(e)}")
                    retry_failures.append(scene_num)
            
            # Update failed list to only include ones that failed twice
            failed_images = retry_failures
        
        # Summary
        if not failed_images and audio_success:
            st.success(f"All files saved to: {output_folder}")
            st.balloons()
        else:
            st.warning(f"Generation completed with some errors. Files saved to: {output_folder}")
            if failed_images:
                st.error(f"Failed images (after retry) for scenes: {', '.join(map(str, failed_images))}")
            if not audio_success:
                st.error("Audio generation failed - check errors above")

# Show output folder if exists
if st.session_state.output_folder:
    st.markdown("---")
    st.subheader("📁 Output Folder")
    st.code(str(st.session_state.output_folder))
    st.info("Drag this folder into CapCut to start editing!")
    
    # Image regeneration section
    st.markdown("---")
    st.subheader("🔄 Regenerate Individual Images")
    st.markdown("Don't like a specific image? Generate a new one with a custom prompt.")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        scene_to_regen = st.number_input(
            "Scene number",
            min_value=1,
            max_value=len(st.session_state.scenes) if st.session_state.scenes else 1,
            value=1,
            step=1
        )
    
    # Show current prompt for reference
    if st.session_state.scenes:
        current_scene = next((s for s in st.session_state.scenes if s['scene_number'] == scene_to_regen), None)
        if current_scene:
            col_a, col_b = st.columns(2)
            
            with col_a:
                with st.expander("📋 Current prompt for this scene", expanded=False):
                    st.code(current_scene['image_prompt'], language=None)
            
            with col_b:
                # Show current image if it exists
                current_image_path = st.session_state.output_folder / f"scene_{scene_to_regen:02d}.png"
                if current_image_path.exists():
                    with st.expander("🖼️ Current image", expanded=False):
                        st.image(str(current_image_path), use_container_width=True)
    
    with col2:
        custom_prompt = st.text_area(
            "Custom image prompt",
            height=100,
            placeholder="Enter a new image prompt for this scene...",
            help="The instruction to avoid text/words will be added automatically"
        )
    
    if st.button("🎨 Regenerate This Image", type="secondary"):
        if not custom_prompt.strip():
            st.error("Please enter a custom prompt")
        elif not google_key:
            st.error("Google API key required")
        else:
            with st.spinner(f"Regenerating image for scene {scene_to_regen}..."):
                try:
                    generate_image(custom_prompt, google_key, scene_to_regen, st.session_state.output_folder)
                    st.success(f"✅ Successfully regenerated scene {scene_to_regen}!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

# Instructions
with st.sidebar:
    st.markdown("---")
    st.markdown("### How to Use")
    st.markdown("""
    1. Enter API keys above
    2. Paste your stream of consciousness
    3. Generate narrative (review/regenerate if needed)
    4. Break into scenes
    5. Generate all assets
    6. Import folder into CapCut
    """)