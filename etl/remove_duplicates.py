import pandas as pd

# ---------------------------------
# Read Dataset with Duplicates
# ---------------------------------
input_file = "data/raw/placement_data_duplicates.xlsx"

df = pd.read_excel(input_file)

print("Total Rows Before Cleaning :", len(df))

# ---------------------------------
# Count Duplicate Records
# ---------------------------------
duplicate_count = df.duplicated().sum()

print("Duplicate Rows Found :", duplicate_count)

# ---------------------------------
# Remove Duplicate Records
# ---------------------------------
df_cleaned = df.drop_duplicates()

print("Total Rows After Cleaning :", len(df_cleaned))

# ---------------------------------
# Save Cleaned Dataset
# ---------------------------------
output_file = "data/cleaned/placement_data_cleaned.xlsx"

df_cleaned.to_excel(
    output_file,
    index=False
)

print("\nDuplicates Removed Successfully")
print("Cleaned File Saved As :", output_file)