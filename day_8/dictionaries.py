#Exercise: Day 8 of 30 Days of Python (Dictionaries)

dog = {}

dog = {
    'name' : 'James',
    'color' : 'Brown',
    'breed' : 'German Shephard',
    'legs': 'Four',
    'age': 'Three'
}
print(dog)

student = {
    'first_name' : 'John',
    'last_name' : 'Smith',
    'gender' : 'Male',
    'age' : '18',
    'marital status' : 'single',
    'skills' : ['HTML', 'CSS'],
    'country' : ' United States',
    'city' : 'New York',
    'Address' : '123 John Road'
}

print(student)
print(len(student))
print(type(student['skills']))
student['skills'].append('JavaScript')
print(student)
print(student.keys())
print(student.values())
print(student.items())
#del student['address']
print(student)
#del student