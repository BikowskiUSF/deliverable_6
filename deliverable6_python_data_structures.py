import pandas as pd   # Import the pandas package
import numpy as np    # Import the numpy package
import seaborn as sns # Import the seaborn package

# Load the iris dataset from seaborn's built-in datasets using the load_dataset() function, and store it in a variable called "iris"
iris = sns.load_dataset('iris')

# Drop the 'species' column from the iris dataset using the drop() function
iris = iris.drop('species', axis=1)

# Create two new columns in the iris dataset called 'sepal_sum' and 'petal_sum', which are the sums of 'sepal_length' and 'sepal_width', and 'petal_length' and 'petal_width', respectively
iris['sepal_sum'] = iris['sepal_length'] + iris['sepal_width']
iris['petal_sum'] = iris['petal_length'] + iris['petal_width']

# Create a new pandas dataframe called "summary_stats" that contains the summary statistics of the iris dataset, such as mean, standard deviation, minimum, and maximum
summary_stats = pd.DataFrame({
    'mean': iris.mean(),
    'std': iris.std(),
    'min': iris.min(),
    'max': iris.max()
})

# Reorder the rows of the summary_stats dataframe to display sepal_length, sepal_width, sepal_sum, petal_length, petal_width, and petal_sum in that order
summary_stats = summary_stats.loc[['sepal_length', 'sepal_width', 'sepal_sum', 'petal_length', 'petal_width', 'petal_sum']]

# Print the summary statistics dataframe to the console
print(summary_stats)

