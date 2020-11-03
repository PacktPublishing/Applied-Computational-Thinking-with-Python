import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:\\...\\us-PuertoRico.csv')

plt.scatter(df['date'], df['deaths'])
plt.xticks(rotation = 90)
plt.title('Deaths per day during October 2020 due to COVID19 in Puerto Rico')
plt.ylabel('Number of Deaths')
plt.tight_layout()
plt.savefig('COVID_PR.png')
plt.show()

