from pydantic import BaseModel

class Hotel(BaseModel):
    hotel_id: int
    name: str
    address: str
    phone: str
    email: str
    MAX_ROOMS:int = 100 

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
    no_of_adults: int
    no_of_children: int

    MAX_PEOPLE_IN_ROOM: int = 10  

class Payment(BaseModel):
    payment_id: int
    reservation_id: int
    payment_amount: float
    payment_date: str

class Reservation(BaseModel):
    reservation_id: int
    guest_id: int
    hotel_id: int
    room_id: int
    check_in_date: str
    check_out_date: str
    total_amount: float

    def __del__(self):
        print(f"Reservation {self.reservation_id} deleted.")

