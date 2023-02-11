from pydantic import BaseModel
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import emo_api
from api_handler.recommendation import Recommendation
import spotify_api
from strawberry.scalars import JSON

class Item(BaseModel):
    text: str
    num: int

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"
schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


    
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def declare_request_body(self, text:str) -> JSON :
        emotion = emo_api.post(text)
        valence: float = emo_api.to_valence(emotion)
        access_token: str = await spotify_api.auth()
        res = await spotify_api.post(access_token=access_token, valence=valence)
        item = Recommendation(**res)
        album = item.tracks[0].album
        artist_names = ""
        for track in item.tracks:
            artist_names = "".join(track.artists[0].name)
        # valenceがnegative(0.0)ならpositiveでもapiを叩く
        if valence == 0.0:
            positive_res = await spotify_api.post(access_token=access_token, valence=1.0)
            positive_item = Recommendation(**positive_res)
            positive_album = positive_item.tracks[0].album
            positive_artist_names = ""
            for track in positive_item.tracks:
                positive_artist_names = "".join(track.artists[0].name)
            return {
                "emo_result": emotion,
                "artist_name": artist_names,
                "album_id": album.id,
                "name": album.name,
                "uri": album.uri,
                "image": {
                        "url": album.images[0].url,
                        "height": album.images[0].height,
                        "width": album.images[0].width
                    },
                "positive": {
                    "emo_result": emotion,
                    "artist_name": positive_artist_names,
                    "album_id": positive_album.id,
                    "name": positive_album.name,
                    "uri": positive_album.uri,
                    "image": {
                            "url": positive_album.images[0].url,
                            "height": positive_album.images[0].height,
                            "width": positive_album.images[0].width
                        }
                }
            }
        return {
            "emo_result": emotion,
            "artist_name": artist_names,
            "album_id": album.id,
            "name": album.name,
            "uri": album.uri,
            "image": {
                    "url": album.images[0].url,
                    "height": album.images[0].height,
                    "width": album.images[0].width
                }
            }

schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")