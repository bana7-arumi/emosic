from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
import emotional_analysis

class Post(BaseModel):
    text: str

app = FastAPI()

@app.get("/", response_class=ORJSONResponse)
def index():
    return ORJSONResponse({
        "Hello": "World!"
    })

@app.post("/inference", response_class=ORJSONResponse)
def inference(post: Post):
    return ORJSONResponse({
        "text": post.text,
        "emotion": emotional_analysis.inference(post.text)
    })
