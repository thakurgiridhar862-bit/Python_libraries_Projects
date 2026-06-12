# Employee Salary Analyzer

## Overview

Employee Salary Analyzer is a Python-based data analysis and visualization project that analyzes employee salary data to generate meaningful business insights related to compensation, departments, cities, attendance, gender distribution, and employee experience.

The project uses Pandas for data analysis and Matplotlib for data visualization.

---

## Features

### Salary Analysis

* Highest Paid Employee Analysis
* Lowest Paid Employee Analysis
* Total Compensation Calculation
* Top 10 Highest Paid Employees

### Department Analysis

* Average Salary by Department
* Maximum Salary by Department
* Minimum Salary by Department
* Employee Count by Department
* Total Department Salary Expenses

### City Analysis

* Average Salary by City
* Maximum Salary by City
* Minimum Salary by City
* Employee Count by City
* Total City Salary Expenses

### Gender Analysis

* Gender-wise Salary Statistics
* Gender Distribution Analysis

### Attendance Analysis

* Low Attendance Employee Detection
* Best Attendance Employee
* Average Attendance Statistics

### Experience Analysis

* Most Experienced Employee
* Least Experienced Employee
* Average Experience Statistics
* Experience vs Salary Analysis

### Report Generation

* Employee Report CSV Generation
* Summary Statistics

---

## Visualizations

The project generates the following graphs:

1. Top 10 Highest Paid Employees
2. Department-wise Average Salary
3. City-wise Average Salary
4. Gender-wise Employee Distribution
5. Employee Attendance Distribution
6. Average Salary by Experience

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib

---

## Dataset Columns

* EmployeeID
* Name
* Department
* Gender
* Age
* Experience
* City
* Salary
* Bonus
* Attendance

---

## Project Structure

```text
Employee_Salary_Analyzer/
│
├── data.py
├── main.py
├── employees.csv
├── employee_report.csv
│
├── graphs/
│   ├── top_10_highest_salaries.png
│   ├── dept_wise_avg_salaries.png
│   ├── city_wise_avg_salaries.png
│   ├── gender_wise_employee_dist.png
│   ├── attendance_dist.png
│   └── avg_salary_by_experience.png
│
└── README.md
```

---

## How to Run

Generate Dataset:

```bash
python data.py
```

Run Analysis:

```bash
python main.py
```

---

## Output

The project generates:

* employee_report.csv
* Visualization graphs in the graphs folder

---

## Key Business Insights

* Identify the highest and lowest paid employees
* Compare salary trends across departments
* Compare salary trends across cities
* Analyze workforce gender distribution
* Monitor employee attendance patterns
* Understand the relationship between experience and salary
* Generate overall workforce statistics

---

## Author

Giridhar Jadon

B.Tech AIML Student | Learning Data Analysis, Data Visualization, Machine Learning, and AI with Python.
