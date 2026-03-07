
#Task1: Sort this list of products by price (lowest to highest)
products = [
    {"name": "Laptop", "price": 999},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
    {"name": "Monitor", "price": 399},
]
# Use sorted() with lambda
# Expected: Mouse → Keyboard → Monitor → Laptop

sortedproducts=sorted(products,key=lambda x:x['price'])
for item in sortedproducts:
    print(item)


#Task2: Given this list of temperatures in Celsius
temps_celsius = [0, 20, 37, 100, -10, 25]

# 1. Convert ALL to Fahrenheit using map()
temps_Fahrenheit=list(map(lambda x:(x*9/5)+32,temps_celsius))
print(temps_Fahrenheit)

# 2. Filter only temperatures above 30°C
temps_30_above=list(filter(lambda x:x>30,temps_celsius))
print(temps_30_above)

#Task3: Given two lists
students = ["Ajmal", "Ali", "Ahmed", "Sara"]
scores =   [92, 85, 97, 78]

# Create a dict: {"Ajmal": 92, "Ali": 85, ...}
result = {student: score for student, score in zip(students, scores)}
print(result)
# Then create another dict with only students who scored above 90
above_90={student:score for student,score in zip(students,scores) if score>=90}
print("above:",above_90)
#task4
scores = [85, 90, 78, 92, 45, 88]

# 1. Did everyone pass? (pass = score >= 50)
passed=all(score>=50 for score in scores )
print(f"did evryone pass:{passed}")
# 2. Did anyone get above 90?
above_90=any(score>=90 for score in scores)
print(f"did enyone get 90 above:{above_90}")
# 3. Did everyone get above 80?
above_80=all(score>=80 for score in scores)
print(f"did enyone get 80 above:{above_80}")