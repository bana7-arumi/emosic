import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from pydantic import BaseModel
from api_handler.recommendation import Recommendation
from api_handler.spotify_interface import dummy_APIcall


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
async def declare_request_body(item: Item):
    return {"test_message": f"text:{item.text},num:{item.num}"}


@app.post('/recommendation')
async def test_for_spotify(text: EmotionText):
    res = dummy_APIcall()
    item = Recommendation(**res)
    album = item.tracks[0].album
    return {
        "name": album.name,
        "uri": album.uri,
        "image": [
            {
                "url": album.images[0].url,
                "height": album.images[0].height,
                "width": album.images[0].width
            }
        ]
    }
