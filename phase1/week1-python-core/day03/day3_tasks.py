# Write a function that accepts any number of scores
# and returns a dict with min, max, average

def analyze_scores(*args):
    numbers=list(args)
    if not numbers:
        return f"please provide input"

    min_val=min(numbers)
    max_val=max(numbers)
    avg_val=sum(numbers)/len(numbers)
    return {'min': min_val, 'max': max_val, 'average': avg_val}

print(analyze_scores(85, 90, 78, 92, 88))
# Output: {'min': 78, 'max': 92, 'average': 86.6}

""" task 2 """

# Fix this function to handle ALL possible errors gracefully
# Must handle:
# - division by zero
# - non-number inputs like divide("a", 2)
def divide(a, b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        return f"Cannot divided by zero"
    except TypeError:
        return f"invalid input..!"
    finally:
        print("program completed") 
print(divide(20,10))

#task3
import json

def save_data(filename, data):
    with open (filename,"w") as f:
        json.dump(data,f,indent=4)


def load_data(filename):
    try:
        with open (filename,"r")as f:
            data=json.load(f)
            return data
    except FileNotFoundError:
        return f"File not found"


student = {"name": "Ajmal", "age": 22, "skills": ["Python", "FastAPI"]}
save_data("student.json", student)
print(load_data("student.json"))
print(load_data("missing.json"))  

""" 
output:
{'name': 'Ajmal', 'age': 22, 'skills': ['Python', 'FastAPI']}
File not found

"""

