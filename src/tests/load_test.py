from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    def on_start(self):
        self.register_user()
        self.login_user()

    def register_user(self):
        user_data = {
            "name": "testuser",
            "email": "testuser@example.com",
            "pwd": "password123"
        }
        response = self.client.post("/register", json=user_data)
        if response.status_code != 200:
            print(f"Failed to register user: {response.text}")
        else:
            print("User registered successfully")

    def login_user(self):
        user_data = {
            "name": "testuser",
            "email": "testuser@example.com",
            "pwd": "password123"
        }
        response = self.client.post("/login", json=user_data)
        if response.status_code == 200:
            self.token = response.json()["access_token"]
            print("User logged in successfully")
        else:
            print(f"Failed to login user: {response.text}")

    @task
    def profile(self):
        if hasattr(self, 'token'):
            headers = {"X-API-KEY": self.token}
            response = self.client.get("/profile", headers=headers)
            if response.status_code != 200:
                print(f"Failed to get profile: {response.text}")
        else:
            print("Token not set, skipping profile task")

    @task
    def search_movie(self):
        if hasattr(self, 'token'):
            headers = {"X-API-KEY": self.token}
            response = self.client.get("/movies/search?query=inception", headers=headers)
            if response.status_code != 200:
                print(f"Failed to search movie: {response.text}")
        else:
            print("Token not set, skipping search_movie task")

    @task
    def get_movie_details(self):
        if hasattr(self, 'token'):
            headers = {"X-API-KEY": self.token}
            response = self.client.get("/movies/12345", headers=headers)
            if response.status_code != 200:
                print(f"Failed to get movie details: {response.text}")
        else:
            print("Token not set, skipping get_movie_details task")

    @task
    def add_favorite_movie(self):
        if hasattr(self, 'token'):
            headers = {"X-API-KEY": self.token}
            response = self.client.post("/movies/favorites/12345", headers=headers)
            if response.status_code != 200:
                print(f"Failed to add favorite movie: {response.text}")
        else:
            print("Token not set, skipping add_favorite_movie task")

    @task
    def delete_favorite_movie(self):
        if hasattr(self, 'token'):
            headers = {"X-API-KEY": self.token}
            response = self.client.delete("/movies/favorites/12345", headers=headers)
            if response.status_code != 200:
                print(f"Failed to delete favorite movie: {response.text}")
        else:
            print("Token not set, skipping delete_favorite_movie task")

    @task
    def get_favorite_movies(self):
        if hasattr(self, 'token'):
            headers = {"X-API-KEY": self.token}
            response = self.client.get("/movies/favorites/", headers=headers)
            if response.status_code != 200:
                print(f"Failed to get favorite movies: {response.text}")
        else:
            print("Token not set, skipping get_favorite_movies task")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://api:81"
