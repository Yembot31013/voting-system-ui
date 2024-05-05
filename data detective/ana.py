# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel('data.xlsx')
print(df["Region"].describe())
# Find duplicate 'Order ID' values
# column = df["City"]
# top_value = column.value_counts().idxmax()
# top_value_count = column.value_counts().max()
# unique_value = column.nunique()

# # print(duplicates.mean())
# # print(duplicates.median())
# # print(duplicates.mode())

# print(top_value)
# print(top_value_count)
# print(unique_value)