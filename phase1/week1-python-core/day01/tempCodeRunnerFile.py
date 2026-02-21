import sys
sys.stdout.reconfigure(encoding='utf-8')

def validate_inputs(name: str, age: int, skills: list[str]) -> bool:
    if not name.strip():
        raise ValueError("Name cannot be empty")
    if age < 0 or age > 100:
        raise ValueError("Age must be between 0 and 120")
    if not skills or len(skills) == 0:
        raise ValueError("Skills list cannot be empty")
    return True

def format_card(name: str, age: int, city: str, goal: str, skills: list[str]) -> str:
    skills_str = " | ".join(skills)
    
    # Build the card using f-strings directly
    card = f"""
    ╔══════════════════════════════════════╗
    ║      DEVELOPER PROFILE CARD          ║
    ╠══════════════════════════════════════╣
    ║  Name  : {name}
    ║  Age   : {age}
    ║  City  : {city}
    ║  Goal  : {goal}
    ║  Skills: {skills_str}
    ╚══════════════════════════════════════╝"""
    return card


name  = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Age must be a number!")
    exit()
city  = input("Enter your city: ")
goal  = input("Enter your goal: ")
skills_input = input("Enter skills (comma separated): ")
skills = [s.strip() for s in skills_input.split(",")]

try:
    validate_inputs(name, age, skills)
    result = format_card(name, age, city, goal, skills)
    print(result)
except ValueError as e:
    print(f"Error: {e}")