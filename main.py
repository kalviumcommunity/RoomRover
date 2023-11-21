from abc import ABC, abstractmethod
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class AbstractDatabase(ABC):

    @abstractmethod
    def create_item(self, item: BaseModel):
        pass

    @abstractmethod
    def get_all_items(self) -> List[BaseModel]:
        pass

    @abstractmethod
    def update_item(self, item_id: int, updated_item: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def delete_item(self, item_id: int) -> BaseModel:
        pass

class InMemoryDatabase(AbstractDatabase):

    def __init__(self):
        self.hotels_db: List[BaseModel] = []

    def create_item(self, item: BaseModel) -> BaseModel:
        new_item = item.dict()
        self.hotels_db.append(new_item)
        return new_item

    def get_all_items(self) -> List[BaseModel]:
        return self.hotels_db

    def update_item(self, item_id: int, updated_item: BaseModel) -> BaseModel:
        if 0 <= item_id < len(self.hotels_db):
            self.hotels_db[item_id] = updated_item.dict()
            return self.hotels_db[item_id]
        else:
            raise HTTPException(status_code=404, detail="Item not found")

    def delete_item(self, item_id: int) -> BaseModel:
        if 0 <= item_id < len(self.hotels_db):
            return self.hotels_db.pop(item_id)
        else:
            raise HTTPException(status_code=404, detail="Item not found")

app = FastAPI()
db = InMemoryDatabase()

# Create a hotel
@app.post("/hotels/", response_model=BaseModel)
async def create_hotel(hotel: BaseModel):
    return db.create_item(hotel)

# Get all hotels
@app.get("/hotels/", response_model=List[BaseModel])
async def get_hotels():
    return db.get_all_items()

# Update a hotel by hotel_id
@app.put("/hotels/{hotel_id}", response_model=BaseModel)
async def update_hotel(hotel_id: int, hotel: BaseModel):
    return db.update_item(hotel_id, hotel)

# Delete a hotel by hotel_id
@app.delete("/hotels/{hotel_id}", response_model=BaseModel)
async def delete_hotel(hotel_id: int):
    return db.delete_item(hotel_id)
