from pydantic import BaseModel
class Hotel(BaseModel):
    hotel_id: int
    name: str
    address: str
    phone: str
    email: str

class RoomType(BaseModel):
    room_type_id: int
    type_name: str
    description: str

class Room(BaseModel):
    room_id: int
    hotel_id: int
    room_number: str
    room_type_id: int
    price: float
    is_available: bool

class Guest(BaseModel):
    guest_id: int
    first_name: str
    last_name: str
    address: str
    phone: str
    email: str

class Reservation(BaseModel):
    reservation_id: int
    guest_id: int
    hotel_id: int
    room_id: int
    check_in_date: str
    check_out_date: str
    total_amount: float

