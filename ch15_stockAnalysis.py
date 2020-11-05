import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

#Get data from Quandl. Note that you'll need your own API to substitute in the api.key below.
quandl.ApiConfig.api_key = '...'
VZ = quandl.get('EOD/VZ')
print(VZ.head())

#Grab the Adj_Close column
VZ = VZ[['Adj_Close']]
print(VZ.head())
