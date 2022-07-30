import numpy as np
import matplotlib.pyplot as plt

# Generate a seq of nos. from -10 to 10 with 100 steps in between
x = np.linspace(-10,10,100)

# Create a second array using sin
y = np.sin(x)

# This makes the chart
plt.plot(x,y, marker='x')
# ================================================
# Code by Abel Roy #
