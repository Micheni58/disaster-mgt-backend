from sqlalchemy import column,Integer,String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = column(Integer, primary_key=True, index=True)
    fullname = column(String, index=True)
    email = column(String, unique=True, index=True)
    phone_number = column(Integer, unique=True, index=True)
    password = column(String) 
    confirm_password = column(String)
    is_active = column(Boolean, default=True)
    role = column(String, default="citizen")

    def __repr__(self):
        return f"<User(id={self.id}, fullname='{self.fullname}', email='{self.email}', phone_number='{self.phone_number}', role='{self.role}')>"