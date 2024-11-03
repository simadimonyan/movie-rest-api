from passlib.context import CryptContext
from dotenv import load_dotenv
import jwt
import os

class Auth:

    def __init__(self):
        load_dotenv("/app/.env")
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = os.getenv("ALGORITHM")
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # password 
    
    async def hash_psw(self, pwd):
        return self.pwd_context.hash(pwd)
    
    async def verify_pwd(self, plain_pwd, hashed_pwd) -> bool:
        return self.pwd_context.verify(plain_pwd, hashed_pwd)
    
    # jwt token

    async def create_access_token(self, data: dict):
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt
    
    async def get_decoded_email(self, token: str):
        try:
            decoded = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return decoded["email"]
        except:
            return None
        
    