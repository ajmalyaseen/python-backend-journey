# Day 6 — OOP: Classes, Objects & Methods

**Phase 1 | Week 2 | Object-Oriented Python**

---

## 📚 Topics Covered

- Classes and Objects — blueprint vs instance
- `__init__` — constructor method
- `self` — reference to current object
- Instance variables vs Class variables
- Dunder methods — `__str__`, `__repr__`, `__len__`, `__eq__`
- `@property` — getter and setter
- Private variables — `_protected` vs `__private`
- Method overriding
- Dataclasses — `@dataclass`

---

## 🧠 Key Concepts Learned

### Class vs Object
```python
# Class = blueprint
class BankAccount:
    pass

# Object = actual instance created from blueprint
acc1 = BankAccount("Ajmal", 1000)
acc2 = BankAccount("Ali", 500)
```

### Instance vs Class Variables
```python
class Product:
    shop_name = "Python Store"  # class variable — same for ALL products

    def __init__(self, name, price):
        self.name = name    # instance variable — unique per product
        self.price = price  # instance variable — unique per product
```

### Dunder Methods
```python
def __str__(self):   # called by print()
def __repr__(self):  # called in terminal/debugging
def __len__(self):   # called by len()
def __eq__(self):    # called by ==
```

### @property — Real World Uses
```python
# 1. Calculated values
@property
def full_name(self):
    return f"{self.first_name} {self.last_name}"

# 2. Read only attributes
@property
def balance(self):
    return self.__balance  # no setter = read only!

# 3. Validation with setter
@price.setter
def price(self, value):
    if value < 0:
        raise ValueError("Price cannot be negative!")
    self.__price = value
```

### Private Variables
```python
self._balance   # protected — convention "don't touch directly"
self.__balance  # private — name mangled, truly hidden
```

### Dataclasses
```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: float = 0.0  # default value

# Gets __init__, __repr__, __eq__ for FREE!
s = Student("Ajmal", 22, 92.5)
print(s)  # Student(name='Ajmal', age=22, grade=92.5)
```

---

## 📁 Files

| File | Description |
|------|-------------|
| `bank_account.py` | BankAccount mini project |

---

## 🛠 Mini Project — BankAccount

A full-featured bank account class with transaction history.

**Features:**
- Deposit with validation
- Withdraw with balance check
- Transfer to another account
- Read-only balance via `@property`
- Full transaction history tracking
- Clean `__str__` and `__repr__`

**Sample Output:**
```
Deposited 1000. Balance: 1100
Transferred 10 to yasi. Balance: 1090
Your Balance: 1090
Transaction History:
1. Deposit 1000
2. Transfer 10 to yasi
```

---

## 💡 Key Lessons

- `@property` makes calculated values look like attributes — no `()` needed
- `__balance` is truly private — use `_balance` for "please don't touch"
- `return` inside `@property` — never `print()`!
- Dataclass is perfect for data containers — reduces boilerplate
- Always validate in `deposit()` and `withdraw()` — never trust user input

---

## 🎤 Interview Questions Practiced

- What is the difference between `__str__` and `__repr__`?
- What is the difference between `_balance` and `__balance`?
- When would you use `@property` without a setter?
- What is a dataclass and when would you use it?

---

## ✅ Checklist

- [x] All coding tasks completed
- [x] BankAccount project built
- [x] Debugging challenge completed
- [x] Interview questions answered
- [x] LinkedIn post published
- [x] Committed to GitHub

---

**Day 7 tomorrow → Inheritance, super(), Abstract Classes** 🚀