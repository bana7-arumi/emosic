import requests
import json

def post(text: str) -> str:
  host = "api"
  port = 8000
  uri = "inference"
  url = f"http://{host}:{port}/{uri}"
  headers = {'Content-Type': 'application/json'}
  data = {
    "text": text
  }
  response = requests.post(
    url,
    headers=headers,
    json=data
  )
  return response.json()
