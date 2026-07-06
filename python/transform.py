import pandas as pd

# -----------------------------
# Step 1: Read Duplicate Dataset
# -----------------------------
df = pd.read_excel("data/raw/placement_with_duplicates.xlsx")

print("=" * 50)
print("DATA CLEANING STARTED")
print("=" * 50)

print(f"Rows Before Cleaning : {len(df)}")

# -----------------------------
# Step 2: Remove Duplicate Rows
# -----------------------------
duplicates = df.duplicated().sum()
print(f"Duplicate Rows Found : {duplicates}")

df = df.drop_duplicates()

print(f"Rows After Removing Duplicates : {len(df)}")

# -----------------------------
# Step 3: Check Missing Values
# -----------------------------
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing department
df["Department"] = df["Department"].fillna("Unknown")

# Remove rows with missing Salary
df = df.dropna(subset=["Salary"])

# -----------------------------
# Step 4: Convert Dates
# -----------------------------
df["Application_Date"] = pd.to_datetime(df["Application_Date"])
df["Placement_Date"] = pd.to_datetime(df["Placement_Date"])

# -----------------------------
# Step 5: Salary Validation
# -----------------------------
df = df[df["Salary"] > 0]

# -----------------------------
# Step 6: Date Validation
# -----------------------------
df = df[df["Placement_Date"] >= df["Application_Date"]]

# -----------------------------
# Step 7: Save Clean Dataset
# -----------------------------
df.to_excel(
    "data/cleaned/placements_clean.xlsx",
    index=False
)

print("\nClean dataset created successfully.")
print(f"Final Rows : {len(df)}")

print("=" * 50)
print("DATA CLEANING COMPLETED")
print("=" * 50)