import requests

def post(text: str) -> float:
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
  emo = response.json()['emotion']
  if emo == "positive":
    return 1.0
  elif emo == "negative":
    return 0
  return 0.5
