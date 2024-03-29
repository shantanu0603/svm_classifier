# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12V0Ke50zwVpDEuTGG2dVWn52gI5RKA1j
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X= iris.data[:,:2]
Y = iris.target

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

svm=SVC(kernel='linear',C=1.0)

svm.fit(X_train,Y_train)

prediction =svm.predict(X_test)

accuracy = accuracy_score(Y_test,prediction)
print("accuracy:",accuracy)

def plot_decision_boundary(X,Y,model,title):

   h = .02  # step size in the mesh
   x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
   y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
   xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

   Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
   Z = Z.reshape(xx.shape)

   plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
   plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.coolwarm, edgecolors='k', marker='o')
   plt.title(title)
   plt.xlabel('Feature 1')
   plt.ylabel('Feature 2')
   plt.show()

# Plot the decision boundary
plot_decision_boundary(X_train, Y_train, svm, 'SVM Decision Boundary (Training Set)')