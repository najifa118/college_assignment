# I. Create the student dictionary
student = {
    'first_name': 'Najifa',
    'last_name': 'Parvin',
    'gender': 'FeMale',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],
    'country': 'INDIA',
    'city': 'Newtown',
    'address': 'PIN: 700160'
}

# II. Get the length of the student dictionary
length_student = len(student)
print("Length of student dictionary:", length_student)

# III. Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))  # Should output 

# IV. Modify the skills values by adding one or two skills
student['skills'].append('PLSQL')
student['skills'].append('C++')
print("Updated skills:", student['skills'])

# V. Get the dictionary keys as a list
keys = list(student.keys())
print("Dictionary keys:", keys)

# VI. Get the dictionary values as a list
values = list(student.values())
print("Dictionary values:", values)

# VII. Change the dictionary to a list of tuples using items() method
items = list(student.items())
print("Dictionary as list of tuples:", items)

# VIII. Delete one of the items in the dictionary
del student['marital_status']
print("Student dictionary after deleting 'marital_status':", student)

# IX. Delete the dictionary completely
del student
print("Student dictionary deleted.")

     
