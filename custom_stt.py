#!/usr/bin/python3.6
import sys
import json
import requests
from asterisk.agi import AGI

agi = AGI()
path = sys.argv[1]

url = 'https://api.deepgram.com/v1/listen'
headers = {
    # adrien's token
    'Authorization': 'Token **token**',
    'Content-Type': 'audio/*',
    "Accept": "application/json",
}

with open(path, 'rb') as f:
    data_sound = f.read()

response = requests.post(url, headers=headers, data=data_sound)
if response.status_code == 200:
    decode_resp = response.content.decode('UTF-8')
    text = json.loads(decode_resp)
    result = text['results']['channels'][0]['alternatives'][0]['transcript']
    agi.set_variable('STT', result)