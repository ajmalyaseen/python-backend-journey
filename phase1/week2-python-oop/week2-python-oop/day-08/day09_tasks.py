from pydantic import BaseModel,field_validator

class User(BaseModel):
    name: str
    age: int
    email: str

# Valid data
user = User(name="ajmal", age=22, email="ajmal@gmail.com")
print(user.name)   # Ajmal
print(user.age)    # 22

# Invalid data — Pydantic catches it!
user2 = User(name="Ali", age="10", email="ali@gmail.com")
print(user2.age)
# ValidationError: age must be an integer!



class User2(BaseModel):
    name: str
    age: int
    email: str
    password: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value:str)->str:
        if "@" not in value:
            raise ValueError("Invalid email!")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value:str)->str:
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters!")
        return value

    @field_validator("age")
    @classmethod
    def validate_age(cls, value:int)->int:
        if value < 18:
            raise ValueError("Must be 18 or older!")
        return value

# ✅ Valid
user = User2(name="Ajmal", age=22, email="ajmal@gmail.com", password="secret123")

# ❌ Invalid email
user2 = User2(name="Ali", age=20, email="not@anemail", password="secret123")
# ValidationError: Invalid email!