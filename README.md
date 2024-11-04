# Movie REST API

## Description

Movie REST API is a development test assignment for an interview.

Asynchronous RESTful API service that allows users to register, authenticate, and manage a list of their favorite movies. Integrated with Kinopoisk Unofficial API to get information about movies: https://kinopoiskapiunofficial.tech

- Python
- FastAPI
- SQLAlchemy
- Kinopoisk Unofficial API
- AsyncIO
- Locust
- Httpx
- Docker
- Git


## Installation

1. Clone the repository.
```bash
sudo git clone https://github.com/simadimonyan/movie-rest-api.git
```

2. Uncomment and configure the example.env file.
```
Open the example.env file.
Replace the placeholder values with your own data.
Save the file as .env.
```

3. Compose the project.
```bash
sudo docker compose up
```

## Swagger Docs

![alt text](/docs/image.jpg)

## Load Test on 100 users by Locust

![alt text](/docs/test.jpg)

## Development Test Assignment

- [Task](/docs/Task.pdf)

## API

### User Registration

**URL:** `POST /register`

**Summary:** Register a new user in the system.

**Tags:** `user`

**Request Body:**
```json
{
  "name": "user",
  "email": "test@gmail.com",
  "pwd": "ps123456789"
}
```

**Request:**
```bash
curl -X 'POST' \
  'http://localhost:8000/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "user",
  "email": "test@gmail.com",
  "pwd": "ps123456789"
}'
```

**Response:**
```json
{
  "message": "User created!",
  "user_data": {
    "name": "user",
    "email": "test@gmail.com"
  }
}
```

---

### User Login

**URL:** `POST /login`

**Summary:** Log in and get an access token.

**Tags:** `user`

**Request Body:**
```json
{
  "name": "user",
  "email": "test@gmail.com",
  "pwd": "ps123456789"
}
```

**Request:**
```bash
curl -X 'POST' \
  'http://localhost:8000/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "test@gmail.com",
  "pwd": "ps123456789"
}'
```

**Response:**
```json
{
  "message": "Login successful!",
  "access_token": "JWT-Token"
}
```

---

### Get User Profile

**URL:** `GET /profile`

**Summary:** Get user profile information.

**Tags:** `profile`

**Headers:**
- `X-API-KEY`: `string` (Required)

**Request:**
```bash
curl -X 'GET' \
  'http://localhost:8000/profile' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: your_access_token'
```

**Response:**
```json
{
  "message": "Your profile info:",
  "id": "integer",
  "data": {
    "id": "1",
    "name": "user",
    "email": "test@gmail.com",
  }
}
```

---

### Search Movies

**URL:** `GET /movies/search`

**Summary:** Search for movies.

**Tags:** `movies`

**Query Parameters:**
- `query`: `string` (Required)

**Headers:**
- `X-API-KEY`: `string` (Required)

**Request:**
```bash
curl -X 'GET' \
  'http://localhost:8000/movies/search?query=%D0%A4%D0%BE%D1%80%D0%B5%D1%81%D1%82%20%D0%93%D0%B0%D0%BC%D0%B0' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: your_access_token'
```

**Response:**
```json
{
  "message": "Search results:",
  "movies": [
      {
        "kinopoiskId": 301,
        "kinopoiskHDId": "4824a95e60a7db7e86f14137516ba590",
        "imdbId": "tt0133093",
        "nameRu": "Матрица",
        "nameEn": "The Matrix",
        "nameOriginal": "The Matrix",
        "posterUrl": "https://kinopoiskapiunofficial.tech/images/posters/kp/301.jpg",
        "posterUrlPreview": "https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg",
        "coverUrl": "https://avatars.mds.yandex.net/get-ott/1672343/2a0000016cc7177239d4025185c488b1bf43/orig",
        "logoUrl": "https://avatars.mds.yandex.net/get-ott/1648503/2a00000170a5418408119bc802b53a03007b/orig",
        "reviewsCount": 293,
        "ratingGoodReview": 88.9,
        "ratingGoodReviewVoteCount": 257,
        "ratingKinopoisk": 8.5,
        "ratingKinopoiskVoteCount": 524108,
        "ratingImdb": 8.7,
        "ratingImdbVoteCount": 1729087,
        "ratingFilmCritics": 7.8,
        "ratingFilmCriticsVoteCount": 155,
        "ratingAwait": 7.8,
        "ratingAwaitCount": 2,
        "ratingRfCritics": 7.8,
        "ratingRfCriticsVoteCount": 31,
        "webUrl": "https://www.kinopoisk.ru/film/301/",
        "year": 1999,
        "filmLength": 136,
        "slogan": "Добро пожаловать в реальный мир",
        "description": "Жизнь Томаса Андерсона разделена на две части:",
        "shortDescription": "Хакер Нео узнает, что его мир — виртуальный. Выдающийся экшен, доказавший, что зрелищное кино может быть умным",
        "editorAnnotation": "Фильм доступен только на языке оригинала с русскими субтитрами",
        "isTicketsAvailable": false,
        "productionStatus": "POST_PRODUCTION",
        "type": "FILM",
        "ratingMpaa": "r",
        "ratingAgeLimits": "age16",
        "hasImax": false,
        "has3D": false,
        "lastSync": "2021-07-29T20:07:49.109817",
        "countries": [
            {
            "country": "США"
            }
        ],
        "genres": [
            {
            "genre": "фантастика"
            }
        ],
        "startYear": 1996,
        "endYear": 1996,
        "serial": false,
        "shortFilm": false,
        "completed": false       
    }
  ]
}
```

