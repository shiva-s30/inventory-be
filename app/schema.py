from typing import Union
from pydantic import BaseModel as PydBaseModel


class Item(PydBaseModel):
    id: int
    owner_id: int
    title: str
    description: Union[str, None] = None

    class Config:
        orm_mode = True


class User(PydBaseModel):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
