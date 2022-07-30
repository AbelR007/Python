# Calculating Standard Deviation from matrix
# =================================================
import statistics as stats

x = [1,2,3,4,67]
print(stats.stdev(x))

def standard_deviation(x):
    # Prints the standard deviation of each row in the matrix
    for i in range(len(x)):
        print("Standard Deviation : ",stats.stdev(x[i]))

matrix = [
    [1,2,3,4,5],
    [6,7,111,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
]
standard_deviation(matrix)
# ================================================
# Code by Abel Roy #
