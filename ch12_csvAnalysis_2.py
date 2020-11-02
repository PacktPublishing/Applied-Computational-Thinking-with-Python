import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import os

#Let Python know correct directory for file.
os.chdir('C:\\...')

graduates = pd.read_csv('ch12_data.csv', index_col = 0)
print(graduates[0:16])