---

### Get Movie Details

**URL:** `GET /movies/{movie_id}`

**Summary:** Get details of a specific movie.

**Tags:** `movies`

**Path Parameters:**
- `movie_id`: `integer` (Required, between 1 and 7000000)

**Headers:**
- `X-API-KEY`: `string` (Required)

**Request:**
```bash
curl -X 'GET' \
  'http://localhost:8000/movies/12345' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: your_access_token'
```

**Response:**
```json
{
  "kinopoiskId": 12345,
  "kinopoiskHDId": null,
  "imdbId": "tt0089175",
  "nameRu": "Ночь страха",
  "nameEn": null,
  "nameOriginal": "Fright Night",
  "posterUrl": "https://kinopoiskapiunofficial.tech/images/posters/kp/12345.jpg",
  "posterUrlPreview": "https://kinopoiskapiunofficial.tech/images/posters/kp_small/12345.jpg",
  "coverUrl": null,
  "logoUrl": null,
  "reviewsCount": 24,
  "ratingGoodReview": 86,
  "ratingGoodReviewVoteCount": 17,
  "ratingKinopoisk": 6.8,
  "ratingKinopoiskVoteCount": 7776,
  "ratingImdb": 7.1,
  "ratingImdbVoteCount": 80649,
  "ratingFilmCritics": 7.2,
  "ratingFilmCriticsVoteCount": 64,
  "ratingAwait": null,
  "ratingAwaitCount": 0,
  "ratingRfCritics": null,
  "ratingRfCriticsVoteCount": 0,
  "webUrl": "https://www.kinopoisk.ru/film/12345/",
  "year": 1985,
  "filmLength": 106,
  "slogan": "There are some very good reasons to be afraid...of the dark.",
  "description": "Юный поклонник ужастиков по имени Чарли обнаруживает, что его сосед — вампир. Хуже того, соседу не нравится, что кто-то знает его тайну, поэтому жизнь парня оказывается под вопросом. Полностью отчаявшись, Чарли обращается за помощью к Питеру Винсенту — ведущему программы «Ночь страха», который якобы знает о вампирах всё.",
  "shortDescription": null,
  "editorAnnotation": null,
  "isTicketsAvailable": false,
  "productionStatus": null,
  "type": "FILM",
  "ratingMpaa": "r",
  "ratingAgeLimits": "age18",
  "countries": [
    {
      "country": "США"
    }
  ],
  "genres": [
    {
      "genre": "фэнтези"
    },
    {
      "genre": "ужасы"
    }
  ],
  "startYear": null,
  "endYear": null,
  "serial": false,
  "shortFilm": false,
  "completed": false,
  "hasImax": false,
  "has3D": false,
  "lastSync": "2024-10-13T11:39:49.633167"
}
```

---

### Add Favorite Movie

**URL:** `POST /movies/favorites/{movie_id}`

**Summary:** Add a movie to favorites.

**Tags:** `movies`

**Path Parameters:**
- `movie_id`: `integer` (Required, between 300 and 7000000)

**Headers:**
- `X-API-KEY`: `string` (Required)

**Request:**
```bash
curl -X 'POST' \
  'http://localhost:8000/movies/favorites/12345' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: your_access_token'
```

