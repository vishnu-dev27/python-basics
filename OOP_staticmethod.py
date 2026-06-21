class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def has_passed(marks):
        return marks >= 35
Rahul = Student("Rahul",79)
Hrithik = Student("Hrithik",34)
print(f"{Rahul.name}:{'passed' if Student.has_passed(Rahul.marks) else 'Failed'}")
print(f"{Hrithik.name}:{'passed' if Student.has_passed(Hrithik.marks) else 'Failed'}")
