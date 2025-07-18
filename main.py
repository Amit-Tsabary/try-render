from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
