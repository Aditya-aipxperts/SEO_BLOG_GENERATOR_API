import re
import time
import requests
from urllib.parse import urlparse
import os
import random
import datetime
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, VideoUnavailable
import traceback
from setup_env import setup_environment

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

setup_environment()
def extract_channel_id(channel_url):
    """Extract YouTube channel ID from URL: supports /channel/, /@handle, /user/, /c/."""
    try:
        # Clean URL
        channel_url = channel_url.strip().rstrip('/')
        if not channel_url.startswith(("http://", "https://")):
            channel_url = "https://" + channel_url

        parsed = urlparse(channel_url)
        path = parsed.path

        # Case 1: Direct channel ID
        if '/channel/' in path:
            return path.split('/channel/')[1]

        # Case 2: Handle - /@pewdiepie
        elif '/@' in path:
            handle = path.split('/@')[1]
            search_url = (
                f"https://www.googleapis.com/youtube/v3/search"
                f"?part=snippet&type=channel&maxResults=1&q={handle}&key={YOUTUBE_API_KEY}"
            )
            response = requests.get(search_url, timeout=10).json()
            if response.get("items"):
                return response["items"][0]["snippet"]["channelId"]

        # Case 3: Legacy URLs like /user/ or /c/
        else:
            # Fallback to scraping
            response = requests.get(channel_url, timeout=10)
            html = response.text
            match = re.search(r'"channelId":"(UC[0-9A-Za-z_-]{22})"', html)
            if match:
                return match.group(1)

        raise ValueError("Could not extract channel ID from URL")

    except Exception as e:
        raise ValueError(f"extract_channel_id failed: {e}")
    

def get_video_ids(channel_id, max_results=2):
    """Fetch latest video IDs from a channel using API (fallback: scraping)."""
    video_ids = []

    # ✅ METHOD 1: Use YouTube Data API
    try:
        url = (
            f"https://www.googleapis.com/youtube/v3/search"
            f"?key={YOUTUBE_API_KEY}&channelId={channel_id}"
            f"&part=snippet,id&order=date&maxResults={max_results}&type=video"
        )
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("items"):
            for item in data["items"]:
                if item["id"]["kind"] == "youtube#video":
                    video_ids.append({
                        "videoId": item["id"]["videoId"],
                        "title": item["snippet"]["title"],
                        "publishedAt": item["snippet"]["publishedAt"]
                    })

        if video_ids:
            return video_ids

    except Exception as e:
        print(f"[API Fallback] Failed to get videos via API: {e}")

    # ❌ METHOD 2: Fallback to scraping
    try:
        url = f"https://www.youtube.com/channel/{channel_id}/videos"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text

        # Extract videoId from HTML
        matches = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
        unique_ids = list(set(matches))[:max_results]

        for vid in unique_ids:
            video_ids.append({
                "videoId": vid,
                "title": f"Video {vid}",
                "publishedAt": datetime.now().isoformat()
            })

        return video_ids

    except Exception as e:
        print(f"[Scrape Fallback] Failed to scrape video IDs: {e}")
        return []

def get_transcript_with_backoff(video_id, max_retries=6):
    for i in range(max_retries):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            print(transcript)
            return "\n".join([entry["text"] for entry in transcript])
        except TranscriptsDisabled:
            print(f"[TranscriptsDisabled] Transcripts are disabled for video: {video_id}")
            return "[Transcripts are disabled for this video]"
        except VideoUnavailable:
            print(f"[VideoUnavailable] Video is unavailable or private: {video_id}")
            return "[Video is unavailable or private]"
        except Exception as e:
            print(f"[Exception] Attempt {i+1}/{max_retries} for video {video_id}: {e!r}")
            traceback.print_exc()
            # Increase wait time exponentially and add a larger random component
            wait = (3 ** i) + random.randint(5, 15)
            print(f"⏳ Rate limited. Retrying in {wait} seconds...")
            time.sleep(wait)
    print(f"[Failed] Could not fetch transcript for video {video_id} after {max_retries} retries.")
    return "[Failed after multiple retries]"

