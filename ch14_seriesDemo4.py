import pandas as pd

myDictionary = {
    'Name' : 'Miguel',
    'Number' : 42,
    'Age' : 'unknown'
    }

mySeries = pd.Series(myDictionary)
print(mySeries[:2])

