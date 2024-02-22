import requests as r
import json

def get_access_token():
    with open('access_token.txt', 'r') as f:
        return f.read()

service_plan_id = 'abghfgf565r7678tu6756756'
access_token = get_access_token()
from_ = '3805865946586'
to_ = '358685995440'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

payload = {
    'from': from_,
    'to': [to_],
    'body': 'Hello, Dear'
}

r.post(
    f'https://sms.api.sinch.com/xms/v1/{service_plan_id}/batches',
    headers=headers,
    data=json.dumps(payload)
).json()