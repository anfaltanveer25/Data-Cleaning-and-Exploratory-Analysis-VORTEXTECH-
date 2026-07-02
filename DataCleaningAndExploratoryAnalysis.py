
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""## Loading the Dataset

In this step, the Wholesale Customers dataset is loaded using Pandas. The first few rows are displayed to understand the structure of the dataset, and the dataset information is checked to identify the number of rows, columns, and data types.
"""
#  load dataset
df=pd.read_csv('Wholesale customers data.csv')
df.head()
df.info()

"""## Checking Missing Values and Duplicate Records

This step checks whether the dataset contains any missing values or duplicate records. The result showed that the dataset has no missing values and no duplicate rows.
"""

#  Missing values
print(df.isnull().sum()) # sum of missing rows
df.duplicated().sum()  #duplicate column

"""## Handling Missing Values

Any missing values in numerical columns are replaced with the column mean. Since there are no categorical columns in this dataset, no categorical missing value handling was required.
"""

#  Handle missing values for numerical columns

numerical_cols=[
  'Channel', 'Region', 'Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen'
]

for col in numerical_cols:
     if df[col].isnull().sum() > 0:
         df[col].fillna(df[col].mean())

print("Null values are handled in numerical columns.")

#Handle missing values for categorical columns
categorical_df = df.select_dtypes(include=['object'])
for col in categorical_df.columns:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mode()[0])

print("Null values are handled in categorical columns.")

"""## Correcting Data Types

The numerical columns are converted to numeric data types to ensure consistency and avoid errors during data analysis and visualization.
"""

#correct data types for numerical columns
for col in numerical_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
print("Data types are corrected for numerical columns.")

"""## Descriptive Statistics

Descriptive statistics are generated to summarize the dataset. These statistics include count, mean, standard deviation, minimum, maximum, and quartile values for each numerical feature.
"""

# descriptive statistics

print(df.describe())
print(df.select_dtypes(include='object').columns)

"""## Histogram Visualization

A histogram is used to visualize the distribution of numerical variables in the dataset. It helps identify the spread of data, skewness, and the presence of potential outliers.

### Observation

Most numerical features are positively skewed, indicating that many customers have lower spending values while a few customers have very high spending amounts. This suggests the presence of outliers in the dataset.
"""

print("======================Visuialization======================")

df.hist(figsize=(15,10), bins=20)

plt.suptitle("Histogram of Wholesale Customers Dataset", fontsize=16)
plt.tight_layout()
plt.show()
plt.savefig('histogram.png')