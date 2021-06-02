# TOPIC : Python Classes & their basic uses

# If you are reading this from Github,
# THESE CODES ARE FOR UNDERSTANDING PURPOSES. YOU MAY USE THEM IN ANY WAY YOU WANT.
# These are not necessarily by me. They are developed by referring through many sources

# Already installed through Python3 | Not necessary module for classes
import datetime

# Python Main CLASS
class Employee:
    """docstring for Employee."""
    raise_amt = 1.04
    num = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num += 1
    
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print("Deleted by AbelR007!")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)
    
    def __len__(self):
        return len(self.fullname())

# SUB CLASS of EMPLOYEE
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

# SUB CLASS of EMPLOYEE
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())

emp1 = Employee('Abel', 'Roy', 50000)
emp2 = Employee('Test', 'User', 60000)

dev1 = Developer('Abel', 'Roy', 50000, "Python")
dev2 = Developer('Test', 'User', 60000, "JS")

mgr1 = Manager("Super Abel", "Super Roy", 90000, [dev1])
mgr2 = Manager("Super Test","Super User", 100000, [dev1, dev2])

# =========================================================
# CREATED with ❤️ by AbelR007
# =========================================================