import sys
sys.stdout.reconfigure(encoding='utf-8')
def format_card(name, age, city, goal, skills):

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

def validate_inputs(name, age, skills):
    if not name.strip():
        raise ValueError("Name cannot be empty!")
    if age <= 0 or age > 100:
        raise ValueError("Age must be between 1 and 100!")
    if len(skills) == 0:
        raise ValueError("Skills cannot be empty!")
    return True



skills = ["Python", "FastAPI", "Git"]
try:
    validate_inputs("Ajmal", 22, skills)
    result = format_card("Ajmal", 22, "Calicut Kerala", "Pro FastAPI + AI Engineer", skills)
    print(result)
except ValueError as e:
    print(f"Error: {e}")

