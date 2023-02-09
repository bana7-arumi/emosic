import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from pydantic import BaseModel
@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

class Item(BaseModel):
    text:str

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.post('/post')
async def declare_request_body(item: Item):
    return {"test_message":f"hello, {item.text}"}