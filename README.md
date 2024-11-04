# Movie REST API

## Description

Movie REST API is a development test assignment for an interview.

- Python
- FastAPI
- SQLAlchemy
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
  "access_token": "token"
}
```

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
  'http://localhost:8000/movies/search?query=inception' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: your_access_token'
```

**Response:**
```json
{
  "message": "Search results:",
  "movies": [
    {
      "id": "integer",
      "title": "string",
      "description": "string"
    }
  ]
}
```

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
  "id": "integer",
  "title": "string",
  "description": "string"
}
```

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
    "id": "integer",
    "title": "string",
    "description": "string"
  }
}
```

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
  'http://localhost:8000/movies/favorites/12345' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: your_access_token'
```

**Response:**
```json
{
  "message": "Movie deleted from your favorites!",
  "data": {
    "id": "integer",
    "title": "string",
    "description": "string"
  }
}
```

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
  "message": "Your favorite movies!",
  "movies": [
    {
      "id": "integer",
      "title": "string",
      "description": "string"
    }
  ]
}
```

## Contact

- **Name:** Dimitri Simonyan
- **Email:** simadimonyan@gmail.com
- **URL:** [GitHub](https://github.com/simadimonyan)