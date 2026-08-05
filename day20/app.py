#Performing EDA - Exploratory Data Analysis
#1.Univariate analysis
# One column - consider one variable at a time
#DATA = Numerical or Categorical
# Categorical - Country 
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
df = pd.read_csv('Titanic-Dataset.csv') 
print(df.head())

#1. Categorical Data 
# here Survived is categorical data as 0,1 ka value hai - survived or not survived 
# for any categorical data - use countplot
sns.countplot(x=df['Survived'])
plt.show()
plt.pause(10)
print(df['Survived'].value_counts())

