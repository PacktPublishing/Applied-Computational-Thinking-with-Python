import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import os

#Let Python know correct directory for file.
os.chdir('C:\\...')

graduates = pd.read_csv('ch12_data.csv', index_col = 0)
print(graduates[0:13])

fig, ax = plt.subplots()
ax.bar(graduates.index, graduates['Hispanic'])
ax.set_xticks(graduates.index)
ax.set_xticklabels(graduates.index, rotation = 60, horizontalalignment = 'right')
ax.set_title('Number of Hispanic graduates from 1996-2012', fontsize = 16)
ax.set_ylabel('Number of Graduates')

plt.show()

 

