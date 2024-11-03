from http.client import HTTPException
from models.users import UserModel
import re

class Utility:

    def __init__(self, auth):
        self.auth = auth

    async def form(self, user_form: UserModel):

        email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        name_regex = re.compile(r"^[a-zA-Z0-9_]+$")
        pwd_regex = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")

        if re.match(name_regex, user_form.name) is None:
            raise HTTPException(status_code=400, detail="The name can only contain letters, digits, and the underscore symbol!")

        if (re.match(email_regex, user_form.email) is None):
            raise HTTPException(status_code=400, detail="Email format is not correct!")

        if re.match(pwd_regex, user_form.pwd) is None:
            raise HTTPException(status_code=400, detail="The password must contain at least one letter, one digit, and be at least 8 characters long!")
        
    async def permission(self, key):
        email = await self.auth.get_decoded_email(key)
        if (email == None):
            raise HTTPException(status_code=300, detail="You don't have permission!")
        return email