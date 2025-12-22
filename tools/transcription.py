from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe_video(video_url):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"""
                You are a transcription assistant.
                Based on this YouTube video, write a detailed transcript or explanation.

                Video URL: {video_url}
                """
            }
        ]
    )

    return response.choices[0].message.content
