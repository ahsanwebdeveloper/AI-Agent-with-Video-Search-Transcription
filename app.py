import streamlit as st
from agent import run_agent

st.set_page_config(page_title="AI Video Agent", layout="wide")

st.title(" AI Agent – Video Search + Transcription")

query = st.text_input("Enter topic to search video:")

if st.button("Search & Transcribe"):
    with st.spinner("Working..."):
        video_url, transcript = run_agent(query)

    if video_url:
        st.success("Video Found!")
        st.video(video_url)

        st.subheader("📄 Transcription")
        st.text_area("Transcript", transcript, height=300)
    else:
        st.error("No video found!")
