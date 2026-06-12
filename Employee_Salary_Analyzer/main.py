import pandas as pd
import matplotlib.pyplot as plt
# ===============================
# READ DATASET
# ===============================

df = pd.read_csv("Employee_Salary_Analyzer/employees.csv")
print("\n" + "=" * 50)
print("       Employees Salary Analyzer ")
print("=" * 50)

# ===============================
# Total compensation
# ===============================
df["Total Compensation"] = df["Salary"] + df["Bonus"]

# ===============================
# Highest And Lowest Paid Employees
# ===============================
Highest_Paid = df.loc[df["Salary"].idxmax()]

Lowest_Paid = df.loc[df["Salary"].idxmin()]

print("\nHighest Paid Employee")
print("-" * 50)
print(f"Name       : {Highest_Paid['Name']}")
print(f"EmployeeID : {Highest_Paid['EmployeeID']}")
print(f"Salary     : {Highest_Paid['Salary']}")
print(f"Department : {Highest_Paid['Department']}")
print(f"Experience : {Highest_Paid['Experience']}")
print(f"Bonus      : {Highest_Paid['Bonus']}")
print(f"Total Compensation : {Highest_Paid['Total Compensation']}")
print("-" * 50)
print("\nLowest Paid Employee")
print("-" * 50)
print(f"Name:        {Lowest_Paid['Name']}")
print(f"EmployeeID : {Lowest_Paid['EmployeeID']}")
print(f"Salary :     {Lowest_Paid['Salary']}")
print(f"Department : {Lowest_Paid['Department']}")
print(f"Experience : {Lowest_Paid['Experience']}")
print(f"Bonus      : {Lowest_Paid['Bonus']}")
print(f"Total Compensation : {Lowest_Paid['Total Compensation']}")

# ==============================
# Top 10 Ranking
# ==============================
print("\nTop 10 highest Salaries")
print("-" * 50)
top10 = df.nlargest(10, "Salary")
print(top10[["Name", "EmployeeID", "Salary", "Department", "Experience"]])

# ===============================
# Department Wise Analysis
# ===============================
dept_avg = df.groupby("Department")["Salary"].mean().round(2)
dep_max = df.groupby("Department")["Salary"].max()
dep_min = df.groupby("Department")["Salary"].min()
dep_Employees = df["Department"].value_counts()
dep_total = df.groupby("Department")["Salary"].sum()
# ================================
# Depatment Wise Output
# ================================
print("\nDEPARTMENT WISE ANALYSIS")
print("-" * 50)
dept_analysis = pd.DataFrame(
    {
        "Average Salary": dept_avg,
        "Maximum Salary": dep_max,
        "Minimum Salary": dep_min,
        "Employee Count": dep_Employees,
        "Total Expenses": dep_total,
    }
)

print(dept_analysis.to_string())

# =================================
# CITY WISE ANALYSIS
# =================================
city_avg = df.groupby("City")["Salary"].mean().round(2)
city_max = df.groupby("City")["Salary"].max()
city_min = df.groupby("City")["Salary"].min()
city_Employees = df["City"].value_counts()
city_total = df.groupby("City")["Salary"].sum()

# =================================
# CITY WISE OUTPUT
# =================================
print("\nCITY WISE ANALYSIS")
print("-" * 50)

city_analysis = pd.DataFrame(
    {
        "Average Salary": city_avg,
        "Maximum Salary": city_max,
        "Minimum Salary": city_min,
        "Employees count": city_Employees,
        "Total Expenses": city_total,
    }
)

print(city_analysis.to_string())

# =================================
# GENDER WISE ANALYSIS
# =================================
Gen_avg = df.groupby("Gender")["Salary"].mean().round(2)
Gen_max = df.groupby("Gender")["Salary"].max()
Gen_min = df.groupby("Gender")["Salary"].min()
Gen_Employees = df["Gender"].value_counts()
Gen_total = df.groupby("Gender")["Salary"].sum()

# ===============================
# GENDER WISE OUTPUT
# ===============================
print("\nGENDER WISE ANALYSIS")
print("-" * 50)

