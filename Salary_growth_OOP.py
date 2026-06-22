class Employee:

    def __init__(self, first, last, pay, role):
        self.first = first
        self.last = last
        self.pay = pay
        self.role = role
        self.email = f"{first}.{last}@company.com"

    @staticmethod
    def get_raise_percent(role):
        if role == "Cloud":
            return 1.12   # 12%
        elif role == "DevOps":
            return 1.17   # 17%
        else:
            return 1.10   # default

    def apply_raise(self):
        multiplier = Employee.get_raise_percent(self.role)
        self.pay = int(self.pay * multiplier)

    def __str__(self):
        return f"{self.first} {self.last} | {self.role} | {self.pay}"
emp_1 = Employee('Sai', 'Vishnu', 97000, "Cloud")
emp_2 = Employee('Leon', 'Kennedy', 95000, "DevOps")

emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1)
print(emp_2)
