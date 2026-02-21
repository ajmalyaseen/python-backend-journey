# Given this list:
students = ["Ali", "Sara", "Ajmal", "Zara", "Omar"]

# 1. Add "Riya" to the end
students.append("riya")
# 2. Insert "Hassan" at position 2
students.insert(2,"Hassan")
# 3. Remove "Sara"
students.remove("Sara")
# 4. Sort alphabetically
print(sorted(students))
# 5. Print the last student using negative indexing
print(students[-1])
# 6. Print first 3 students using slicing
print(students[:3])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehensions create:
# 1. List of squares of odd numbers only
odd_squer=[x*x for x in numbers if x%2!=0]
print(odd_squer)
# 2. List of numbers divisible by 3
divisable_by_3=[x for x in numbers if x%3==0]
print(divisable_by_3)
# 3. List of strings - "even" if even, "odd" if odd
list_of_str = ["even" if x%2==0 else "odd" for x in numbers]
print(list_of_str)


# Create a student dict with: name, age, grade, subjects(list)
student={
    'name':'yaseen',
    'age':20,
    'grade':'A',
    'subjects':['maths','python','java']
}
# 1. Print all keys
print(student.keys())
# 2. Print all values
print(student.values())
# 3. Add "email" key
student["email"]="ajmal@gmail.com"
# 4. Update grade
student["grade"]="B"

# 5. Loop and print each key: value
for key,value in student.items():
    print(f"{key}:{value}")
# 6. Safely get a key that doesn't exist with default message
print(student.get("city","key not found"))

python_devs  = {"Ajmal", "Ali", "Sara", "Zara"}
fastapi_devs = {"Ali", "Hassan", "Zara", "Omar"}

# 1. Who knows BOTH Python and FastAPI?
print(python_devs & fastapi_devs)
# 2. All developers combined (no duplicates)
print(python_devs | fastapi_devs)
# 3. Python devs who don't know FastAPI
print(python_devs - fastapi_devs)
# 4. Add "Riya" to python_devs
python_devs.add("Riya")
print(python_devs)