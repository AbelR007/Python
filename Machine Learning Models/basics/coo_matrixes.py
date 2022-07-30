# Representing data in COO Format
# =================================================
import numpy as np
from scipy import sparse

x = np.ones(4)
r = np.arange(4)
c = np.arange(4)
sm = sparse.coo_matrix((x,(r,c)))
print("Data :\n",x)
print("Matrix in COO format :\n",sm)
# =================================================
"""
    WHY COO Format instead of CSR format?

    COO compresses the dense representations of sparse matrix data (as they wouldn't fit into memory). It also helps create the sparse representations directly.
"""
# ================================================
# Code by Abel Roy #