**Response:**
```json
{
  "message": "Movie added to favorites!",
  "payload": {
    "kinopoiskId": 12345,
    "kinopoiskHDId": null,
    "imdbId": "tt0089175",
    "nameRu": "Ночь страха",
    "nameEn": null,
    "nameOriginal": "Fright Night",
    "posterUrl": "https://kinopoiskapiunofficial.tech/images/posters/kp/12345.jpg",
    "posterUrlPreview": "https://kinopoiskapiunofficial.tech/images/posters/kp_small/12345.jpg",
    "coverUrl": null,
    "logoUrl": null,
    "reviewsCount": 24,
    "ratingGoodReview": 86,
    "ratingGoodReviewVoteCount": 17,
    "ratingKinopoisk": 6.8,
    "ratingKinopoiskVoteCount": 7776,
    "ratingImdb": 7.1,
    "ratingImdbVoteCount": 80649,
    "ratingFilmCritics": 7.2,
    "ratingFilmCriticsVoteCount": 64,
    "ratingAwait": null,
    "ratingAwaitCount": 0,
    "ratingRfCritics": null,
    "ratingRfCriticsVoteCount": 0,
    "webUrl": "https://www.kinopoisk.ru/film/12345/",
    "year": 1985,
    "filmLength": 106,
    "slogan": "There are some very good reasons to be afraid...of the dark.",
    "description": "Юный поклонник ужастиков по имени Чарли обнаруживает, что его сосед — вампир. Хуже того, соседу не нравится, что кто-то знает его тайну, поэтому жизнь парня оказывается под вопросом. Полностью отчаявшись, Чарли обращается за помощью к Питеру Винсенту — ведущему программы «Ночь страха», который якобы знает о вампирах всё.",
    "shortDescription": null,
    "editorAnnotation": null,
    "isTicketsAvailable": false,
    "productionStatus": null,
    "type": "FILM",
    "ratingMpaa": "r",
    "ratingAgeLimits": "age18",
    "countries": [
        {
        "country": "США"
        }
    ],
    "genres": [
        {
        "genre": "фэнтези"
        },
        {
        "genre": "ужасы"
        }
    ],
    "startYear": null,
    "endYear": null,
    "serial": false,
    "shortFilm": false,
    "completed": false,
    "hasImax": false,
    "has3D": false,
    "lastSync": "2024-10-13T11:39:49.633167"
  }
}
```

---

### Delete Favorite Movie

**URL:** `DELETE /movies/favorites/{movie_id}`

**Summary:** Delete a movie from favorites.

**Tags:** `movies`

**Path Parameters:**
- `movie_id`: `integer` (Required, greater than or equal to 1)

**Headers:**
- `X-API-KEY`: `string` (Required)

**Request:**
```bash
curl -X 'DELETE' \
  'http://localhost:8000/movies/favorites/1' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: your_access_token'
```

**Response:**
```json
{
  "message": "Movie deleted from your favorites!",
  "data": {
    "kinopoiskId": 12345,
    "kinopoiskHDId": null,
    "imdbId": "tt0089175",
    "nameRu": "Ночь страха",
    "nameEn": null,
    "nameOriginal": "Fright Night",
    "posterUrl": "https://kinopoiskapiunofficial.tech/images/posters/kp/12345.jpg",
    "posterUrlPreview": "https://kinopoiskapiunofficial.tech/images/posters/kp_small/12345.jpg",
    "coverUrl": null,
    "logoUrl": null,
    "reviewsCount": 24,
    "ratingGoodReview": 86,
    "ratingGoodReviewVoteCount": 17,
    "ratingKinopoisk": 6.8,
    "ratingKinopoiskVoteCount": 7776,
    "ratingImdb": 7.1,
    "ratingImdbVoteCount": 80649,
    "ratingFilmCritics": 7.2,
    "ratingFilmCriticsVoteCount": 64,
    "ratingAwait": null,
    "ratingAwaitCount": 0,
    "ratingRfCritics": null,
    "ratingRfCriticsVoteCount": 0,
    "webUrl": "https://www.kinopoisk.ru/film/12345/",
    "year": 1985,
    "filmLength": 106,
    "slogan": "There are some very good reasons to be afraid...of the dark.",
    "description": "Юный поклонник ужастиков по имени Чарли обнаруживает, что его сосед — вампир. Хуже того, соседу не нравится, что кто-то знает его тайну, поэтому жизнь парня оказывается под вопросом. Полностью отчаявшись, Чарли обращается за помощью к Питеру Винсенту — ведущему программы «Ночь страха», который якобы знает о вампирах всё.",
    "shortDescription": null,
    "editorAnnotation": null,
    "isTicketsAvailable": false,
    "productionStatus": null,
    "type": "FILM",
    "ratingMpaa": "r",
    "ratingAgeLimits": "age18",
    "countries": [
        {
        "country": "США"
        }
    ],
    "genres": [
        {
        "genre": "фэнтези"
        },
        {
        "genre": "ужасы"
        }
    ],
    "startYear": null,
    "endYear": null,
    "serial": false,
    "shortFilm": false,
    "completed": false,
    "hasImax": false,
    "has3D": false,
    "lastSync": "2024-10-13T11:39:49.633167"
  }
}
```

---

### Get Favorite Movies

**URL:** `GET /movies/favorites/`

**Summary:** Get a list of favorite movies.

**Tags:** `movies`

**Headers:**
- `X-API-KEY`: `string` (Required)

**Request:**
```bash
curl -X 'GET' \
  'http://localhost:8000/movies/favorites/' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: your_access_token'
```

**Response:**
```json
{
  {
  "message": "Your favorite movies!",
  "movies": []
  }
}
```

---

## Contact

- **Name:** Dimitri Simonyan
- **Email:** simadimonyan@gmail.com
- **URL:** [GitHub](https://github.com/simadimonyan)