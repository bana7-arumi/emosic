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
  return emo

def to_valence(emotion):
  if emotion == "positive":
    return 1.0
  elif emotion == "negative":
    return 0
  else:
    return 0.5