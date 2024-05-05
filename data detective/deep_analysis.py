# Import necessary libraries
import pandas as pd

# Load the data
df = pd.read_csv('your_file.csv')

# Check for outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print("Outliers:")
print(((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).sum())
print("\n")

# Check for inconsistent data entry
print("Unique values for 'City' column:")
print(df['City'].unique())
print("\n")

# Check data types of each column
print("Data types:")
print(df.dtypes)
print("\n")

# Check for irrelevant data
print("Columns:")
print(df.columns)
print("\n")

# Check for data transformation needs
print("Data description:")
print(df.describe())
