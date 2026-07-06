class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
@property
def marks(self):
    return self.marks
@marks.setter
def marks(self,value):
    if 0 <= value <= 100:
        self.marks = value
    else:
        print("marks should be in between 1 and 100")
@marks.deleter
def marks(self):
    print("marks deleted")
    del self.marks
student = Student("vishnu",80)
print(student.marks)
student.marks = 87
print(student.marks)
del student.marks
