import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# STUDENT MARKS ANALYZER
# ==================================================

print("\n" + "=" * 50)
print("          STUDENT MARKS ANALYZER")
print("=" * 50)


# ==================================================
# 1. READ DATASET
# ==================================================

df = pd.read_csv("Students_Marks_Analyzer/students.csv")


# ==================================================
# 2. BASIC CALCULATIONS
# ==================================================

subjects = ["Maths", "Physics", "Chemistry", "Computers", "Soft Skills"]

df["Total"] = df[subjects].sum(axis=1)

df["Percentage"] = (df["Total"] / 500) * 100


# ==================================================
# 3. GRADE SYSTEM
# ==================================================


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


# ==================================================
# 4. RANKING
# ==================================================

df["Rank"] = df["Total"].rank(ascending=False, method="dense").astype(int)


# ==================================================
# 5. CLASS TOPPER
# ==================================================

topper = df.loc[df["Total"].idxmax()]

print("\nCLASS TOPPER")
print("-" * 50)
print(f"Name        : {topper['Name']}")
print(f"Total Marks : {topper['Total']}")
print(f"Percentage  : {topper['Percentage']:.2f}%")
print(f"Grade       : {topper['Grade']}")


# ==================================================
# 6. TOP 10 STUDENTS
# ==================================================

print("\nTOP 10 STUDENTS")
print("-" * 50)

top10 = df.nlargest(10, "Total")

print(top10[["Name", "Total", "Percentage", "Grade", "Rank"]])


# ==================================================
# 7. SUBJECT TOPPERS
# ==================================================

print("\nSUBJECT TOPPERS")
print("-" * 50)

for subject in subjects:
    subject_topper = df.loc[df[subject].idxmax()]
    print(f"{subject:<12}: {subject_topper['Name']} ({subject_topper[subject]})")


# ==================================================
# 8. LOW ATTENDANCE STUDENTS
# ==================================================

print("\nLOW ATTENDANCE STUDENTS (<75%)")
print("-" * 50)

low_attendance = df[df["Attendance"] < 75]

print(low_attendance[["Name", "Attendance"]])


# ==================================================
# 9. CLASS WISE AVERAGE PERCENTAGE
# ==================================================

print("\nCLASS WISE AVERAGE PERCENTAGE")
print("-" * 50)

class_avg = df.groupby("Class")["Percentage"].mean().round(2)

print(class_avg)


# ==================================================
# 10. FAILED STUDENTS
# ==================================================

print("\nFAILED STUDENTS")
print("-" * 50)

fail_students = df[(df[subjects] < 40).any(axis=1)]

print(fail_students[["Name"] + subjects])


# ==================================================
# 11. GRADE DISTRIBUTION
# ==================================================

print("\nGRADE DISTRIBUTION")
print("-" * 50)

grade_distribution = df["Grade"].value_counts()

print(grade_distribution)


# ==================================================
# 12. TOPPER OF EACH CLASS
# ==================================================

print("\nTOPPER OF EACH CLASS")
print("-" * 50)

class_toppers = df.sort_values(by="Total", ascending=False).groupby("Class").first()

print(class_toppers[["Name", "Total", "Percentage"]])


# ==================================================
# 13. OVERALL STATISTICS
# ==================================================

print("\nOVERALL STATISTICS")
print("-" * 50)

print(f"Total Students : {len(df)}")
print(f"Average Marks  : {df['Total'].mean():.2f}")
print(f"Highest Marks  : {df['Total'].max()}")
print(f"Lowest Marks   : {df['Total'].min()}")

# ===================================================
# VISUALIZATIONS PROCESS
# ===================================================

