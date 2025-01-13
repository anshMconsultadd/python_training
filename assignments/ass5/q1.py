
import os
print(os.getcwd())
import pandas as pd

# Replace 'sales_data.csv' with the actual file name or path
data=pd.read_csv('supermarket_sales - Sheet1.csv')
print(data.head())  # Display the first few rows of the data
average_income = data['gross income'].mean()
max_income = data['gross income'].max()
max_income_row = data[data['gross income'] == max_income]

print(f"Average Gross Income: {average_income}")
print(f"Maximum Gross Income: {max_income}")
print("Details of the Best Sale:")
print(max_income_row)

