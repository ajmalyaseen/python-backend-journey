
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

#string tasks 

email = "ajmal.dev@gmail.com"
# Extract and print:
# 1. username → everything before @  (ajmal.dev)
username=email.split('@')[0]
print(username)
# 2. domain   → everything after @   (gmail.com)
domain=email.split("@")[1]
print(domain)
# 3. provider → just "gmail" (no .com)
provider=domain.split(".")[0]
print(provider)


# A user submitted this data - clean it up
username = "  AJMAl_YaSeeN  "
email = "  AJMAL@GMAIL.COM  "

# Print:
# cleaned username → lowercase, stripped
cleaned_username=username.strip().lower().replace("_","")
print(f"Cleaned username: {cleaned_username}")
# cleaned email    → lowercase, stripped
cleaned_email=email.strip().lower()
print(f"Cleaned email: {cleaned_email}") 
# is username alphanumeric? → True or False (remove _ first using replace)
print(cleaned_username.isalnum())
 



password = "Ajmal@123"
# Print:
# Length of password
length=len(password)
# Has digit?     → True/False  (use any(c.isdigit() for c in password))
has_digit = any(c.isdigit() for c in password)  # ✅
# Has uppercase? → True/False  (use any(c.isupper() for c in password))
has_upper = any(c.isupper() for c in password)
# Is strong?     → True if length >= 8 AND has digit AND has uppercase
is_strong=False
if length>=8 and has_digit and has_upper:
    is_strong=not is_strong

print(f"Length: {length}")
print(f"Has digit: {has_digit}")
print(f"Has uppercase: {has_upper}")
print(f"Is strong: {is_strong}")
