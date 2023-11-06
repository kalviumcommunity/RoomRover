from pydantic import BaseModel

class BaseEntity(BaseModel):
    entity_id: int

class Hotel(BaseEntity):
    name: str
    address: str
    phone: str
    email: str
    MAX_ROOMS: int = 100

class RoomType(BaseEntity):
    type_name: str
    description: str

class Room(BaseEntity):
    hotel_id: int
    room_number: str
    room_type_id: int
    price: float
    is_available: bool

class Guest(BaseEntity):
    first_name: str
    last_name: str
    address: str
    phone: str
    email: str
    no_of_adults: int
    no_of_children: int
    MAX_PEOPLE_IN_ROOM: int = 10

class Payment(BaseEntity):
    reservation_id: int
    payment_amount: float
    payment_date: str

class Reservation(BaseEntity):
    guest_id: int
    hotel_id: int
    room_id: int
    check_in_date: str
    check_out_date: str
    total_amount: float
