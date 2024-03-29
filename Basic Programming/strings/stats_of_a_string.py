# Statistics of a String
# =================================================
def stats(string):
    alphabets = uppercase = lowercase = digits = spaces = 0
    for i in string:
        if i.isalpha():
            alphabets += 1
        if i.isupper():
            uppercase += 1
        if i.islower():
            lowercase += 1
        if i.isdigit():
            digits += 1
        if i.isspace():
            spaces += 1
    return alphabets, uppercase, lowercase, spaces, digits

user_input = str(input("Enter a string : "))
alphabets, uppercase, lowercase, spaces, digits = stats(user_input)
print(
    f"""
    Statistics of a String :
        Length : {len(user_input)}
        Alphabets : {alphabets}
            Uppercase : {uppercase}
            Lowercase : {lowercase}
        Spaces : {spaces}
        Digits : {digits}
    """
)
# ================================================
# Code by Abel Roy #
