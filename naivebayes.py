import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("data.csv")
print(dataset.info())

dataset = dataset.drop(["id"], axis = 1)
dataset = dataset.drop(["Unnamed: 32"], axis = 1)
print(dataset.info())

M = dataset[dataset.diagnosis == "M"]
B = dataset[dataset.diagnosis == "B"]

plt.title("Malignant vs Benign Tumor")
plt.xlabel("Radius Mean")
plt.ylabel("Texture Mean")
plt.scatter(M.radius_mean, M.texture_mean, color = "red", label = "Malignant", alpha = 0.3)
plt.scatter(B.radius_mean, B.texture_mean, color = "lime", label = "Benign", alpha = 0.3)
plt.legend()
plt.show()

dataset.diagnosis=[1 if i=="M" else 0 for i in dataset.diagnosis]

x = dataset.drop(["diagnosis"], axis = 1)
y = dataset.diagnosis.values

import sklearn
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
print(nb.fit(x_train, y_train))

print("Naive Bayes score: ",nb.score(x_test, y_test))