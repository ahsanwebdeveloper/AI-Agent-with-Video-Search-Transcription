from tools.video_search import search_youtube_video
from tools.transcription import transcribe_video

def run_agent(user_query):
    # Step 1: Search Video
    video_url = search_youtube_video(user_query)
    if not video_url:
        return None, "No video found"

    # Step 2: Transcription
    transcript = transcribe_video(video_url)

    # Step 3: Save transcript
    with open("transcripts/output.txt", "w", encoding="utf-8") as f:
        f.write(transcript)

    return video_url, transcript
