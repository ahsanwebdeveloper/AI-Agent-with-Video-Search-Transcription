import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

def search_youtube_video(query):
    params = {
        "engine": "youtube",
        "search_query": query,
        "api_key": os.getenv("SERPAPI_API_KEY")
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    videos = results.get("video_results", [])
    if not videos:
        return None

    return videos[0]["link"]
