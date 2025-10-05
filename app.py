import streamlit as st
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

# Page configuration
st.set_page_config(page_title="Video to Audio Extractor", page_icon="🎵")

st.title("🎬 Video to Audio Extractor")
st.write("Upload any video file and extract the audio as MP3 instantly!")

# File uploader
uploaded_file = st.file_uploader("📤 Upload a video file", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file is not None:
    # Show preview
    st.video(uploaded_file)

    if st.button("🎧 Extract Audio"):
        # Save uploaded file temporarily
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            # Extract audio from video
            video = VideoFileClip("temp_video.mp4")
            audio = video.audio

            output_path = "output_audio.mp3"
            audio.write_audiofile(output_path, codec="libmp3lame", fps=44100)

            st.success("✅ Audio extracted successfully!")

            # Play extracted audio
            st.audio(output_path)

            # Download option
            with open(output_path, "rb") as f:
                st.download_button("⬇️ Download Audio", f, file_name="extracted_audio.mp3")

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")

        finally:
            # Cleanup resources
            if 'audio' in locals():
                audio.close()
            if 'video' in locals():
                video.close()
            if os.path.exists("temp_video.mp4"):
                os.remove("temp_video.mp4")
            if os.path.exists("output_audio.mp3"):
                os.remove("output_audio.mp3")
