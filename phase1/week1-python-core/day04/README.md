# Day 4 — Lambda, Comprehensions & Built-ins

**Phase 1 | Week 1 | Python Core**

---

## 📚 Topics Covered

- Lambda functions — when to use, syntax, real use cases
- `map()` — transform every item in a list
- `filter()` — select specific items from a list
- `zip()` — combine two or more lists together
- `enumerate()` — get index and value while looping
- Dict and Set comprehensions
- Generator expressions — lazy evaluation
- `yield` keyword — generator functions
- `any()` and `all()` — boolean checks on iterables

---

## 🧠 Key Concepts Learned

### Lambda Functions
```python
# Normal function
def square(x):
    return x ** 2

# Lambda — same thing, one line
square = lambda x: x ** 2

# Real use case — sorting by key
sorted_students = sorted(students, key=lambda s: s["grade"])
```

### map() and filter()
```python
numbers = [1, 2, 3, 4, 5]

# map() — transform every item
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# filter() — keep items matching condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]
```

### zip() — combine lists
```python
students = ["Ajmal", "Ali", "Ahmed"]
scores   = [92, 85, 97]

result = {student: score for student, score in zip(students, scores)}
# {"Ajmal": 92, "Ali": 85, "Ahmed": 97}
```

### Dict Comprehension
```python
# All items
squares = {x: x**2 for x in range(1, 6)}

# With condition — only values > 100
filtered = {k: v for k, v in data.items() if v > 100}
```

### Generator Expression vs List Comprehension
```python
# List comprehension — loads everything into memory immediately
squares_list = [x**2 for x in range(1000000)]  # heavy!

# Generator expression — creates items one by one (lazy)
squares_gen = (x**2 for x in range(1000000))   # light!
```

### yield — Generator Functions
```python
def read_large_file(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line  # one line at a time — saves memory!
```

### any() and all()
```python
scores = [85, 90, 78, 92, 45]

all(score >= 50 for score in scores)  # Did everyone pass?
any(score >= 90 for score in scores)  # Did anyone get 90+?
```

---

## 📁 Files

| File | Description |
|------|-------------|
| `day04_tasks.py` | All coding tasks for Day 4 |
| `student_report.py` | Student Report Generator mini project |

---

## 🛠 Mini Project — Student Report Generator

A report generator that ranks students by average score using functional programming.

**Sample Output:**
```
1. Ahmed  | Subject: Django  | Avg: 95.2 | Grade: A | Pass
2. Zara   | Subject: Python  | Avg: 88.2 | Grade: B | Pass
3. Ajmal  | Subject: Python  | Avg: 87.6 | Grade: B | Pass
4. Ali    | Subject: FastAPI | Avg: 73.0 | Grade: C | Pass
5. Sara   | Subject: Flask   | Avg: 50.0 | Grade: D | Pass

Top Students (avg > 85): Ahmed, Zara, Ajmal
Did everyone pass? True
Did anyone get A grade? True
```

---

## 🐛 Debugging Practice

- `reduce(numbers, lambda...)` → wrong order, function must come first
- `x % 2 = 0` → should be `==` not `=`
- `n.upper` → missing `()`, should be `n.upper()`

---

## 💡 Key Lessons

- **Variable shadowing** — never reuse variable names inside loops!
- `map()` transforms, `filter()` selects
- Generator `()` is lazy — memory efficient for large data
- `yield` pauses and resumes — perfect for large files
- `zip()` bridges separate lists together

---

## 🎤 Interview Questions Practiced

- What is the difference between `map()` and `filter()`?
- When would you use a generator instead of a list comprehension?
- What does `{k: v for k, v in data.items() if v > 100}` do?
- What is variable shadowing?

---

## ✅ Checklist

- [x] All coding tasks completed
- [x] Student Report Generator built
- [x] Debugging challenge — 3/3 bugs found
- [x] Interview questions answered
- [x] LinkedIn post published
- [x] Committed to GitHub

---

**Day 5 tomorrow → Week 1 Review + CLI Calculator Project** 🚀