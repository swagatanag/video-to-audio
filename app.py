import streamlit as st
from moviepy.video.io.VideoFileClip import VideoFileClip

import os

st.set_page_config(page_title="Video to Audio Extractor", page_icon="🎵")

st.title("🎬 Video to Audio Extractor")
st.write("Upload any video file and extract the audio as MP3.")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file is not None:
    # Show video preview
    st.video(uploaded_file)

    if st.button("Extract Audio"):
        # Save uploaded video temporarily
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract audio
        video = VideoFileClip("temp_video.mp4")
        audio = video.audio

        output_path = "output_audio.mp3"
        audio.write_audiofile(output_path)

        st.success("✅ Audio extracted successfully!")

        # Play audio in app
        st.audio(output_path)

        # Download button
        with open(output_path, "rb") as f:
            st.download_button("Download Audio", f, file_name="extracted_audio.mp3")

        # Clean up
        audio.close()
        video.close()
        os.remove("temp_video.mp4")