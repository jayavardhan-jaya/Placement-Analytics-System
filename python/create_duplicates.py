import pandas as pd

df = pd.read_excel("data/raw/placement_1000_rows.csv.xlsx")

print("Original Rows:", len(df))

duplicates = df.sample(n=150, random_state=42)

new_df = pd.concat([df, duplicates], ignore_index=True)

print("Rows After Adding Duplicates:", len(new_df))

new_df.to_excel(
    "data/raw/placement_with_duplicates.xlsx",
    index=False
)

print("File Created Successfully")