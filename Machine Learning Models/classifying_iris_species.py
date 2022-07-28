# Machine Learning Model | Classifying IRIS species (3 Class Distribution)
# =================================================
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the dataset
iris_dataset = load_iris()

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)

# Use algorithm KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# Accuracy Test
accuracy = knn.score(X_test, y_test)
# print(knn.score(X_test, y_test))
print(f"Model Accuracy : {int(accuracy*100)}%")

# Evaluates data
input = eval(input("Enter dataset to identify : "))
X_new = np.array([input])
prediction = iris_dataset['target_names'][knn.predict(X_new)]
print("Predicted species is ",prediction[0])
# ================================================
# Code by Abel Roy #
