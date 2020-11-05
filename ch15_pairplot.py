import seaborn as sns
import pandas as pd

df = pd.read_csv('C:\\...\\Data_Cortex_Nuclear.csv')
sns.pairplot(df, hue = 'Treatment')
