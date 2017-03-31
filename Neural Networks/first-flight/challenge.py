# Challenge program with the challenge data set

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read the data
dataframe = pd.read_fwf('challenge_database.txt')
xVals = dataframe.split[","]
