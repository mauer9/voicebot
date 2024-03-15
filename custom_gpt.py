#!/usr/bin/python3.6
import sys
import json
import requests
from asterisk.agi import AGI

agi = AGI()
question = sys.argv[1]

URL = 'https://api.openai.com/v1/chat/completions'
TOKEN = 'sk-nuh-uh'
headers = {
    "Content-Type": "application/json",
    'Authorization': f'Bearer {TOKEN}'
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": 'give response in one short sentence: ' + question}],
    "temperature": 0.7
}

response = requests.post(URL, headers=headers, json=data)
if response.status_code == 200:
    decode_resp = response.content.decode('UTF-8')
    text = json.loads(decode_resp)
    content = text['choices'][0]['message']['content']
    agi.set_variable('GPT', content)