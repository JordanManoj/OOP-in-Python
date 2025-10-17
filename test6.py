
class Employee:
    company_name = "Cloud Orbot Technology"

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def apply_raise(self, percent):
        self.salary *= (1 + percent / 100)

    def display_details(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: Rs{self.salary:.2f}, Company: {Employee.company_name}")

emp1 = Employee("Aine Ann", "Drug engineer", 80000)
emp2 = Employee("Jordan Manoj", "Data Scientist", 100000)

print("salary before Raise:")
emp1.display_details()
emp2.display_details()
emp1.apply_raise(10)
emp2.apply_raise(15)
print("\nsalary after Raise:")
emp1.display_details()
emp2.display_details()