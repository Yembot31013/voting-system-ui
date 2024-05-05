# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel('data.xlsx')

# Calculate basic statistics
mean = df.mean()
median = df.median()
mode = df.mode()

print(f'Mean:\n{mean}\n')
print(f'Median:\n{median}\n')
print(f'Mode:\n{mode}\n')

# Visualize the data
df.hist(figsize=(10,10))
plt.tight_layout()
plt.show()
