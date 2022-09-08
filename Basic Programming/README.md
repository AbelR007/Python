# Python Basics

### About Python
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.

### Designed by :
Guido Van Rossum in 1991

---
## Chapter 1 : Basics Concepts


```python
# Prints"Hello, world"
print("Hello, world!")
```

    Hello, world!


---
## Chapter 2 : Data Types

#### Basic Datatypes
- Integer :
    `1,-4`
- Float :
    `27.2, -12`
- String :
    `"Hello", 'hi'`
- Boolean :
    `True, False`


```python
# Initialisation of each basic datatype
integer = 5 # integer
floats = 2.0 # float
string = "Hello" # string
boolean = True # boolean
```

#### Advanced Datatypes
- List : `[1,2,3,4]`
- Tuple : `(1,2,3,4)`
- Dictionary : `{1 : "Hello", 2 : "world"}`
- Sets : `{1,2,3,4}`


```python
# Using each Advanced Datatype
List = [1,2,3,4]
Tuple = (1,2,3,4)
Dictionary = {
    1:"Hello" ,
    2 : "World"
}
Set = {1,2,3,4}
```

---
## Chapter 3 : Operators in Python

In Python there are many operations that we can perform on operands/values,

- Arithmetic Operators
- Conditional Operators
- Logical Operations
- Assignment Operations
- Bitwise Operations
- Membership Operations
- Identity Operations


```python
# Example of Arithmetic Operation
# Basic Calculator
a = 1
b = 2
print("Basic Calculator Operations : ")
print("Addition : ", a + b)
print("Subtraction : ", a - b)
print("Division : ", a / b)
print("Multiplication : ",a * b)
```

    Basic Calculator Operations :
    Addition :  3
    Subtraction :  -1
    Division :  0.5
    Multiplication :  2


---
## Chapter 4 : If - Elif - Else

Conditional Statements in Python are a way of categorizing and performing tasks only if the condition is true.
A great way to manipulate and create lists is through list comprehensions, which have an expression and then a ‘for’ clause, followed by a zero or more ‘for’ or ‘if’ clauses.


```python
# Example of If - Elif - Else
a = 5
b  = 10

if a > b :
    print("A is greater")
elif b > a :
    print("B is greater")
else:
    print("A and B is equal")
```

    B is greater


---
## Chapter 5 : Loops

Loops in Python help programs to iterate over a specific statement for 'n' no. of times.
Python’s flow control statements are ‘while’, ‘for’. For a switch, you need to use ‘if’. For enumerating through list members, use ‘for’. For obtaining a number list, use range (number).


```python
# Example : For Loop
for i in range(3):
    print(i)
```

    0
    1
    2



```python
# Example : While Loop
i = 0
while i < 3:
    print(i)
    i += 1
```

    0
    1
    2


---
## Chapter 6 : Functions

Functions are block of code that performs a specific task. In python, you can define a function using a "def" keyword and calling a function.



```python
# Defining a Function
def my_func(name):
    print("My name is ",name)

# Calling a Function
my_func("Abel Roy")
```

    My name is  Abel Roy


---
## Chapter 7 : Methods

Methods in Python are datatype specific. Each data type has it's own set of methods.



```python
# List eMethods
new_value = 5
List = [1,2,3,4]

List.append(new_value) # This is a List Method
print(List)
```

    [1, 2, 3, 4, 5]


---
## Simple Python Projects

1. TicTacToe in Python
2. Rock Paper Scissors - User Defined
3. Basic Password Creation Tool
4. Advanced Calculator with 8 Functions
5. Mark Grading System with Custom Feedback
6. Showcasing Time of 2+ Different Locations
7. Probability/ Memory Game using Basics
---
##### Created with ❤️ by Abel Roy
