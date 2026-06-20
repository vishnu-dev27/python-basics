class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def Fullname(self):
        return '{} {}'.format(self.first, self.last)
        def apply_raise(self):
        self.pay=int(self.pay * 1.04)
emp_1=Employee('Sai','Vishnu',50000)

print(emp_1.pay)
emp_1.apply_raise
print(emp_1.pay)



class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def Fullname(self):
        return '{} {}'.format(self.first, self.last)
        def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
emp_1=Employee('Sai','Vishnu',50000)
print(emp1. __dict__)

employee.raise_amount = 1.06
print(employee.raise_amount)
print(emp_1.raise_amount)
