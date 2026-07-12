import pandas as pd
import random
from faker import Faker

# -------------------------------------------------
# Configuration
# -------------------------------------------------

fake = Faker("en_IN")
Faker.seed(42)
random.seed(42)

# -------------------------------------------------
# Read Cleaned Dataset
# -------------------------------------------------

df = pd.read_excel("data/cleaned/placement_data_cleaned.xlsx")

print("="*60)
print("PLACEMENT ANALYTICS SYSTEM")
print("TRANSFORMATION STARTED")
print("="*60)

# -------------------------------------------------
# Students
# -------------------------------------------------

students = (
    df[["Student_ID", "Department"]]
    .drop_duplicates(subset=["Student_ID"])
    .sort_values("Student_ID")
    .reset_index(drop=True)
)

students["Name"] = [fake.name() for _ in range(len(students))]

students["Gender"] = [
    random.choice(["Male","Female"])
    for _ in range(len(students))
]

students["Graduation_Year"] = [
    random.choice([2023,2024,2025,2026])
    for _ in range(len(students))
]

students["CGPA"] = [
    round(random.uniform(6.0,9.9),2)
    for _ in range(len(students))
]

students = students[
    [
        "Student_ID",
        "Name",
        "Gender",
        "Department",
        "Graduation_Year",
        "CGPA"
    ]
]

# -------------------------------------------------
# Companies
# -------------------------------------------------

company_names = [
"TCS",
"Infosys",
"Accenture",
"Wipro",
"Cognizant",
"Capgemini",
"IBM",
"HCLTech",
"Tech Mahindra",
"Deloitte",
"Oracle",
"Google",
"Microsoft",
"Amazon",
"Adobe",
"LTIMindtree",
"Persistent",
"Mphasis",
"Hexaware",
"DXC Technology"
]

industries = [
"IT Services",
"Consulting",
"Cloud",
"Software",
"Product",
"Technology"
]

locations = [
"Hyderabad",
"Bengaluru",
"Chennai",
"Pune",
"Noida",
"Mumbai"
]

companies = (
    df[["Company_ID"]]
    .drop_duplicates()
    .sort_values("Company_ID")
    .reset_index(drop=True)
)

companies["Company_Name"] = company_names[:len(companies)]

companies["Industry"] = [
    random.choice(industries)
    for _ in range(len(companies))
]

companies["Location"] = [
    random.choice(locations)
    for _ in range(len(companies))
]

companies = companies[
    [
        "Company_ID",
        "Company_Name",
        "Industry",
        "Location"
    ]
]

# -------------------------------------------------
# Jobs
# -------------------------------------------------

jobs = (
    df[
        [
            "Company_ID",
            "Job_Role",
            "Salary"
        ]
    ]
    .drop_duplicates()
    .reset_index(drop=True)
)

jobs.insert(
    0,
    "Job_ID",
    range(1,len(jobs)+1)
)

jobs.rename(
    columns={
        "Salary":"Salary_Offered"
    },
    inplace=True
)

jobs["Job_Type"] = [
    random.choice(
        [
            "Full-Time",
            "Internship"
        ]
    )
    for _ in range(len(jobs))
]

# -------------------------------------------------
# Applications
# -------------------------------------------------

applications = df[
    [
        "Student_ID",
        "Company_ID",
        "Job_Role",
        "Salary",
        "Application_Date",
        "Status"
    ]
].copy()

applications = applications.merge(

    jobs[
        [
            "Job_ID",
            "Company_ID",
            "Job_Role",
            "Salary_Offered"
        ]
    ],

    left_on=[
        "Company_ID",
        "Job_Role",
        "Salary"
    ],

    right_on=[
        "Company_ID",
        "Job_Role",
        "Salary_Offered"
    ],

    how="left"

)

applications.insert(
    0,
    "Application_ID",
    range(1,len(applications)+1)
)

applications = applications[
    [
        "Application_ID",
        "Student_ID",
        "Job_ID",
        "Application_Date",
        "Status"
    ]
]

# -------------------------------------------------
# Placements
# -------------------------------------------------

placements = df[
    [
        "Placement_ID",
        "Student_ID",
        "Company_ID",
        "Job_Role",
        "Salary",
        "Placement_Date"
    ]
].copy()

placements = placements.merge(

    jobs[
        [
            "Job_ID",
            "Company_ID",
            "Job_Role",
            "Salary_Offered"
        ]
    ],

    left_on=[
        "Company_ID",
        "Job_Role",
        "Salary"
    ],

    right_on=[
        "Company_ID",
        "Job_Role",
        "Salary_Offered"
    ],

    how="left"

)

placements = placements[
    [
        "Placement_ID",
        "Student_ID",
        "Company_ID",
        "Job_ID",
        "Placement_Date",
        "Salary"
    ]
]

# -------------------------------------------------
# Save Files
# -------------------------------------------------

students.to_excel(
    "data/processed/students.xlsx",
    index=False
)

companies.to_excel(
    "data/processed/companies.xlsx",
    index=False
)

jobs.to_excel(
    "data/processed/jobs.xlsx",
    index=False
)

applications.to_excel(
    "data/processed/applications.xlsx",
    index=False
)

placements.to_excel(
    "data/processed/placements.xlsx",
    index=False
)

print("\nTransformation Summary")
print("-"*60)

print("Students      :",len(students))
print("Companies     :",len(companies))
print("Jobs          :",len(jobs))
print("Applications  :",len(applications))
print("Placements    :",len(placements))

print("\nProcessed files created successfully.")

print("="*60)
print("TRANSFORMATION COMPLETED")
print("="*60)