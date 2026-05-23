import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Seed for reproducibility
np.random.seed(42)

# Generate 1000 rows of data
n_rows = 1000

categories = ['Electronics', 'Furniture', 'Office Supplies', 'Clothing']
regions = ['North', 'East', 'South', 'West']
products = {
    'Electronics': ['Laptop', 'Smartphone', 'Headphones', 'Smartwatch'],
    'Furniture': ['Office Chair', 'Desk', 'Sofa', 'Bookcase'],
    'Office Supplies': ['Paper Pack', 'Binder', 'Pens', 'Stapler'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Sneakers']
}

data = {
    'Order_ID': [f'ORD{1000 + i}' for i in range(n_rows)],
    'Order_Date': [datetime(2024, 1, 1) + timedelta(days=int(np.random.randint(0, 365))) for i in range(n_rows)],
    'Region': [np.random.choice(regions) for _ in range(n_rows)],
    'Category': [np.random.choice(categories) for _ in range(n_rows)],
}

data['Product_Name'] = [np.random.choice(products[cat]) for cat in data['Category']]
data['Quantity'] = np.random.randint(1, 10, size=n_rows)
# FIXED: used Python's built-in round function
data['Unit_Price'] = [round(np.random.uniform(5, 500), 2) for _ in range(n_rows)]

df = pd.DataFrame(data)
df['Sales'] = df['Quantity'] * df['Unit_Price']
df['Profit'] = (df['Sales'] * np.random.uniform(0.1, 0.4, size=n_rows)).round(2)

# 1. Injecting Duplicates for cleaning task
df_duplicates = df.sample(n=30, random_state=42)
df = pd.concat([df, df_duplicates], ignore_index=True)

# 2. Injecting Null/NaN values for cleaning task
df.loc[df.sample(n=25, random_state=10).index, 'Region'] = np.nan
df.loc[df.sample(n=20, random_state=20).index, 'Profit'] = np.nan

# Save to data/raw/
df.to_csv('data/raw/raw_sales_data.csv', index=False)
print("Success: 'raw_sales_data.csv' has been created inside data/raw/ folder!")