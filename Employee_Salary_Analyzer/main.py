import pandas as pd
#===============================
# READ DATASET
#===============================

df=pd.read_csv("Employee_Salary_Analyzer/employees.csv")
print("\n"+"="*50)
print("       Employees Salary Analyzer ")
print("="*50)

#===============================
# Total compensation 
#===============================
df["Total Compensation"]=(
    df["Salary"]+df["Bonus"]
)

#===============================
# Highest And Lowest Paid Employees
#===============================
Highest_Paid=df.loc[
    df["Salary"].idxmax()
]

Lowest_Paid=df.loc[
    df["Salary"].idxmin()
]

print("\nHighest Paid Employee")
print("-"*50)
print(f"Name       : {Highest_Paid['Name']}")
print(f"EmployeeID : {Highest_Paid['EmployeeID']}")
print(f"Salary     : {Highest_Paid['Salary']}")
print(f"Department : {Highest_Paid['Department']}")
print(f"Experience : {Highest_Paid['Experience']}")
print(f"Bonus      : {Highest_Paid['Bonus']}")
print(f"Total Compensation : {Highest_Paid['Total Compensation']}")
print("-"*50)
print("\nLowest Paid Employee")
print("-"*50)
print(f"Name:        {Lowest_Paid['Name']}")
print(f"EmployeeID : {Lowest_Paid['EmployeeID']}")
print(f"Salary :     {Lowest_Paid['Salary']}")
print(f"Department : {Lowest_Paid['Department']}")
print(f"Experience : {Lowest_Paid['Experience']}")
print(f"Bonus      : {Lowest_Paid['Bonus']}")
print(f"Total Compensation : {Lowest_Paid['Total Compensation']}")

#==============================
# Top 10 Ranking
#==============================
print("\nTop 10 highest Salaries")
print("-"*50)
top10=df.nlargest(
    10,
    "Salary"
)
print(top10[["Name","EmployeeID","Salary","Department","Experience"]])

#===============================
# Department Wise Analysis
#===============================
dept_avg=(
    df.groupby("Department")["Salary"]
        .mean()
        .round(2)
)
dep_max=(
    df.groupby("Department")["Salary"]
    .max()
)
dep_min=(
    df.groupby("Department")["Salary"]
    .min()
)
dep_Employees=df["Department"].value_counts()
dep_total=(
    df.groupby("Department")["Salary"]
    .sum()
)
#================================
# Depatment Wise Output
#================================
print("\nDEPARTMENT WISE ANALYSIS")
print("-" * 50)
dept_analysis = pd.DataFrame({
    "Average Salary": dept_avg,
    "Maximum Salary": dep_max,
    "Minimum Salary": dep_min,
    "Employee Count": dep_Employees,
    "Total Expenses": dep_total,
})

print(dept_analysis.to_string())

#=================================
# CITY WISE ANALYSIS 
#=================================
city_avg=(
    df.groupby("City")["Salary"]
    .mean()
    .round(2)
)
city_max=(
    df.groupby("City")["Salary"]
    .max()
)
city_min=(
    df.groupby("City")["Salary"]
    .min()
)
city_Employees=df["City"].value_counts()
city_total=(
    df.groupby("City")["Salary"]
    .sum()
)

#=================================
# CITY WISE OUTPUT
#=================================
print("\nCITY WISE ANALYSIS")
print("-" * 50)

city_analysis=pd.DataFrame({
    "Average Salary"     : city_avg,
    "Maximum Salary"     : city_max,
    "Minimum Salary"     : city_min,
    "Employees count"    : city_Employees,
    "Total Expenses"     : city_total,
})

print(city_analysis.to_string())

#=================================
# GENDER WISE ANALYSIS
#=================================
Gen_avg=(
    df.groupby("Gender")["Salary"]
    .mean()
    .round(2)
)
Gen_max=(
    df.groupby("Gender")["Salary"]
    .max()
)
Gen_min=(
    df.groupby("Gender")["Salary"]
    .min()
)
Gen_Employees=df["Gender"].value_counts()
Gen_total=(
    df.groupby("Gender")["Salary"]
    .sum()
)

#===============================
# GENDER WISE OUTPUT
#===============================
print("\nGENDER WISE ANALYSIS")
print("-" * 50)

