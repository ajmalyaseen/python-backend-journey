def get_grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def report_genrator(students:dict)->None:
    avarage=list(map(lambda x:sum(x["scores"])/len(x["scores"]),students))
    pass_or_fail=list(map(lambda x:all(score>=45 for score in x["scores"]),students))
    grade=list(map(lambda x:get_grade(x),avarage))
    print(grade)
    combined=zip(students,grade,avarage,pass_or_fail)
    sorted_students=sorted(combined,key=lambda x:x[2],reverse=True)
    for i, (student, std_grade, avg, passed) in enumerate(sorted_students, start=1):
        status = "Pass" if passed else "Fail"
        print(f"{i}. {student['name']} | Subject: {student['subject']} | Avg: {avg:.1f} | Grade: {std_grade} | {status}")
    top_students = list(filter(lambda x: x[2] > 85, sorted_students))
    print(f"\nTop Students (avg > 85): {', '.join(s[0]['name'] for s in top_students)}")
    print(f"Did everyone pass? {all(pass_or_fail)}")
    print(f"Did anyone get A grade? {any(g == 'A' for g in grade)}")


students = [
    {"name": "Ajmal",  "subject": "Python",  "scores": [85, 92, 78, 95, 88]},
    {"name": "Ali",    "subject": "FastAPI",  "scores": [72, 68, 75, 80, 70]},
    {"name": "Ahmed",  "subject": "Django",   "scores": [95, 98, 92, 97, 94]},
    {"name": "Sara",   "subject": "Flask",    "scores": [45, 52, 48, 55, 50]},
    {"name": "Zara",   "subject": "Python",   "scores": [88, 91, 85, 90, 87]},
]

report_genrator(students)