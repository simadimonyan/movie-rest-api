from fastapi import *
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader
from handlers.auth import Auth 
from handlers.database import Database
from models.users import UserModel
from handlers.kinopoisk import Kinopoisk
from handlers.utility import Utility


app = FastAPI(
    title="Movie REST API",
    version="1",
    contact={
        "name": "Dimitri Simonyan",
        "email": "simadimonyan@gmail.com",
        "url": " https://github.com/simadimonyan"
    }
)
auth = Auth()
db = Database()
kinopoisk = Kinopoisk()
utility = Utility(auth)

header_scheme = APIKeyHeader(name="X-API-KEY")


# user 

@app.post("/register", summary="Зарегистрироваться в системе", tags=["user"])
async def register(user_form: UserModel):

    # register validation
    await utility.form(user_form)

    if (await db.get_user_by_email(user_form.email) != None):
        raise HTTPException(status_code=400, detail="User already registered!")

    user = await db.add_user(user_form.name, user_form.email, await auth.hash_psw(user_form.pwd))
    return JSONResponse({ "message": "User created!", "user_data": user.toJSON()})


@app.post("/login", summary="Войти в систему и получить токен", tags=["user"])
async def login(user_form: UserModel):
    
    # register validation
    await utility.form(user_form)

    user = await db.get_user_by_email(user_form.email)
    if (user is None):
        raise HTTPException(status_code=400, detail="User is not registered!")

    if (await auth.verify_pwd(user_form.pwd, user.hashed_pwd) == False):
        raise HTTPException(status_code=400, detail="Incorrect email or password!")

    token = await auth.create_access_token({"name": user_form.name, "email": user_form.email})

    return JSONResponse({ "message": "Login successfull!", "access_token": token })


# profile 

@app.get("/profile", summary="Мой профиль", tags=["profile"])
async def profile(key = Depends(header_scheme)):

    # permission check
    email = await utility.permission(key)

    profile = await db.get_user_by_email(email=email)
    return JSONResponse({ "message": "Your profile info:", "id": profile.id, "data": profile.toJSON() })


# movies

@app.get("/movies/search", summary="Поиск фильмов", tags=["movies"])
async def search_movie(query, key = Depends(header_scheme)):

    # permission check
    await utility.permission(key)
    
    return await kinopoisk.search_movie(query)


@app.get("/movies/{movie_id}", summary="Детали фильма", tags=["movies"])
async def search_movie(movie_id: int = Path(ge=1, le=7000000), key = Depends(header_scheme)):
    
    # permission check
    await utility.permission(key)

    return await kinopoisk.get_movie(movie_id)


@app.post("/movies/favorites/{movie_id}", summary="Добавить фильм в избранные", tags=["movies"])
async def add_favorites(movie_id: int = Path(ge=300, le=7000000), key = Depends(header_scheme)):
    email = await auth.get_decoded_email(key)
    if (email == None):
        raise HTTPException(status_code=400, detail="You don't have permission!")
    profile = await db.get_user_by_email(email=email)
    payload = await kinopoisk.get_movie(movie_id)

    if (await db.get_favorite(profile.id, movie_id) is not None):
        raise HTTPException(status_code=400, detail="You already saved the favorite movie!")
    
    await db.add_favorite(profile.id, movie_id, payload)

    return JSONResponse({ "message": "Movie added to favorites!", "payload": payload })


@app.delete("/movies/favorites/{movie_id}", summary="Удалить фильм из избранных", tags=["movies"])
async def delete_favorites(movie_id: int = Path(ge=1), key = Depends(header_scheme)):

    # permission check
    email = await utility.permission(key)

    profile = await db.get_user_by_email(email=email)

    deleted = await db.delete_favorite(profile.id, movie_id)

    if (deleted == None):
        raise HTTPException(status_code=400, detail="Movie is not in your favorites!")

    return JSONResponse({ "message": "Movie deleted from your favorites!", "data": deleted.payload})


@app.get("/movies/favorites/", summary="Посмотреть избранные фильмы", tags=["movies"])
async def get_favorites(key = Depends(header_scheme)):

    # permission check
    email = await utility.permission(key)

    profile = await db.get_user_by_email(email=email)
    records = await db.get_favorites(profile.id)

    return JSONResponse({ "message": "Your favorite movies!", "movies": [m.toJSON() for m in records] })