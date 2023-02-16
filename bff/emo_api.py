import requests
import math
import random

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
  truncation = 100
  if emotion == "positive":
    # 0.7 < x <= 1.0
    return math.floor(random.uniform(0.71, 1.0) * truncation) / truncation
  elif emotion == "negative":
    # 0.0 <= x < 0.3
    return math.floor(random.uniform(0.0, 2.9) * truncation) / truncation
  else:
    # 0.3 <= x <= 0.7
    return math.floor(random.uniform(0.3, 0.7) * truncation) / truncation