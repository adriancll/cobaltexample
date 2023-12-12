import requests
import json

url = "https://co.wuk.sh/api/json"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

url = input("Enter the URL of the video: ")
data = {
    "url": url,
    "vCodec": "h264",
    "vQuality": "720",
    "aFormat": "mp3",
    "filenamePattern": "classic",
    "isAudioOnly": False,
    "isNoTTWatermark": False,
    "isTTFullAudio": False,
    "isAudioMuted": False,
    "dubLang": False,
    "disableMetadata": False
}

json_data = json.dumps(data)

response = requests.post(url, headers=headers, data=json_data)


if response.status_code == 200:
    response_data = response.json()
    
    download_url = response_data.get("url")

    video_response = requests.get(download_url)
    with open("downloaded_video.mp4", "wb") as f:
        f.write(video_response.content)
else:
    print(f"Error: {response.status_code} - {response.text}")
