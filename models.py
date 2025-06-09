from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Grades(BaseModel):
    date: datetime
    grade: str
    score: int

class Address(BaseModel):
    building: str
    coord: list[float]
    street: str
    zipcode: int

class Restaurant(BaseModel):
    id: Optional[str] = Field(default_factory=str, alias="_id")
    address: Address
    borough: str
    cuisine: str
    grades: list[Grades]
    name: str
    restaurant_id: int

