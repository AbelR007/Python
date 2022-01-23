import uuid
import random

x = str(uuid.uuid4()).replace("-", "")
uid = int(x, 16)
print(uid)

ids = uuid.uuid4()
print(ids.int)


def check(id :int):
    if -9223372036854775808 > id  >9223372036854775807:
        print("Yup.")
    else :
        print("Nopes")

# ================================
# CREATED with ❤️ by AbelAbelR007
# ================================
