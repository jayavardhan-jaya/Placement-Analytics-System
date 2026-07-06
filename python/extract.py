import pandas as pd

df = pd.read_excel(
    "data/raw/placement_with_duplicates.xlsx"
)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())