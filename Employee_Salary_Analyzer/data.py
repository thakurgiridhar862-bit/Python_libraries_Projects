import numpy as np
import pandas as pd

# =====================================
# RANDOM SEED
# =====================================
np.random.seed(42)

# =====================================
# NUMBER OF EMPLOYEES
# =====================================
n = 500

# =====================================
# DATASET GENERATION
# =====================================
data = {
    "EmployeeID": range(1001, 1001 + n),

    "Name": [f"Employee_{i}" for i in range(1, n + 1)],

    "Department": np.random.choice(
        ["WebDev", "AIML", "Finance", "Marketing", "Sales", "IT"],
        n
    ),

    "Gender": np.random.choice(
        ["Male", "Female"],
        n
    ),

    "Age": np.random.randint(
        21,
        60,
        n
    ),

    "Experience": np.random.randint(
        0,
        20,
        n
    ),

    "City": np.random.choice(
        ["Agra", "Delhi", "Noida", "Gurugram", "Meerut"],
        n
    ),

    "Salary": np.random.randint(
        30000,
        300000,
        n
    ),

    "Bonus": np.random.randint(
        5000,
        50000,
        n
    ),

    "Attendance": np.random.randint(
        70,
        100,
        n
    ),
}

# =====================================
# CREATE DATAFRAME
# =====================================
df = pd.DataFrame(data)

# =====================================
# SAVE CSV
# =====================================
df.to_csv(
    "Employee_Salary_Analyzer/employees.csv",
    index=False
)

# =====================================
# PREVIEW
# =====================================
print("\nCSV Generated Successfully!")
print("-" * 50)
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDepartments:")
print(df["Department"].value_counts())

print("\nCities:")
print(df["City"].value_counts())

print("\nGender:")
print(df["Gender"].value_counts())