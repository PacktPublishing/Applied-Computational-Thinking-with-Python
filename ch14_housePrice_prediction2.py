# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


housing_data= pd.read_csv("C:\\Users\\sofia.dejesus\\Documents\\02_book\\kc_house_data.csv")
#Housing_data.head()
#print(housing_data.shape)

housing_data.describe(include=[np.number])
housing_data.head

housing_data.describe()

#Checking for missing values in data
housing_data.isnull().sum()




#Pairplotting for some data
coln = ['price','sqft_living','zipcode', 'sqft_above']
sns.pairplot(housing_data[coln], height = 4);
plt.savefig('pairplotting.png',dpi =300)
plt.show()



from plotnine.data import huron
from plotnine import ggplot, aes, geom_boxplot

(ggplot(huron)
 +aes(x = 'sqft_living', y='sqft_above')
+geom_boxplot()
)
