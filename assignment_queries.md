1. Display only IT employees
print(df[df["Department"] == "IT"])
2. Display employees with salary greater than ₹50,000
print(df[df["Salary"] > 50000])
3. Display employees with salary less than ₹50,000
print(df[df["Salary"] < 50000])
4. Find employees whose salary is between ₹50,000 and ₹70,000
print(df[(df["Salary"] >= 50000) & (df["Salary"] <= 70000)])

Here & means AND.

5. Find employees from IT with salary greater than ₹50,000
print(df[(df["Department"] == "IT") & (df["Salary"] > 50000)])
6. Find employees from IT or HR
print(df[
    (df["Department"] == "IT") |
    (df["Department"] == "HR")
])

Here | means OR.

7. Increase IT salaries by 10%
df.loc[df["Department"] == "IT", "Salary"] *= 1.10

print(df)
8. Increase Finance salaries by 5%
df.loc[df["Department"] == "Finance", "Salary"] *= 1.05

print(df)
9. Give ₹2,000 bonus to HR employees
df.loc[df["Department"] == "HR", "Salary"] += 2000

print(df)
10. Find the employee with the highest salary ⭐
print(df.loc[df["Salary"].idxmax()])

This will return the complete row of the employee with the highest salary.

11. Find the employee with the lowest salary
print(df.loc[df["Salary"].idxmin()])
12. Sort employees by salary
Lowest to highest
print(df.sort_values("Salary"))
Highest to lowest
print(df.sort_values("Salary", ascending=False))
13. Find average salary
average_salary = df["Salary"].mean()

print("Average Salary:", average_salary)
14. Find total salary
total_salary = df["Salary"].sum()

print("Total Salary:", total_salary)

This is useful for understanding the company's total salary expense.

15. Count number of employees
print("Total Employees:", len(df))
16. Count employees in each department ⭐
print(df["Department"].value_counts())

Example:

IT          3
HR          1
Finance     1
17. Calculate average salary by department
print(df.groupby("Department")["Salary"].mean())

This gives something like:

Department
Finance    55000
HR         45000
IT         58333.33
18. Find IT employees with salary below ₹60,000
print(df[
    (df["Department"] == "IT") &
    (df["Salary"] < 60000)
])
19. Create a new column Bonus

For example, give everyone a 10% bonus:

df["Bonus"] = df["Salary"] * 0.10

print(df)

Now your DataFrame becomes:

ID  Name     Department  Salary  Bonus
101 Preetii  IT          60000   6000
102 Sneha    HR          45000   4500
...
20. Create a new column Annual Salary

If your Salary is monthly:

df["Annual Salary"] = df["Salary"] * 12

print(df)
