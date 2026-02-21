
#task 1
# Create these 5 variables and print each one with its type
name = "Ajmal"
age = 22
weight = 72.5
is_developer = True
data = None

# Print like this:
print(f"NAME={name} | type= {type(name)}")
print(f"AGE={age} | type= {type(age)}")
print(f"WEIGHT={weight} | type= {type(weight)}")
print(f"is_Dveloper={is_developer} | type= {type(is_developer)}")
print(f"DATA={data} | type= {type(data)}")

#task 2
# This crashes - fix it so it prints "I am 22 years old"
age = 22
print("I am " + str(age) + " years old")

#task3
# Using only f-strings, print this output:
# Name: Ajmal
# Age: 22
# Weight: 72.5 kg
# Developer: True
# Next year age: 23

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Weight: {weight} kg")
print(f"Developer: {is_developer}")
print(f"Next year age: {age + 1}")