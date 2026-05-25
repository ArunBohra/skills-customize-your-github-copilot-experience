from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

items: List[Item] = []

@app.get("/items", response_model=List[Item])
def list_items(limit: int = 10, search: Optional[str] = None):
    results = items
    if search:
        results = [item for item in items if search.lower() in item.name.lower()]
    return results[:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if any(existing.id == item.id for existing in items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item)
    return item

if __name__ == "__main__":
    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
