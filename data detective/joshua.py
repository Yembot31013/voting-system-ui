import pandas as pd

df = pd.read_excel('data.xlsx')

quanlity_df = df["Quantity"]

print(quanlity_df.sum())