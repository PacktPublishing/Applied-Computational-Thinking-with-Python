import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('diabetes.csv')

# Split dataset into input(x) and output(y) variables 
x_variables = dataset.iloc[:,0:8]
y_variable = dataset.iloc[:,8]

print(x_variables)
print(y_variable)

from sklearn.model_selection import train_test_split
X_train,X_test, y_train,y_test = train_test_split(x_variables, y_variable, test_size = 0.20, random_state = 10)
