# Import necessary libraries
import pandas as pd

# Load the data
df = pd.read_excel('data.xlsx')

# Check for missing values
print("Missing values for each column:")
print(df.isnull().sum())
print("\n")

# Check for duplicate for order id
print("Duplicate rows:")
print(df.duplicated().sum())
print("\n")

# Check data types of each column
print("Data types:")
print(df.dtypes)

