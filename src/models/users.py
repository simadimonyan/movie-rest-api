from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from models.base import Base

class UserModel(BaseModel):
    name: str
    email: str
    pwd: str

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    email = Column(String(256))
    hashed_pwd = Column(String(256))

    favorites = relationship("FavoriteMovie", back_populates="owner")

    def __init__(self, name, email, hashed_pwd):
        self.name = name
        self.email = email
        self.hashed_pwd = hashed_pwd

    def toJSON(self):
        return {
            "name": self.name,
            "email": self.email
        }

