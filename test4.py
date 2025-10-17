
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_mark(self, subject, score):
        self.marks[subject] = score

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def display_report(self):
        print(f"Student Name: {self.name}")
        for subject, score in self.marks.items():
            print(f"{subject}: {score}")
        print(f"Average: {self.average():.2f}")
student = Student("Josh M.C")
student.display_report()
student.add_mark("Math", 90)
student.add_mark("Science", 85)
student.add_mark("English", 95)
student.display_report()
