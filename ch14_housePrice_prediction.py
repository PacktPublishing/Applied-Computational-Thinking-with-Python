# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

housing_data= pd.read_csv("kc_house_data.csv")
#Housing_data.head()
#print(housing_data.shape)

housing_data.describe(include=[np.number])
housing_data.head

housing_data.describe()

#Checking for missing values in data
housing_data.isnull().sum()

names=['price','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','zipcode','lat','long']
df=housing_data[names]
correlations= df.corr()
fig=plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(correlations,vmin=-1,vmax=1)
fig.colorbar(cax)
ticks=np.arange(0,15,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names, rotation =' 90')
ax.set_yticklabels(names)
plt.tight_layout()
plt.savefig('Correlation_graph.png',dpi = 300)
plt.show()

#Pairplotting for all data
sns.pairplot(housing_data)
plt.savefig('graphing.png',dpi =300)
plt.show()
#Pairplotting for some data
coln = ['price','sqft_living','sqft_above']
sns.pairplot(housing_data[coln], size = 3);
plt.savefig('pairplotting.png',dpi =300)
plt.show()
