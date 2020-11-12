# Import seaborn
import seaborn as sns

sns.set_style('darkgrid')
# Load an example dataset
exercise = sns.load_dataset("exercise")

#Create the plot
sns.relplot(
    data=exercise,
    x='id', y="pulse", col="time",

)
