#!/usr/bin/python3.6
import sys
import json
import requests
from asterisk.agi import AGI

agi = AGI()

TEXT = ''.join(sys.argv[1:])

url = "https://api.play.ht/api/v2/tts/stream"

payload = {
    "text": TEXT,
    "voice": "s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json",
    "output_format": "mp3",
    "sample_rate": 12000,
    "quality": "low"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "AUTHORIZATION": "**token**",
    "X-USER-ID": "**token**"
}

response = requests.post(url, json=payload, headers=headers)
if response.status_code == 201:
    text = response.content.decode('utf-8')
    text = json.loads(text)
    agi.set_variable('TTS', text['href'])