import typing as t

from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# FastAPI object initialization
app = FastAPI(
    description="This is the backend project for inventory management using FastAPI for API development" # noqa
)

# adding cors middleware to allow cross-origin request that can come from
# different protocol, domains or ports
# reference: https://fastapi.tiangolo.com/tutorial/cors/#cors-cross-origin-resource-sharing # noqa
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    description: t.Union[str, None] = None
    cost: float
    time: datetime = datetime.now()


@app.get("/")
def root_path():
    return "This is the root path of Inventory Management framework"


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}
