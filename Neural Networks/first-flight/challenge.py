# Challenge program with the challenge data set

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read the data
with open('challenge_database.txt') as dataframe:
    lines = dataframe.read.splitlines()  # pesky bug

left = []
right = []

for line in lines:
    numbers = line.split(',')
    left_num = float(numbers[0])
    right_num = float(numbers[1])
    left.append(left_num)
    right.append(right_num)

reg = linear_model.LinearRegression()
reg.fit(left, right)

# visualize
plt.scatter(left, right)
plt.plot(left, reg.predict(left))
plt.show()


