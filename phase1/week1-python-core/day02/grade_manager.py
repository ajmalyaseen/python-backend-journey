def add_student(students) -> list:
    name=input("enter student name: ")
    grade=int(input("enter your grade: "))
    subject=input("enter your subject: ")
    student={'name':name,
             'grade':grade,
             'subject':subject
             }
    students.append(student)
    return student

def get_average(students: list) -> float:
     return sum(s['grade'] for s in students) / len(students)

def top_student(students: list) -> dict:
    return max(students, key=lambda s: s['grade'])

def filter_by_grade(students: list, min_grade: int) -> list:
    return [s for s in students if s['grade'] >= min_grade]
    

def display_all(students: list) -> None:
    for s in students:
        print(f"Name: {s['name']} | Grade: {s['grade']} | Subject: {s['subject']}")

def main():
    students=[]
    while True:
        print('''\n===== STUDENT GRADE MANAGER =====

    1. Add Student
    2. View All Students
    3. Get Average Grade
    4. Top Student
    5. Filter by Grade
    6. Exit

    ''')
        option=input("Choose option(eg:1 for add studnet):")
        if option=="1":
            student=add_student(students)
            print(f"{student} | added successfully")
        elif option=="2":
            print("\ndisplaying all students")
            display_all(students)
        elif option == "3":
            if not students:
                print("No students yet!")
            else:
                print(f"Average grade: {get_average(students):.1f}")

        elif option == "4":
            if not students:
                print("No students yet!")
            else:
                top = top_student(students)
                print(f"Top student: {top['name']} with {top['grade']}")

        elif option=="5":
            try:
                grade_filter=int(input("enter grade filter (eg:60 to see baove scored 60): "))
                result=filter_by_grade(students,grade_filter)
                print(f"Students above {grade_filter}:")
                for s in result:
                 print(f"  {s['name']} - {s['grade']}")
            except TypeError:
                print("invalid input")
        elif option=="6":
            print("thank you exiting...")
            break
        else:
            print("invalid option try again") 

    
main()