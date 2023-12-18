class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        srednia_ocen = sum(self.marks) / len(self.marks)
        return srednia_ocen > 50

student1 = Student("Jan", [60, 70, 80])
student2 = Student("Ala", [40, 30, 20])

print(student1.name, student1.is_passed())
print(student2.name, student2.is_passed())
