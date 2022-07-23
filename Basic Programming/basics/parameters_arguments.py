# FUNCTIONS in PYTHON
# =======================================================
# Parameter :
""" A parameter is the variable listen inside the parentheses in the function defintion """
# Argument :
""" An argument is the value that is sent to the function when it is called."""

def my_function(my_parameter,two): # this is a parameter
    print(my_parameter + "\t" + two)
my_function("here goes an argument","two") # this is an argument
# ======================================================
# Arbitrary Arguments :
"""
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
"""
def my_func(*li):
    print(li)
my_func("Abel","Roy")
# =======================================================
# Default Parameters :
def my_func(this = "Abel"):
    print("I am ",this)
my_func("Pranav")
my_func()
# =====================================================
# Code by Abel Roy #
