#2. Write code to:
#- Display the first 2 rows of the DataFrame.
#- Add a new column named `Bonus` where the bonus is 10% of the salary.
#- Calculate the average salary of employees in the DataFrame.
#- Filter and display employees who are older than 25.
import pandas as pd

# Sample data for employees
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 22, 28, 35],
    'Salary': [50000, 60000, 45000, 55000, 70000]
}

# Create DataFrame
df = pd.DataFrame(data)

# 1. Display the first 2 rows of the DataFrame
print("First 2 rows of the DataFrame:")
print(df.head(2))

# 2. Add a new column named 'Bonus' where the bonus is 10% of the salary
df['Bonus'] = df['Salary'] * 0.10

# 3. Calculate the average salary of employees in the DataFrame
average_salary = df['Salary'].mean()
print("\nAverage Salary of Employees:", average_salary)

# 4. Filter and display employees who are older than 25
older_than_25 = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(older_than_25)

