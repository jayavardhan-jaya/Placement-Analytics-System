import pandas as pd

# Read the dataset
df = pd.read_excel("data/raw/placement_data.xlsx")

# Display basic information
print("\nDataset Loaded Successfully")
print("-" * 40)
print(f"Total Rows    : {len(df)}")
print(f"Total Columns : {len(df.columns)}")

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())