# graph 1
fig, axes = plt.subplots(1, 1, figsize=(16, 5))
axes.set_title("TOP 10 Students by Total Marks")
axes.set_xlabel("Student Name")
axes.set_ylabel("Marks")
axes.set_ylim(300, 500)
colors = [
    "green"
    if v == max(top10["Total"])
    else "red"
    if v == min(top10["Total"])
    else "blue"
    for v in top10["Total"]
]
average_marks = top10["Total"].mean()
bars = axes.bar(top10["Name"], top10["Total"], color=colors, alpha=0.5)
axes.axhline(
    y=average_marks,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average ({average_marks:.2f})",
)
axes.legend(loc=1)
axes.bar_label(bars, padding=5)
axes.grid(axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
plt.savefig(
    "Students_Marks_Analyzer/graphs/top10_students.png", dpi=300, bbox_inches="tight"
)


# grade vs students 2
grade_order = ["A+", "A", "B", "C", "D", "Fail"]
grade_distribution = grade_distribution.reindex(grade_order, fill_value=0)

fig, axes_grade = plt.subplots(1, 1, figsize=(16, 5))
x2 = grade_distribution.index
y2 = grade_distribution.values
axes_grade.set_title("Grade distribution of students")
axes_grade.set_xlabel("Grades")
axes_grade.set_ylabel("Number of students")
axes_grade.set_ylim(0, 250)
bars = axes_grade.bar(x2, y2, color="steelblue")

axes_grade.bar_label(bars, padding=5)
axes_grade.grid(axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
plt.savefig(
    "Students_Marks_Analyzer/graphs/grades_distribution.png",
    dpi=300,
    bbox_inches="tight",
)


# graph 3

fig, axes_per = plt.subplots(1, 1, figsize=(16, 5))
x3 = class_avg.index
y3 = class_avg.values
axes_per.set_title("Class Wise average percentage")
axes_per.set_xlabel("Class")
axes_per.set_ylabel("Average Percentage")
axes_per.set_ylim(0, 100)
color3 = ["green" if v == max(y3) else "blue" for v in y3]
bars = axes_per.bar(x3, y3, color=color3)

axes_per.bar_label(bars, labels=[f"{v:.2f}%" for v in y3], padding=5)
axes_per.grid(axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
plt.savefig(
    "Students_Marks_Analyzer/graphs/class_average_percentage.png",
    dpi=300,
    bbox_inches="tight",
)


# subject wise average
fig, axes_sub = plt.subplots(1, 1, figsize=(16, 5))
subject_avg = df[subjects].mean().round(2)
x4 = subject_avg.index
y4 = subject_avg.values
axes_sub.set_title("Subject Wise average Marks")
axes_sub.set_xlabel("Subject")
axes_sub.set_ylabel("Average Marks")
axes_sub.set_ylim(0, 100)
color4 = ["green" if v == max(y4) else "red" if v == min(y4) else "blue" for v in y4]
bars = axes_sub.bar(x4, y4, color=color4)
axes_sub.bar_label(bars, labels=[f"{v:.2f}" for v in y4], padding=5)
axes_sub.grid(axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
plt.savefig(
    "Students_Marks_Analyzer/graphs/subject_average_marks.png",
    dpi=300,
    bbox_inches="tight",
)


# graph 5
fig, axes_attend = plt.subplots(1, 1, figsize=(16, 5))
axes_attend.set_title("Attendance distribution")
axes_attend.set_xlabel("Attendance (%) ")
axes_attend.set_ylabel("Number of students ")
axes_attend.hist(df["Attendance"], bins=10, color="lightblue")
axes_attend.grid(axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
plt.savefig(
    "Students_Marks_Analyzer/graphs/attendance_distribution.png",
    dpi=300,
    bbox_inches="tight",
)

# graph six
fig, axes_percentage = plt.subplots(1, 1, figsize=(16, 5))
axes_percentage.set_title("Percentage distribution of students")
axes_percentage.set_xlabel("Percentage (%) ")
axes_percentage.set_ylabel("Number of students")
axes_percentage.hist(df["Percentage"], bins=10, color="lightgreen")
axes_percentage.grid(axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
plt.savefig(
    "Students_Marks_Analyzer/graphs/percentage_distribution.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close(fig)
# ==================================================
#  EXPORT FINAL REPORT
# ==================================================
print("\nAll graphs generated successfully!")
df.to_csv("Students_Marks_Analyzer/student_report.csv", index=False)

print("\nstudent_report.csv generated successfully!")
print("=" * 50)
