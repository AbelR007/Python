# Merging a dict into another one using basic fundamentals
# =================================================
dict1 = {1:"Hello", "Abel":"OP"}
dict2 = {2:"Hi"}
dict3 = {}

def merge_dict(to, fro):
    for i in fro:
        to[i] = fro[i]

merge_dict(dict3, dict1)
merge_dict(dict3, dict2)
print(dict3)
# ================================================
# Code by Abel Roy #
