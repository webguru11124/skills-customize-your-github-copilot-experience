from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

# TODO: Add CRUD endpoints here