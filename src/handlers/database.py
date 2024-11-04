from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from models.users import User
from models.favorite_movies import FavoriteMovie
from dotenv import load_dotenv
from models.base import Base
import os
import psycopg

class Database:

    def __init__(self):
        load_dotenv("/app/.env")
        password = os.getenv('POSTGRES_PASSWORD')
        movies = os.getenv('DATABASE_NAME')

        self.engine = create_engine(f'postgresql+psycopg://admin:{password}@postgres')

        # Database existence check
        with self.engine.connect() as connection:
            result = connection.execute(text(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{movies}'")).fetchone()

            if not result:
                # Outside of transaction
                conn = psycopg.connect(dbname='postgres', user='admin', password=password, host='postgres')
                conn.autocommit = True
                cursor = conn.cursor()
                cursor.execute(f"CREATE DATABASE {movies}")
                cursor.close()
                conn.close()
                print(f"База данных '{movies}' создана.")
            else:
                print(f"База данных '{movies}' уже существует.")

        self.engine = create_engine(f'postgresql+psycopg://admin:{password}@postgres/{movies}')

        Base.metadata.create_all(self.engine)

    async def add_user(self, name, email, hashed_pwd):
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            user = User(name=name, email=email, hashed_pwd=hashed_pwd)
            session.merge(user)
            session.commit()
            return user

    async def get_user_by_email(self, email):
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            return session.query(User).filter_by(email=email).first()

    async def get_user(self, user_id):
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            return session.query(User).get(user_id)

    async def add_favorite(self, user_id, kinopoisk_id, payload):
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            favorite = FavoriteMovie(user_id=user_id, kinopoisk_id=kinopoisk_id, payload=payload)
            session.merge(favorite)
            session.commit()
            return favorite
        
    async def get_favorite(self, user_id, id):
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            favorite = session.query(FavoriteMovie).filter_by(user_id=user_id, id=id).first()
            return favorite

    async def get_favorites(self, user_id):
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            records = session.query(FavoriteMovie).filter_by(user_id=user_id).all()
            return records

    async def delete_favorite(self, user_id, id):
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            favorite = session.query(FavoriteMovie).filter_by(user_id=user_id, id=id).first()
            if favorite:
                session.delete(favorite)
                session.commit()
                return favorite
            return None
