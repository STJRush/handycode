# This program lets you investigate if 4 variables on a line graph are correlated.
# In this example, it looks at data from 4 geiger counters namely QA060,rad100,FS2011,XH-901
# You can switch those names for your own data eg. Happiness, Homework, Fun etc.

import pandas as pd
import numpy as np
from time import sleep


def interpret_correlation(correlation):
    """Function to interpret the correlation coefficient with emojis."""
    abs_corr = abs(correlation)
    if abs_corr >= 0.9:
        return "Very High Correlation 🚀"
    elif abs_corr >= 0.7:
        return "High Correlation 🔥"
    elif abs_corr >= 0.5:
        return "Moderate Correlation 👍"
    elif abs_corr >= 0.3:
        return "Low Correlation 👀"
    else:
        return "Negligible Correlation 😴"



print("Pearson's Correlation: This measures the linear correlation between two variables.")
print("")
print("It gives a value between -1 and 1")
print(" ➞  1 is total positive linear correlation")
print(" ➞  0 is no linear correlation")
print(" ➞ -1 is total negative linear correlation.")
print("")

# Load data from CSV file
data = pd.read_csv('mydata.csv')

# Extract data for each column
data_QA060 = data['QA060']
data_rad100 = data['RAD 100']
data_FS2011 = data['FS2011']
data_XH901 = data['XH-901']

# Calculating Pearson Correlation for each pair
corr_QA060_rad100 = np.corrcoef(data_QA060, data_rad100)[0, 1]
corr_QA060_FS2011 = np.corrcoef(data_QA060, data_FS2011)[0, 1]
corr_QA060_XH901 = np.corrcoef(data_QA060, data_XH901)[0, 1]
corr_rad100_FS2011 = np.corrcoef(data_rad100, data_FS2011)[0, 1]
corr_rad100_XH901 = np.corrcoef(data_rad100, data_XH901)[0, 1]
corr_FS2011_XH901 = np.corrcoef(data_FS2011, data_XH901)[0, 1]


print("")
print("PEARSON'S CORRELATION (LINEAR TRENDS ONLY)")
print("")


# Print correlation and interpretation
print(f"Correlation between QA060 and rad100: {corr_QA060_rad100} ({interpret_correlation(corr_QA060_rad100)})")
print(f"Correlation between QA060 and FS2011: {corr_QA060_FS2011} ({interpret_correlation(corr_QA060_FS2011)})")
print(f"Correlation between QA060 and XH-901: {corr_QA060_XH901} ({interpret_correlation(corr_QA060_XH901)})")
print(f"Correlation between rad100 and FS2011: {corr_rad100_FS2011} ({interpret_correlation(corr_rad100_FS2011)})")
print(f"Correlation between rad100 and XH-901: {corr_rad100_XH901} ({interpret_correlation(corr_rad100_XH901)})")
print(f"Correlation between FS2011 and XH-901: {corr_FS2011_XH901} ({interpret_correlation(corr_FS2011_XH901)})")


# Show a line graph

import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('mydata.csv')

# Plotting the data
plt.figure(figsize=(10, 6))


# Assuming the columns are named 'QA060', 'rad100', 'FS2011', 'XH-901'
plt.plot(data['QA060'], label='QA060')
plt.plot(data['RAD 100'], label='RAD 100')
plt.plot(data['FS2011'], label='FS2011')
plt.plot(data['XH-901'], label='XH-901')

# Adding title and labels
plt.title('Line Graph of QA060, rad100, FS2011, XH-901')
plt.xlabel('Index')
plt.ylabel('Value')

# Adding a legend
plt.legend()

# Showing the plot
plt.show()



# Show a Seaborn Graph

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('mydata.csv')

# Calculating the correlation matrix
correlation_matrix = data.corr()

# Setting up the matplotlib figure
plt.figure(figsize=(10, 8))

# Drawing the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlGn', fmt=".2f", linewidths=.5, vmin=-1, vmax=1)

# Adding title and labels
plt.title('PEARSONS Correlation Matrix (Are they related)')
plt.xlabel('Variables')
plt.ylabel('Variables')

# Showing the plot
plt.show()

print(" ")
sleep(0.5)
print(" ")

print("")
print("SPEARMAN'S CORRELATION (CAN BE NON-LINEAR TREND. LESS SENSITIVE TO OUTLIERS)")
print("")

sleep(3)


import pandas as pd
import numpy as np
from scipy.stats import spearmanr

# Sample data loading (Replace this with your actual CSV file path)
data = pd.read_csv('mydata.csv')

# Extracting the columns
qa060 = data['QA060']
rad100 = data['RAD 100']
fs2011 = data['FS2011']
xh901 = data['XH-901']

# Calculating Spearman's correlation
corr_qa060_rad100, _ = spearmanr(qa060, rad100)
corr_qa060_fs2011, _ = spearmanr(qa060, fs2011)
corr_qa060_xh901, _ = spearmanr(qa060, xh901)
corr_rad100_fs2011, _ = spearmanr(rad100, fs2011)
corr_rad100_xh901, _ = spearmanr(rad100, xh901)
corr_fs2011_xh901, _ = spearmanr(fs2011, xh901)




# Printing the results
print(f"Spearman's correlation between QA060 and rad100: {corr_qa060_rad100} ({interpret_correlation(corr_QA060_rad100)})")
print(f"Spearman's correlation between QA060 and FS2011: {corr_qa060_fs2011} ({interpret_correlation(corr_QA060_FS2011)})")
print(f"Spearman's correlation between QA060 and XH-901: {corr_qa060_xh901} ({interpret_correlation(corr_QA060_XH901)})")
print(f"Spearman's correlation between rad100 and FS2011: {corr_rad100_fs2011} ({interpret_correlation(corr_rad100_FS2011)})")
print(f"Spearman's correlation between rad100 and XH-901: {corr_rad100_xh901} ({interpret_correlation(corr_rad100_XH901)})")
print(f"Spearman's correlation between FS2011 and XH-901: {corr_fs2011_xh901} ({interpret_correlation(corr_FS2011_XH901)})")




# Spearman instead of Pearson

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('mydata.csv')

# Calculating Spearman's correlation matrix
spearman_corr_matrix = data.corr(method='spearman')

# Setting up the matplotlib figure
plt.figure(figsize=(10, 8))

plt.title('SPEARMANS Correlation Matrix (Are they related)')

# Drawing the heatmap for Spearman's correlation matrix
sns.heatmap(spearman_corr_matrix, annot=True, cmap='RdYlGn', fmt=".2f", linewidths=.5, vmin=-1, vmax=1)

# Adding title and labels
plt.title('Spearman\'s Correlation Matrix for Variables')
plt.xlabel('Variables')
plt.ylabel('Variables')

# Showing the plot
plt.show()



