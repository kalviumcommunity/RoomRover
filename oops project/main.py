from fastapi import FastAPI, HTTPException
from typing import List
from models import Hotel, RoomType, Room, Guest, Reservation


app = FastAPI()

hotels_db = []
room_types_db = []
rooms_db = []
guests_db = []
reservations_db = []

# Create a hotel
@app.post("/hotels/", response_model=Hotel)
async def create_hotel(hotel: Hotel):
    new_hotel = hotel.dict()
    hotels_db.append(new_hotel)
    return new_hotel

# Get all hotels
@app.get("/hotels/", response_model=List[Hotel])
async def get_hotels():
    return hotels_db

# Update a hotel by hotel_id
@app.put("/hotels/{hotel_id}", response_model=Hotel)
async def update_hotel(hotel_id: int, hotel: Hotel):
    if hotel_id < 0 or hotel_id >= len(hotels_db):
        raise HTTPException(status_code=404, detail="Hotel not found")
    
    hotels_db[hotel_id] = hotel.dict()
    return hotels_db[hotel_id]

# Delete a hotel by hotel_id
@app.delete("/hotels/{hotel_id}", response_model=Hotel)
async def delete_hotel(hotel_id: int):
    if hotel_id < 0 or hotel_id >= len(hotels_db):
        raise HTTPException(status_code=404, detail="Hotel not found")
    
    deleted_hotel = hotels_db.pop(hotel_id)
    return deleted_hotel

# Create a room type
@app.post("/room_types/", response_model=RoomType)
async def create_room_type(room_type: RoomType):
    new_room_type = room_type.dict()
    room_types_db.append(new_room_type)
    return new_room_type

# Get all room types
@app.get("/room_types/", response_model=List[RoomType])
async def get_room_types():
    return room_types_db

# Create a room
@app.post("/rooms/", response_model=Room)
async def create_room(room: Room):
    new_room = room.dict()
    rooms_db.append(new_room)
    return new_room

# Get all rooms
@app.get("/rooms/", response_model=List[Room])
async def get_rooms():
    return rooms_db

# Create a guest
@app.post("/guests/", response_model=Guest)
async def create_guest(guest: Guest):
    new_guest = guest.dict()
    guests_db.append(new_guest)
    return new_guest

# Get all guests
@app.get("/guests/", response_model=List[Guest])
async def get_guests():
    return guests_db

# Create a reservation
@app.post("/reservations/", response_model=Reservation)
async def create_reservation(reservation: Reservation):
    new_reservation = reservation.dict()
    reservations_db.append(new_reservation)
    return new_reservation

# Get all reservations
@app.get("/reservations/", response_model=List[Reservation])
async def get_reservations():
    return reservations_db

# Update a reservation by reservation_id
@app.put("/reservations/{reservation_id}", response_model=Reservation)
async def update_reservation(reservation_id: int, reservation: Reservation):
    if reservation_id < 0 or reservation_id >= len(reservations_db):
        raise HTTPException(status_code=404, detail="Reservation not found")

    # Update the reservation in the database
    reservations_db[reservation_id] = reservation.dict()
    return reservations_db[reservation_id]

# Delete a reservation by reservation_id
@app.delete("/reservations/{reservation_id}", response_model=Reservation)
async def delete_reservation(reservation_id: int):
    if reservation_id < 0 or reservation_id >= len(reservations_db):
        raise HTTPException(status_code=404, detail="Reservation not found")

    # Remove the reservation from the database
    deleted_reservation = reservations_db.pop(reservation_id)
    return deleted_reservation
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)