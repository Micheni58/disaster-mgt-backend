from sqlalchemy import Column,Integer,String, Boolean, column
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(Integer, unique=True, index=True)
    password = Column(String) 
    is_active = Column(Boolean, default=True)
    role = Column(String, default="citizen")

    def __repr__(self):
        return f"<User(id={self.id}, fullname='{self.fullname}', email='{self.email}', phone_number='{self.phone_number}', role='{self.role}')>"