class Student:
    count = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
    def get_info(self):
        return"{self.name}{self.gpa}"
    @classmethod
    def get_count(cls):
        return f"total # of students: {cls.count}"
Student_1 = Student("Spongebob",3.2)
Student_2 = Student("Patrick",2.9)
Student_3 = Student("Sandy",3.8)
print(Student.get_count())


class Student:
    count = 0
    gpa = 0
    total_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    def get_info(self):
        return"{self.name}{self.gpa}"
    @classmethod
    def get_count(cls):
        return f"total # of students: {cls.count}"
    @classmethod
    def get_average_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count}"
Student_1 = Student("Spongebob",3.2)
Student_2 = Student("Patrick",2.9)
Student_3 = Student("Sandy",3.8)
print(Student.get_count())
print(Student.get_average_gpa())

