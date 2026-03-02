# Schemas control what comes in and goes out of the API. 
# They are used to validate the data and to serialize the data.
# schemas/user.py
#Without schemas:
#No input validation
#No automatic Swagger docs
#No control of what password returns
#No clean separation
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    fullname: str
    email: str
    phone_number: int
    role: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True