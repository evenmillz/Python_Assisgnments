import pandas as pd

# Load the data from the CSV file
data = pd.read_csv(r'C:\Users\evenrichardson\dev\Python_Assisgnments\pandas_assignments\data\grades.csv')

# Calculate the average grade for each student
average_grades = data.groupby('Student Name')['Grade'].mean()

# Calculate and print the maximum grade in the class
max_grade = data['Grade'].max()
print('Highest grade in the class: ', max_grade)

# Calculate and print the minimum grade in the class
min_grade = data['Grade'].min()
print('Lowest grade in the class: ', min_grade)

# Calculate and print the average grade for the class
class_average = data['Grade'].mean()
print('Average grade for the class: ', class_average)

# Create a new column called "Pass/Fail" that indicates whether 
# each student passed or failed the course (assuming a passing 
# grade is 60 or above)
data['Pass/Fail'] = data['Grade'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')
print(data)

# Count the number of students who passed and failed
pass_count = data[data['Pass/Fail'] == 'Pass'].shape[0]
fail_count = data[data['Pass/Fail'] == 'Fail'].shape[0]
print('Number of students who passed: ', pass_count)
print('Number of students who failed: ', fail_count)
