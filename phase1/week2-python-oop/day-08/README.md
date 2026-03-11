# Day 8 — Pydantic v2 & Type Hints

**Phase 1 | Week 2 | Object-Oriented Python**

---

## 📚 Topics Covered

- Type hints — `str`, `int`, `float`, `bool`, `Optional`, `Union`, `List`, `Dict`
- Pydantic `BaseModel` — automatic validation
- `Field()` — advanced constraints (`gt`, `ge`, `lt`, `le`, `min_length`, `max_length`)
- `field_validator` — custom validation logic
- `model_dump()` — Pydantic model → dict
- `model_validate()` — dict → Pydantic model
- `ValidationError` — catching Pydantic errors cleanly
- `model_config` — `ConfigDict`, `from_attributes`, `str_strip_whitespace`
- Nested Pydantic models

---

## 🧠 Key Concepts Learned

### Type Hints
```python
from typing import Optional, Union, List, Dict, Any

name: str = "Ajmal"
age: int = 22
phone: Optional[str] = None      # str or None
scores: list[int] = [85, 90]
data: dict[str, int] = {"age": 22}
```

### Pydantic BaseModel
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

user = User(name="Ajmal", age=22, email="ajmal@gmail.com")
print(user.name)  # Ajmal

# Auto type conversion
user2 = User(name="Ali", age="22", email="ali@gmail.com")
# "22" → 22 automatically! ✅
```

### Field() — Constraints
```python
from pydantic import Field

class Product(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0)       # greater than 0
    quantity: int = Field(ge=0)      # greater than or equal to 0
    discount: float = Field(le=100)  # less than or equal to 100
```

### field_validator — Custom Validation
```python
from pydantic import field_validator

@field_validator("email")
@classmethod
def validate_email(cls, value: str) -> str:
    if "@" not in value:
        raise ValueError("Invalid email!")
    return value
```

### model_dump() and model_validate()
```python
# Pydantic → dict
user_dict = user.model_dump()

# dict → Pydantic
user = User.model_validate(user_dict)
```

### Catching ValidationError
```python
from pydantic import ValidationError

try:
    user = User.model_validate(data)
except ValidationError as e:
    for error in e.errors():
        print(f"❌ {error['loc'][0]}: {error['msg']}")
```

### model_config
```python
from pydantic import ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,  # "  Ajmal  " → "Ajmal"
        from_attributes=True,       # works with ORM objects
    )
```

---

## 📁 Files

| File | Description |
|------|-------------|
| `day08_tasks.py` | All coding tasks for Day 8 |
| `UserRegistrationSystem.py` | User Registration mini project |

---

## 🛠 Mini Project — User Registration System

A full user registration system with Pydantic validation and JSON persistence.

**Validations:**
- Name — min 2, max 20 characters
- Age — must be greater than 18
- Email — must contain @
- Password — minimum 8 characters
- Phone — optional

**Sample Output:**
```
===== USER REGISTRATION SYSTEM =====
1. Register User
2. View All Users
3. Exit

Name: ajmal
Age: 10
Email: anai
Password: ajm

❌ age: Input should be greater than 18
❌ email: Value error, Invalid email!
❌ password: String should have at least 8 characters

User ajmal registered successfully!

===== REGISTERED USERS =====
1. ajmal | Age: 20 | Email: ajmal@gmail.com | Phone: N/A
```

---

## 💡 Key Lessons

- Never use `int(input())` — let Pydantic handle type conversion!
- `ValidationError` catches ALL Pydantic failures — one except block is enough!
- `field_validator` needs `@classmethod` — always!
- `model_dump()` → out as dict, `model_validate()` → in from dict
- `Optional[str]` = `str | None` — user doesn't have to provide it
- `gt=0` → 0 not allowed, `ge=0` → 0 allowed

---

## 🎤 Interview Questions Practiced

- What is Pydantic and why do we use it?
- What is the difference between `Field(gt=0)` and `Field(ge=0)`?
- What does `model_dump()` do?
- When would you use `field_validator` instead of just `Field()`?

---

## ✅ Checklist

- [x] All coding tasks completed
- [x] User Registration System built
- [x] Pydantic validation working correctly
- [x] Interview questions answered
- [x] LinkedIn post published
- [x] Committed to GitHub

---

**Day 9 tomorrow → Decorators & Context Managers** 🚀