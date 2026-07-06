# employee salary distribution records

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, amount):
        if amount >= 10000:
            self._salary = amount
        else:
            print("Salary is too low!")
    @salary.deleter
    def salary(self):
        print("Salary record deleted.")
        del self._salary
emp = Employee("Rahul", 30000)
print(emp.salary)      # Getter
emp.salary = 40000     # Setter
print(emp.salary)
emp.salary = 5000      # Invalid
del emp.salary         # Deleter
