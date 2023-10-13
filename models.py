from pydantic import BaseModel

class Hotel(BaseModel):
    def _init_(self,hotel_id: int, name: str, address: str, phone: str,email: str):
        self.hotel_id = hotel_id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        
class RoomType(BaseModel):
    def _init_(self,room_type_id: int, type_name: str, description: str):
        self.room_type_id:room_type_id
        self.type_name: type_name
        self.description:description
    

class Room(BaseModel):
    def _init_(self, room_id: int, hotel_id: int, room_number: str, room_type_id: int,price: float,is_available: bool):
        self.room_id: room_id
        self.hotel_id: hotel_id
        self.room_number: room_number
        self.room_type_id: room_type_id
        self.price: price
        self.is_available: is_available

class Guest(BaseModel):
    def _init_(self,guest_id: int, first_name: str, last_name: str, address: str, phone: str, email: str, no_of_adults: int, no_of_children: int,max_people_in_room: int = 2):
       self. guest_id: guest_id
       self.first_name: first_name
       self.last_name: last_name
       self.address: address
       self.phone: phone
       self.email: email
       self.no_of_adults: no_of_adults
       self.no_of_children: no_of_children
       self.max_people_in_room: max_people_in_room
    

class Payment(BaseModel):
    def _init_(self,payment_id: int, reservation_id: int,payment_amount: float,payment_date: str):
        self.payment_id: payment_id
        self.reservation_id: reservation_id
        self.payment_amount: payment_amount
        self.payment_date: payment_date

class Reservation(BaseModel):
    def _init_(self,reservation_id: int,guest_id: int,hotel_id: int,room_id: int,check_in_date: str,check_out_date: str,total_amount: float):
        self.reservation_id: reservation_id
        self.guest_id: guest_id
        self.hotel_id: hotel_id
        self.room_id: room_id
        self.check_in_date: check_in_date
        self.check_out_date: check_out_date
        self.total_amount: total_amount

    
    def _del_(self):
        print(f"Reservation {self.reservation_id} deleted.")