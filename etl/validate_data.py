import pandas as pd

# ---------------------------------
# Read Cleaned Dataset
# ---------------------------------
file_path = "data/cleaned/placement_data_cleaned.xlsx"

df = pd.read_excel(file_path)

print("=" * 50)
print("PLACEMENT DATA VALIDATION REPORT")
print("=" * 50)

# ---------------------------------
# Total Rows and Columns
# ---------------------------------
print(f"\nTotal Rows    : {len(df)}")
print(f"Total Columns : {len(df.columns)}")

# ---------------------------------
# Duplicate Check
# ---------------------------------
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows : {duplicates}")

# ---------------------------------
# Missing Values
# ---------------------------------
print("\nMissing Values")
print(df.isnull().sum())

# ---------------------------------
# Data Types
# ---------------------------------
print("\nData Types")
print(df.dtypes)

# ---------------------------------
# Salary Validation
# ---------------------------------
print("\nSalary Statistics")
print(df["Salary"].describe())

# ---------------------------------
# Status Distribution
# ---------------------------------
print("\nStatus Distribution")
print(df["Status"].value_counts())

print("\nValidation Completed Successfully")
print("=" * 50)