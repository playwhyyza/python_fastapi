# how to run app
# uvicorn main:app --reload

from typing import List, Dict
from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

class User(BaseModel):
    id: int
    name: str
    joined: date

def main(user_id: str):
    return user_id

my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30"
}

my_second_user: User = User(**second_user_data)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_id": item_id}

@app.get("/user")
def read_user():
    return {"my_user": my_user, "my_second_user": my_second_user}