Gen_analysis = pd.DataFrame(
    {
        "Average Salary": Gen_avg,
        "Maximum Salary": Gen_max,
        "Minimum Salary": Gen_min,
        "Employees count": Gen_Employees,
        "Total Expenses": Gen_total,
    }
)

print(Gen_analysis.to_string())

# ====================================
# ATTENDANCE ANALYSIS
# ====================================

# LOW ATTENDANCE EMPLOYEES
low_attendance = df[df["Attendance"] < 80]
print("\n LOW ATTENDANCE EMPLOYEES")
print("-" * 50)
print(low_attendance[["Name", "Attendance", "Experience"]])

best_attendance = df.loc[df["Attendance"].idxmax()]
avg_attendance = df["Attendance"].mean().round(2)
highest_att = df["Attendance"].max()
lowest_att = df["Attendance"].min()

# ======================================
# BEST ATTENDANCE EMPLOYEESS
# ======================================
print("\nBEST ATTENDANCE EMPLOYEE")
print("-" * 50)
print(f"Name        : {best_attendance['Name']}")
print(f"Department  : {best_attendance['Department']}")
print(f"Attendance  : {best_attendance['Attendance']}")
print(f"Experience  : {best_attendance['Experience']}")

print("-" * 50)
print("Average attendance :", avg_attendance)
print("Highest attendance :", highest_att)
print("Lowest attendance :", lowest_att)


# ====================================
# EXPERIENCE ANALYSIS
# ====================================

most_exp = df.loc[df["Experience"].idxmax()]
least_exp = df.loc[df["Experience"].idxmin()]

print("\nMost Experienced Employee")
print("-" * 50)
print(f"Name       : {most_exp['Name']}")
print(f"EmployeeID : {most_exp['EmployeeID']}")
print(f"Salary     : {most_exp['Salary']}")
print(f"Department : {most_exp['Department']}")
print(f"Experience : {most_exp['Experience']}")
print(f"Bonus      : {most_exp['Bonus']}")
print(f"Total Compensation : {most_exp['Total Compensation']}")
print("-" * 50)
print("\nLeast Experienced Employee")
print("-" * 50)
print(f"Name       : {least_exp['Name']}")
print(f"EmployeeID : {least_exp['EmployeeID']}")
print(f"Salary     : {least_exp['Salary']}")
print(f"Department : {least_exp['Department']}")
print(f"Experience : {least_exp['Experience']}")
print(f"Bonus      : {least_exp['Bonus']}")
print(f"Total Compensation : {least_exp['Total Compensation']}")

high_exp = df["Experience"].max()
avg_exp = df["Experience"].mean().round(2)
low_exp = df["Experience"].min()

print("-" * 50)
print("Average Experience :", avg_exp)
print("Highest Experience :", high_exp)
print("Lowest Experience  :", low_exp)

# ====================================
# EXPERIENCE VS SALARY ANALYSIS
# ====================================

exp_analysis = (
    df.groupby("Experience")
    .agg(Average_Salary=("Salary", "mean"), Employee_Count=("EmployeeID", "count"))
    .round(2)
)

print("\nEXPERIENCE VS SALARY ANALYSIS")
print("-" * 50)
print(exp_analysis.to_string())

# ====================================
# OUTPUT STATISTICS
# ====================================

print("\n OVERALL STATISTICS ")
print("-" * 50)
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


# ============================================
# VISUALISATION PROCESS
# ============================================

# GRAPH 1
fig, axes1 = plt.subplots(1, 1, figsize=(16, 5))
axes1.set_title("Top 10 Highest Paid Employees")
axes1.set_xlabel("Salary")
axes1.set_ylabel("Employee Name")
axes1.set_xlim(295000, 300000)
x1 = top10["Name"]
y1 = top10["Salary"]
color1 = ["green" if v == max(y1) else "red" if v == min(y1) else "blue" for v in y1]
bar1 = axes1.barh(x1, y1, color=color1)
axes1.bar_label(bar1, labels=[f"{v:,}" for v in y1], padding=5)
axes1.invert_yaxis()
axes1.grid(axis="x", linestyle="--", alpha=0.4)
plt.savefig(
    "Employee_Salary_Analyzer/graphs/top_10_highest_salaries.png",
    dpi=300,
    bbox_inches="tight",
)


