import statistics as stats
x = [1,2,3,4,67]
print(stats.stdev(x))

def matrix(x):
    for i in range(len(x)):
        print("Standard Deviation : ",stats.stdev(x[i]))

new = [
    [1,2,3,4,5],
    [6,7,111,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
]
matrix(new)
