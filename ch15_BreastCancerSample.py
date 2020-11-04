#Import libraries needed
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#Get data set. Remember to check your directory and/or add the full location of the file.
dataset = pd.read_csv('C:\\...\\breast-cancer.csv')
dataset.head()
dataset.isnull().sum()

#Create count variable for diagnosis
count = dataset.diagnosis.value_counts()
count

#Create bargraph of the diagnosis values
count.plot(kind = 'bar')
plt.title('Tumor distribution (malignant: M, benign: B)')
plt.xlabel('Diagnosis')
plt.ylabel('count')
plt.show()
y_target = dataset['diagnosis']
dataset.columns.values
dataset['target'] = dataset['diagnosis'].map({0:'B',1:'M'})

#Create scatterplot of mean perimeter and mean texture
sns.scatterplot(x = 'perimeter_mean', y = 'texture_mean', data = dataset, hue = 'diagnosis', palette = 'bright');
