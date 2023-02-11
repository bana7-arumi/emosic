import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from pydantic import BaseModel
import emo_api
from api_handler.recommendation import Recommendation
import spotify_api


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


class Item(BaseModel):
    text: str
    num: int


class EmotionText(BaseModel):
    """感情分析に噛ませるためのテキスト
    """
    text: str

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.post('/post')
async def declare_request_body(item: EmotionText):
    emotion = emo_api.post(item.text)
    valence: float = emo_api.to_valence(emotion)
    access_token: str = await spotify_api.auth()
    res = await spotify_api.post(access_token=access_token, valence=valence)
    item = Recommendation(**res)
    album = item.tracks[0].album
    return {
        "emo_result": emotion,
        "album_id": album.id,
        "name": album.name,
        "uri": album.uri,
        "image": {
                "url": album.images[0].url,
                "height": album.images[0].height,
                "width": album.images[0].width
            }
    }
