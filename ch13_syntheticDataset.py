from numpy import where
from sklearn.datasets import make_classification
from matplotlib import pyplot

#Create a synthetic dataset
X, y = make_classification(n_samples = 1800, n_features = 2, n_informative = 2, n_redundant = 0, n_clusters_per_class = 1, random_state=4)
#Scatterplot
for class_value in range(2):
	row_ix = where(y == class_value)
	pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
#Display plot
pyplot.show()
