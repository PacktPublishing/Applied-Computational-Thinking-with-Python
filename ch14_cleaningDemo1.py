import pandas as pd
myData = pd.read_csv('C:\\Users\\sofia.dejesus\\Documents\\02_book\\demo_missing.csv')
print(myData)
cleanData = myData.dropna(axis = 0, how = 'any')
print(cleanData)
