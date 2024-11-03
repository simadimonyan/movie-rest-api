from dotenv import load_dotenv
import httpx
import os

class Kinopoisk:

    def __init__(self):
        load_dotenv("/app/.env")
        self.key = os.getenv('API_KEY')

    # search the movie

    async def search_movie(self, name):
        url = 'https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword'
        params = {'keyword': name}
        headers = {
            'accept': 'application/json',
            'X-API-KEY': self.key
        }
        response = httpx.get(url=url, params=params, headers=headers)
        return response.json()

    # movie details 

    async def get_movie(self, movie_id):
        url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{movie_id}' 
        headers = {
            'accept': 'application/json',
            'X-API-KEY': self.key
        }
        response = httpx.get(url=url, headers=headers)
        return response.json()

