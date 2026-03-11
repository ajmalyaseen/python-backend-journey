from pydantic import BaseModel,Field,field_validator,ValidationError
from typing import Optional, Any, List
import json
class User(BaseModel):
    name:str=Field(min_length=2,max_length=20)
    age:int=Field(gt=18)
    email:str
    password:str=Field(min_length=8)
    phone:Optional[str]=Field(default=None)

    @field_validator("email")
    @classmethod
    def email_validat(cls,value:str)->str:
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
    

def load_users(filename: str = "users.json") -> List[dict[str, Any]]:
    try:
        with open (filename,'r') as f:
            data=json.load(f)
        return data
    except FileNotFoundError:
        return []

        
def save_user(user_detail: dict[str, Any]) -> None:
    user = User.model_validate(user_detail)
    user_dict = user.model_dump()
    existing_users = load_users()  
    existing_users.append(user_dict)

    with open("users.json", "w") as f:
        json.dump(existing_users, f, indent=4)

    print(f"User {user.name} registered successfully!")

def display_users() -> None:
    users = load_users()
    if not users:
        print("No users found!")
        return
    print("\n===== REGISTERED USERS =====")
    for i, user in enumerate(users, start=1):
        print(f"{i}. {user['name']} | Age: {user['age']} | Email: {user['email']} | Phone: {user['phone'] or 'N/A'}")
    

def main():
    while True:
        print("\n===== USER REGISTRATION SYSTEM =====")
        print("1. Register User")
        print("2. View All Users")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
          try:
            name = input("Name: ")
            age = input("Age: ")
            email = input("Email: ")
            password = input("Password: ")
            phone = input("Phone (optional, press enter to skip): ") or None
            save_user({"name": name, "age": age, "email": email,"password": password, "phone": phone})
          except ValidationError as e:
              for error in e.errors():
                print(f" {error['loc'][0]}: {error['msg']}")
          except Exception as e:
               print(f"Registration failed: {e}")
        elif choice == "2":
            display_users()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

main()