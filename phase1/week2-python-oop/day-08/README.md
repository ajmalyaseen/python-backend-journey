# Day 7 — Inheritance, super(), Abstract Classes & MRO

**Phase 1 | Week 2 | Object-Oriented Python**

---

## 📚 Topics Covered

- Inheritance — parent and child classes
- Method overriding — child changes parent behavior
- `super()` — calling parent class methods
- Multiple inheritance
- MRO (Method Resolution Order)
- Abstract classes — `ABC`, `@abstractmethod`
- Abstract properties — `@property` + `@abstractmethod`

---

## 🧠 Key Concepts Learned

### Inheritance
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # method overriding
        return "Woof!"

dog = Dog("Bruno", "Canine")
print(dog.speak())  # Woof! — overridden
print(dog.name)     # Bruno — inherited from Animal
```

### super().__init__()
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")  # runs Animal's __init__!
        self.breed = breed  # Dog's own variable

# Without super().__init__() — self.name and self.species never set!
```

### Multiple Inheritance & MRO
```python
class D(B, C):  # inherits from both B and C
    pass

# MRO — Python checks left to right:
# D → B → C → A → object
print(D.__mro__)  # shows exact order!
```

### Abstract Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):  # cannot be instantiated!
    
    @property
    @abstractmethod
    def area(self) -> float:
        pass  # child MUST implement this!

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.14 * self.radius ** 2

# shape = Shape()   # ❌ TypeError!
circle = Circle(5)  # ✅ works!
```

---

## 📁 Files

| File | Description |
|------|-------------|
| `day07_tasks.py` | All coding tasks for Day 7 |
| `EmployeeManagementSystem.py` | Employee system mini project |

---

## 🛠 Mini Project — Employee Management System

A full employee management system using inheritance and abstract classes.

**Class Hierarchy:**
```
BaseEmployee (Abstract)
├── FullTimeEmployee  — fixed monthly salary
├── PartTimeEmployee  — hourly rate × hours worked
└── Contractor        — daily rate × days worked
```

**Sample Output:**
```
Liyan | Liyan@gmail.com | 30000
Lora | Lora@gmail.com | 21250
Arjun | Arjun@gmail.com | 15200

===== EMPLOYEE SUMMARY =====
Name: Liyan | Email: Liyan@gmail.com
Name: Lora | Email: Lora@gmail.com
Name: Arjun | Email: Arjun@gmail.com

Total Salary: ₹66450
Highest Paid: Liyan
```

---

## 💡 Key Lessons

- Always call `super().__init__()` FIRST in child class — before adding own variables!
- Abstract class = blueprint that cannot be instantiated directly
- `@abstractmethod` forces ALL child classes to implement that method
- If base uses `@property @abstractmethod` — child must also use `@property`!
- MRO = left to right order in multiple inheritance
- `super().__init__()` missing `()` → `TypeError` — always use `super()`!

---

## 🎤 Interview Questions Practiced

- What is inheritance and why do we use it?
- What does `super().__init__()` do and why is it important?
- What is an abstract class? Can you create an object from it?
- What is MRO and why does Python need it?

---

## ✅ Checklist

- [x] All coding tasks completed
- [x] Employee Management System built
- [x] Debugging challenge completed
- [x] Interview questions answered
- [x] LinkedIn post published
- [x] Committed to GitHub

---

**Day 8 tomorrow → Pydantic v2 & Type Hints** 🚀