# Day 3 — Functions, Error Handling, File I/O & JSON

**Phase 1 | Week 1 | Python Core**

---

## 📚 Topics Covered

- Functions — default arguments, `*args`, `**kwargs`
- Error handling — `try`, `except`, `else`, `finally`
- Custom exceptions and raising errors
- File I/O — read, write, append modes with `with` statement
- JSON — `json.dump()`, `json.load()`, `json.dumps()`, `json.loads()`
- Timestamps with `datetime` module

---

## 🧠 Key Concepts Learned

### `*args` vs `**kwargs`
```python
def example(*args, **kwargs):
    print(args)    # tuple → (1, 2, 3)
    print(kwargs)  # dict  → {'name': 'Ajmal'}

example(1, 2, 3, name="Ajmal")
```

### try / except / else / finally
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("runs if error occurs")
else:
    print("runs if NO error occurs")
finally:
    print("ALWAYS runs — cleanup here")
```

### File I/O with `with` statement
```python
# Write
with open("file.txt", "w") as f:
    f.write("Hello!")

# Read
with open("file.txt", "r") as f:
    content = f.read()
```

### JSON
```python
import json

# Dict → File
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# File → Dict
with open("data.json", "r") as f:
    data = json.load(f)
```

---

## 📁 Files

| File | Description |
|------|-------------|
| `day3_tasks.py` | All coding tasks for Day 3 |
| `task_manager.py` | JSON Task Manager mini project |

---

## 🛠 Mini Project — JSON Task Manager

> Full project lives in its own repo: [json-task-manager](https://github.com/ajmalyaseen/json-task-manager)

A CLI task manager that persists data using JSON file storage.

**Features:**
- Add tasks with automatic timestamp
- View all tasks
- Mark tasks as complete
- Delete tasks
- View pending tasks only
- Data persists between runs

---

## 🐛 Debugging Practice

Found and fixed bugs in broken code — no running allowed!

**Bugs caught today:**
- Missing `:` after `for` loop
- Wrong operator `=+` instead of `+=`
- Wrong variable case (`Average` vs `average`)
- Missing empty list guard for division by zero
- `json.dumps()` instead of `json.dump()` for file writing
- Wrong file mode `"a"` instead of `"w"` for JSON

---

## 🎤 Interview Questions Practiced

- What is the difference between `json.dump()` and `json.loads()`?
- What does the `with` statement do when opening a file?
- What error must you always handle when reading a file?
- What is the difference between `except`, `else`, and `finally`?

---

## ✅ Checklist

- [x] All coding tasks completed
- [x] Mini project built and pushed to separate repo
- [x] Debugging challenge completed
- [x] Interview questions answered
- [x] LinkedIn post published
- [x] Committed to GitHub

---

## 📝 Personal Notes

- `finally` should NEVER have a `return` statement — it overrides all other returns!
- Always use `"w"` mode for JSON files — `"a"` mode breaks JSON structure
- `with` statement automatically closes files even if an error occurs
- Use `not numbers` instead of `len(numbers) == 0` — more Pythonic!

---

**Day 4 tomorrow → Lambda, map(), filter(), comprehensions** 🚀