# GRAPH 2
fig, axes2 = plt.subplots(1, 1, figsize=(16, 5))
axes2.set_title("Department Wise Average Salary")
axes2.set_xlabel("Department")
axes2.set_ylabel("Salary")
axes2.set_ylim(150000, 170000)
x2 = dept_avg.index
y2 = dept_avg.values
color2 = ["green" if v == max(y2) else "red" if v == min(y2) else "blue" for v in y2]
bar2 = axes2.bar(x2, y2, color=color2)
axes2.bar_label(bar2, labels=[f"{v:,.0f}" for v in y2], padding=5)
axes2.grid(axis="y", linestyle="--", alpha=0.4)
plt.savefig(
    "Employee_Salary_Analyzer/graphs/dept_wise_avg_salaries.png",
    dpi=300,
    bbox_inches="tight",
)


# GRAPH 3
fig, axes3 = plt.subplots(1, 1, figsize=(16, 5))
axes3.set_title("City-Wise Average Salary")
axes3.set_xlabel("City")
axes3.set_ylabel("Average Salary")
axes3.set_ylim(140000, 170000)
x3 = city_avg.index
y3 = city_avg.values
color3 = ["green" if v == max(y3) else "red" if v == min(y3) else "blue" for v in y3]
bar3 = axes3.bar(x3, y3, color=color3)
axes3.bar_label(bar3, labels=[f"{v:,.0f}" for v in y3], padding=5)
axes3.grid(axis="y", linestyle="--", alpha=0.4)
plt.savefig(
    "Employee_Salary_Analyzer/graphs/city_wise_avg_salaries.png",
    dpi=300,
    bbox_inches="tight",
)

# GRAPH 4
fig, axes4 = plt.subplots(1, 1, figsize=(8, 6))
axes4.set_title("Gender Wise Employee Distribution")
counts = Gen_Employees.values


def my_autopct(pct):
    count = int(round(pct / 100 * sum(counts)))
    return f"{count} ({pct:.1f}%)"


axes4.pie(
    Gen_Employees.values,
    labels=Gen_Employees.index,
    autopct=my_autopct,
    startangle=90,
    shadow=False,
    explode=[0.05, 0],
    textprops={"fontsize": 15},
)
axes4.axis("equal")
plt.savefig(
    "Employee_Salary_Analyzer/graphs/gender_wise_employee_dist.png",
    dpi=300,
    bbox_inches="tight",
)

# GRAPH 5
fig, axes5 = plt.subplots(1, 1, figsize=(16, 5))
axes5.set_title("Employee Attendance Distribution")
axes5.set_xlabel("Attendace (%)")
axes5.set_ylabel("Number of employees")
axes5.hist(df["Attendance"], bins=12, color="pink")
axes5.grid(axis="y", linestyle="--", alpha=0.3)
axes5.axvline(
    x=avg_attendance,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average ({avg_attendance:.2f})",
)
axes5.legend()
plt.savefig(
    "Employee_Salary_Analyzer/graphs/attendance_dist.png",
    dpi=300,
    bbox_inches="tight",
)


# GRAPH 6
fig, axes6 = plt.subplots(1, 1, figsize=(10, 5))

x6 = exp_analysis.index
y6 = exp_analysis["Average_Salary"]

axes6.plot(x6, y6, marker="o", linewidth=2)

axes6.set_title("Average Salary by Experience")
axes6.set_xlabel("Experience (Years)")
axes6.set_ylabel("Average Salary")
axes6.grid(linestyle="--", alpha=0.4)

plt.savefig(
    "Employee_Salary_Analyzer/graphs/avg_salary_by_experience.png",
    dpi=300,
    bbox_inches="tight",
)

df.to_csv("Employee_Salary_Analyzer/employee_report.csv", index=False)
print("\nemployee_report.csv generated successfully!")
