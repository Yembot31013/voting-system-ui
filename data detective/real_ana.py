# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel('data.xlsx')

# Calculate the total sales for each customer
customer_details = df.groupby('Customer ID')['Region']
# customer_sales = customer_details.sum()

print(customer_details)
# print(len(customer_sales))
# print(customer_sales.describe())
# Sort the customers by total sales
# sorted_customer_sales = customer_sales.sort_values(ascending=False)

# sale_date = df.groupby('Order Date')['Order Date']
# print(sorted_customer_sales[-1])

# Plot the total sales for the top 10 customers
# plt.figure()
# print(sorted_customer_sales[:10])
customer_sales.plot(kind='bar')
plt.title('Sales per date')
plt.ylabel('Date')
plt.xlabel('Total Sales')
plt.show()
