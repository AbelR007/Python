import datetime

class Employee:
    """docstring for Employee."""
    raise_amount = 1.04
    num = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True

class Developer(Employee):
    pass

emp1 = Developer('Abel', 'Roy', 50000)
emp2 = Developer('Test', 'User', 60000)

print(emp1.email)
print(emp2.email)

print("Done.")
# =========================================================
# ===== Not needed =========
"""emp1.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
"""

"""
newemp1 = 'John-Doe-7000'
first, last, pay = newemp1.split("-")
newempdata = Employee(first, last, pay)
newempdata = Employee.from_string(newemp1)

print(newempdata.email)
print(newempdata.pay)
"""
"""
mydate = datetime.date(2016,7,11)
print(Employee.is_workday(mydate))

"""
