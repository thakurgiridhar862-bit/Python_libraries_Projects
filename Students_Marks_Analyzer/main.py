import pandas as pd

# READ DATASET
df = pd.read_csv("Students_Marks_Analyzer/students.csv")

print("\n" + "=" * 50)
print("      STUDENT MARKS ANALYZER")
print("=" * 50)

# TOTAL MARKS
df["Total"] = (
    df["Maths"] + df["Physics"] + df["Chemistry"] + df["Computers"] + df["Soft Skills"]
)

# PERCENTAGE
df["Percentage"] = (df["Total"] / 500) * 100

# GRADE SYSTEM


def grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


df["Grade"] = df["Percentage"].apply(grade)

# RANKING
df["Rank"] = df["Total"].rank(ascending=False, method="dense").astype(int)

# CLASS TOPPER
topper = df.loc[df["Total"].idxmax()]

print("\nCLASS TOPPER")
print("-" * 50)
print(f"Name        : {topper['Name']}")
print(f"Total Marks : {topper['Total']}")
print(f"Percentage  : {topper['Percentage']:.2f}%")
print(f"Grade       : {topper['Grade']}")

# TOP 10 STUDENTS
print("\nTOP 10 STUDENTS")
print("-" * 50)

top10 = df.nlargest(10, "Total")

print(top10[["Name", "Total", "Percentage", "Grade", "Rank"]])

# SUBJECT TOPPERS
maths_topper = df.loc[df["Maths"].idxmax()]
physics_topper = df.loc[df["Physics"].idxmax()]
chemistry_topper = df.loc[df["Chemistry"].idxmax()]
computer_topper = df.loc[df["Computers"].idxmax()]
softskills_topper = df.loc[df["Soft Skills"].idxmax()]

print("\nSUBJECT TOPPERS")
print("-" * 50)

print(f"Maths        : {maths_topper['Name']} ({maths_topper['Maths']})")
print(f"Physics      : {physics_topper['Name']} ({physics_topper['Physics']})")
print(f"Chemistry    : {chemistry_topper['Name']} ({chemistry_topper['Chemistry']})")
print(f"Computers    : {computer_topper['Name']} ({computer_topper['Computers']})")
print(
    f"Soft Skills  : {softskills_topper['Name']} ({softskills_topper['Soft Skills']})"
)

# LOW ATTENDANCE
print("\nLOW ATTENDANCE STUDENTS (<75%)")
print("-" * 50)

low_attendance = df[df["Attendance"] < 75]

print(low_attendance[["Name", "Attendance"]])

# CLASS WISE AVERAGE
print("\nCLASS WISE AVERAGE PERCENTAGE")
print("-" * 50)

class_avg = df.groupby("Class")["Percentage"].mean().round(2)

print(class_avg)

# FAILED STUDENTS
fail_students = df[
    (df["Maths"] < 40)
    | (df["Physics"] < 40)
    | (df["Chemistry"] < 40)
    | (df["Computers"] < 40)
    | (df["Soft Skills"] < 40)
]

print("\nFAILED STUDENTS")
print("-" * 50)

print(
    fail_students[["Name", "Maths", "Physics", "Chemistry", "Computers", "Soft Skills"]]
)

# GRADE DISTRIBUTION
print("\nGRADE DISTRIBUTION")
print("-" * 50)

print(df["Grade"].value_counts())

# TOPPER OF EACH CLASS
print("\nTOPPER OF EACH CLASS")
print("-" * 50)

class_toppers = df.sort_values(by="Total", ascending=False).groupby("Class").first()

print(class_toppers[["Name", "Total", "Percentage"]])

# OVERALL STATISTICS
print("\nOVERALL STATISTICS")
print("-" * 50)

print(f"Total Students : {len(df)}")
print(f"Average Marks  : {df['Total'].mean():.2f}")
print(f"Highest Marks  : {df['Total'].max()}")
print(f"Lowest Marks   : {df['Total'].min()}")

# FINAL REPORT
df.to_csv("Students_Marks_Analyzer/student_report.csv", index=False)

print("\nstudent_report.csv generated successfully!")
print("=" * 50)
