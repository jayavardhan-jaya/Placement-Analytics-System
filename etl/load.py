import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.exc import SQLAlchemyError

# =====================================================
# Placement Analytics System
# ETL - Load Data into MySQL
# =====================================================

# -----------------------------------------------------
# Database Configuration
# -----------------------------------------------------

USERNAME = "root"
PASSWORD = "Jayavardhan@123"
HOST = "localhost"
PORT = 3306
DATABASE = "placement_analytics"

# -----------------------------------------------------
# Create Database Connection
# -----------------------------------------------------

try:

    connection_url = URL.create(

        drivername="mysql+pymysql",

        username=USERNAME,

        password=PASSWORD,

        host=HOST,

        port=PORT,

        database=DATABASE

    )

    engine = create_engine(connection_url)

    connection = engine.connect()

    print("=" * 60)
    print("SUCCESSFULLY CONNECTED TO MYSQL")
    print("=" * 60)

except SQLAlchemyError as e:

    print("\nDatabase Connection Failed!\n")

    print(e)

    exit()

# =====================================================
# Read Processed Files
# =====================================================

try:

    print("\nReading Processed Excel Files...\n")

    students = pd.read_excel("data/processed/students.xlsx")

    companies = pd.read_excel("data/processed/companies.xlsx")

    jobs = pd.read_excel("data/processed/jobs.xlsx")

    applications = pd.read_excel("data/processed/applications.xlsx")

    placements = pd.read_excel("data/processed/placements.xlsx")

    print("Files Read Successfully.\n")

except Exception as e:

    print("Unable to Read Excel Files")

    print(e)

    exit()

# =====================================================
# Load Order
# =====================================================

tables = [

    ("Companies", companies),

    ("Students", students),

    ("Jobs", jobs),

    ("Applications", applications),

    ("Placements", placements)

]

# =====================================================
# Load Data
# =====================================================

print("=" * 60)
print("LOADING DATA INTO MYSQL")
print("=" * 60)

for table_name, dataframe in tables:

    try:

        print(f"\nLoading {table_name}...")

        dataframe.to_sql(

            name=table_name,

            con=engine,

            if_exists="append",

            index=False

        )

        print(f"{table_name} Loaded Successfully")

        print(f"Rows Inserted : {len(dataframe)}")

    except Exception as e:

        print(f"\nError Loading {table_name}")

        print(e)

        connection.close()

        exit()

# =====================================================
# Close Connection
# =====================================================

connection.close()

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)

print("ALL TABLES LOADED SUCCESSFULLY")

print("=" * 60)

print("\nSUMMARY")

print("-" * 60)

print(f"Companies     : {len(companies)}")

print(f"Students      : {len(students)}")

print(f"Jobs          : {len(jobs)}")

print(f"Applications  : {len(applications)}")

print(f"Placements    : {len(placements)}")

print("\nData Loaded Successfully into MySQL.")