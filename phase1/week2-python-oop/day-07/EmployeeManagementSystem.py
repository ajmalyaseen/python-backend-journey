from abc import ABC, abstractmethod

class BaseEmployee(ABC):
    def __init__(self, name, email):  # init in abstract class!
        self.name = name
        self.email = email

    def __str__(self):
        return f"Name: {self.name} | Email:{self.email}" 
    @abstractmethod
    def calculate_salary(self) -> float:
        pass
    @property
    @abstractmethod
    def get_details(self) -> str:
        pass

class FullTimeEmployee(BaseEmployee):
    def __init__(self, name, email, salary):
        super().__init__(name, email)  # calls BaseEmployee __init__!
        self.salary = salary
    
    def calculate_salary(self):
        return self.salary
    @property
    def get_details(self):
        return f"{self.name} | {self.email} | {self.calculate_salary()}"

class PartTimeEmployee(BaseEmployee):
    def __init__(self,name,email,hours_worked,hourly_rate):
        super().__init__(name,email)
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate

    def calculate_salary(self):
        return self.hourly_rate*self.hours_worked
    @property
    def get_details(self):
        return f"{self.name} | {self.email} | {self.calculate_salary()}"
    
class Contractor(BaseEmployee):
    def __init__(self,name,email,days_worked,daily_rate):
        super().__init__(name,email)
        self.days_worked=days_worked
        self.daily_rate=daily_rate
        
    def calculate_salary(self):
        return self.daily_rate*self.days_worked
    
    @property
    def get_details(self):
        return f"{self.name} | {self.email} | {self.calculate_salary()}"
    

fulltimer1=FullTimeEmployee("Liyan","Liyan@gmail.com",30000)
print(fulltimer1.get_details)

parttimer1=PartTimeEmployee("Lora","Lora@gmail.com",250,85)
print(parttimer1.get_details)
contractor1=Contractor("Arjun","Arjun@gmail.com",19,800)
print(contractor1.get_details)


# Add this at the end
employees = [fulltimer1, parttimer1, contractor1]

print("\n===== EMPLOYEE SUMMARY =====")
for emp in employees:
    print(emp)  # calls __str__

total_salary = sum(emp.calculate_salary() for emp in employees)
print(f"\nTotal Salary: {total_salary}")
highest_paid = max(employees, key=lambda e: e.calculate_salary())
print(f"Highest Paid: {highest_paid.name}")