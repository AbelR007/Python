import numpy as np
from scipy import sparse

x = np.array(
    [[1,2,3],
    [4,5,6]]
)
# print(x)
# x = np.eye(4) # Creates a diagonal matrix
sm = sparse.csr_matrix(x)
print(sm)

data = np.empty(2)
print(data)

# ================================================
# Code by Abel Roy #
