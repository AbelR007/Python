# Bubble Sort in Python
# =================================================
lis = [5,2,4,2,1]

print(lis)
for i in range(1,len(lis)):
    if lis[i] < lis[i-1]:
        # print("hmm")
        list[i],list[i-1] = list[i-1],list[i]
print(lis)

# ================================================
# Code by Abel Roy #
