import dataclasses
from datetime import date
from enum import Enum

class Hobby(Enum):
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


@dataclasses.dataclass
class User:

    full_name: str
    email: str
    gender: str
    number: str
    date_of_birth: date
    subject: str
    hobbies: list[Hobby]
    upload_file: str
    address: str
    state_city: str
    permanent_address: str

admin = User(
    full_name="John Smith",
    email="admin@mail.com",
    gender="Male",
    number="7985258684",
    date_of_birth=date(1994, 11, 10),
    subject="Maths, Computer Science",
    hobbies=[Hobby.SPORTS, Hobby.READING],
    upload_file="kapi.jpg",
    address="Finland, Central Street, 25, 13",
    state_city="Haryana Karnal",
    permanent_address = "Finland, Qqq Street, 455, 1"
)

guest = User(
    full_name="Margot Robbie",
    email="qwerty@mail.com",
    gender="Female",
    number="1234567890",
    date_of_birth=date(1988, 3, 5),
    subject="Computer Science",
    hobbies=[Hobby.MUSIC],
    upload_file="kapi.jpg",
    address="USA, Central Street, 12, 12",
    state_city="NCR Delhi",
    permanent_address = "USA, Wash Street, 455, 1"
)