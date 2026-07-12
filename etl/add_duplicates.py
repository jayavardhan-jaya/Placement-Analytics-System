import pandas as pd

# -------------------------------
# Read Original Dataset
# -------------------------------
df = pd.read_excel("data/raw/placement_data.xlsx")

print("Original Rows :", len(df))

# -------------------------------
# Randomly Select 150 Existing Rows
# -------------------------------
duplicate_rows = df.sample(
    n=150,
    random_state=42
)

# -------------------------------
# Append Duplicate Rows
# -------------------------------
df_with_duplicates = pd.concat(
    [df, duplicate_rows],
    ignore_index=True
)

# -------------------------------
# Save Dataset
# -------------------------------
output_file = "data/raw/placement_data_duplicates.xlsx"

df_with_duplicates.to_excel(
    output_file,
    index=False
)

print("150 Duplicate Rows Added Successfully")
print("New Total Rows :", len(df_with_duplicates))
print("Saved As :", output_file)