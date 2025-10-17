from fastapi import FastAPI
from pydantic.v1 import BaseConfig as BaseConfig
# Create an app
app = FastAPI()

# define a path for HTTP Get method
@app.get("/")
def root():
    return {"Hello": "World"}

items = ["orange"]

@app.post("items")
def create_item(item: str):
    items.append(item)
    return item

@app.get("items/{item_id}")
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item