#Question:
#sing the Pandas library, perform the following tasks:

#1. Create a DataFrame from the following data:
#| Name     | Age | Department   | Salary  |
#|----------|-----|--------------|---------|
#| John     | 28  | HR           | 45000   |
#| Alice    | 34  | IT           | 60000   |
#| Bob      | 23  | Marketing    | 35000   |
#| Diana    | 29  | Finance      | 50000   |
import pandas as pd

# Create a DataFrame with the provided data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}

df = pd.DataFrame(data)

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())



