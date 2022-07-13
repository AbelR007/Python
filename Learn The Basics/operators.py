
def arithmetic_operators(a,b):

    # Arithmetic operators
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b

    mod = a % b
    fdiv = a // b

    return add, sub, mul, div, mod, fdiv

def comparison_operators(a,b):

    greater = a > b
    lesser = a < b
    equal = a == b
    not_equal = a != b
    return greater, lesser, equal, not_equal

def logical_operators(a,b):

    _and = a and b
    _or = a or b
    _not = not a

    return _and, _or, _not

def main():
    a = 10
    b = 3

    add, sub, mul, div, mod, fdiv = arithmetic_operators(a,b)
    print(f"Add: {add}, Sub: {sub}, Mul: {mul}, Div: {div}, Mod: {mod}, FDiv: {fdiv}")

    greater, lesser, equal, not_equal = comparison_operators(a,b)
    print(f"Greater: {greater}, Less: {lesser}, Equal: {equal}, Not Equal: {not_equal}")

    AND, OR, NOT = logical_operators(a,b)
    print(f"AND: {AND}, OR: {OR}, NOT:{NOT}")

main()

# ================================================
""" Code by Abel Roy """

n = [21,2,3]k
n.sort()
print(n[len(n) // 2])
print(list(reversed(range(1,11))))
