# Statistics of a String
# =================================================
def stats(string):
    alphabets = uppercase = lowercase = digits = spaces = 0
    for i in range(len(string)):
        if string[i].isalpha() is True:
            alphabets += 1
        if string[i].isupper() is True:
            uppercase += 1
        if string[i].islower() is True:
            lowercase += 1
        if string[i].isdigit() is True:
            digits += 1
        if string[i].isspace() is True:
            spaces += 1
    return alphabets, uppercase, lowercase, spaces, digits

user_input = str(input("Enter a string : "))
alphabets, uppercase, lowercase, spaces, digits = stats(user_input)
print(
    f"""
    Statistics of a String :
        Alphabets : {alphabets}
            Uppercase : {uppercase}
            Lowercase : {lowercase}
        Spaces : {spaces}
        Digits : {digits}
    """
)
# ================================================
# Code by Abel Roy #
