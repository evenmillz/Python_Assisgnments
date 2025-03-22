import pandas as pd

# Load the data from the CSV file
data = pd.read_csv(r'C:\Users\evenrichardson\dev\Python_Assisgnments\pandas_assignments\data\grades.csv')

# Calculate the average grade for each student
average_grades = data.groupby('Student Name')['Grade'].mean()

# Calculate and print the maximum grade in the class
max_grade = data['Grade'].max()
print('Highest grade in the class: ', max_grade)

