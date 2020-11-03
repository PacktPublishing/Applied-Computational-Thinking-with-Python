import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:\\...\\us-PuertoRico.csv')

plt.scatter(df['date'], df['cases'])
plt.xticks(rotation = 90)
plt.title('Cases per day during October 2020 due to COVID19 in Puerto Rico')
plt.ylabel('Number of Cases')
plt.tight_layout()
plt.show()
plt.savefig('COVID_PR.png')

