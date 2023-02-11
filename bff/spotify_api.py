import base64
import requests
import os

CLIENT_ID=os.environ['CLIENT_ID']
CLIENT_SECRET=os.environ['CLIENT_SECRET']

async def auth():
  url = "https://accounts.spotify.com/api/token"
  encoded = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode())
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Basic {encoded}'
    }
  data = {'grant_type': 'client_credentials'}
  response = requests.post(
    url,
    headers=headers,
    data=data
  )
  return response.json