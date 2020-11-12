# Import seaborn
import seaborn as sns

sns.set_style('darkgrid')
# Load an example dataset
flights = sns.load_dataset("flights")

#Create the plot
sns.pairplot(
    data=flights,
)