Gen_analysis=pd.DataFrame({
    "Average Salary"     : Gen_avg,
    "Maximum Salary"     : Gen_max,
    "Minimum Salary"     : Gen_min,
    "Employees count"    : Gen_Employees,
    "Total Expenses"     : Gen_total,
})

print(Gen_analysis.to_string())

#====================================
# ATTENDANCE ANALYSIS
#====================================
 
# LOW ATTENDANCE EMPLOYEES
low_attendance=df[df["Attendance"]<80]
print("\n LOW ATTENDANCE EMPLOYEES")
print("-"*50)
print(low_attendance[["Name","Attendance","Experience"]])

best_attendance = df.loc[
    df["Attendance"].idxmax()
]
avg_attendance=df["Attendance"].mean().round(2)
highest_att=df["Attendance"].max()
lowest_att=df["Attendance"].min()

#======================================
# BEST ATTENDANCE EMPLOYEESS
#======================================
print("\nBEST ATTENDANCE EMPLOYEE")
print("-" * 50)
print(f"Name        : {best_attendance['Name']}")
print(f"Department  : {best_attendance['Department']}")
print(f"Attendance  : {best_attendance['Attendance']}")
print(f"Experience  : {best_attendance['Experience']}")

print("-"*50)
print("Average attendance :",avg_attendance)
print("Highest attendance :",highest_att)
print("Lowest attendance :",lowest_att)


#====================================
# EXPERIENCE ANALYSIS
#====================================

most_exp=df.loc[
    df["Experience"].idxmax()
]
least_exp=df.loc[
    df["Experience"].idxmin()
]

print("\nMost Experienced Employee")
print("-"*50)
print(f"Name       : {most_exp['Name']}")
print(f"EmployeeID : {most_exp['EmployeeID']}")
print(f"Salary     : {most_exp['Salary']}")
print(f"Department : {most_exp['Department']}")
print(f"Experience : {most_exp['Experience']}")
print(f"Bonus      : {most_exp['Bonus']}")
print(f"Total Compensation : {most_exp['Total Compensation']}")
print("-"*50)
print("\nLeast Experienced Employee")
print("-"*50)
print(f"Name       : {least_exp['Name']}")
print(f"EmployeeID : {least_exp['EmployeeID']}")
print(f"Salary     : {least_exp['Salary']}")
print(f"Department : {least_exp['Department']}")
print(f"Experience : {least_exp['Experience']}")
print(f"Bonus      : {least_exp['Bonus']}")
print(f"Total Compensation : {least_exp['Total Compensation']}")

high_exp=df["Experience"].max()
avg_exp=df["Experience"].mean().round(2)
low_exp=df["Experience"].min()

print("-"*50)
print("Average Experience :",avg_exp)
print("Highest Experience :",high_exp)
print("Lowest Experience  :",low_exp)

#====================================
# EXPERIENCE VS SALARY ANALYSIS
#====================================

exp_analysis = df.groupby("Experience").agg(
    Average_Salary=("Salary", "mean"),
    Employee_Count=("EmployeeID", "count")
).round(2)

print("\nEXPERIENCE VS SALARY ANALYSIS")
print("-" * 50)
print(exp_analysis.to_string())

#====================================
# OUTPUT STATISTICS
#====================================

print("\n OVERALL STATISTICS ")
print("-"*50)
print(f"Total Employees     :{len(df)}")
print(f"Average Salary      :{df['Salary'].mean().round(2)}")
print(f"Highest Salary      :{df['Salary'].max()}")
print(f"Lowest Salary       :{df['Salary'].min()}")
print(f"Average Attendance  :{df['Attendance'].mean().round(2)}")
print(f"Highest Attendance  :{df['Attendance'].max()}")
print(f"Lowest Attendance   :{df['Attendance'].min()}")
print(f"Average Experience  :{df['Experience'].mean().round(2)}")
print(f"Highest Experience  :{df['Experience'].max()}")
print(f"Lowest Experience   :{df['Experience'].min()}")

df.to_csv("Employee_Salary_Analyzer/employee_report.csv", index=False)
print("\nemployee_report.csv generated successfully!")