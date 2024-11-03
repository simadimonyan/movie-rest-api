from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import JSONB
from models.base import Base

class FavoriteMovieModel(BaseModel):
    id: int
    user_id: int
    kinopoisk_id: int
    payload: str

class FavoriteMovie(Base):
    __tablename__ = "favorite_movies"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    kinopoisk_id = Column(Integer)
    payload = Column(JSONB)

    owner = relationship("User", back_populates="favorites")

    def __init__(self, user_id, kinopoisk_id, payload):
        self.user_id = user_id
        self.kinopoisk_id = kinopoisk_id
        self.payload = payload

    def toJSON(self):
        return {
            "movie_id": self.id,
            "payload": self.payload
        }