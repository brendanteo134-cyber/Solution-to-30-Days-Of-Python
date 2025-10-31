#Day 9 of 30 Days of Python (Conditionals)

age_1 = input("Enter your age: ")
drive_requirement = int(18)
years_remaining = int (18) - int (age_1)
print(f"You are {age_1} years old.")

if int (age_1) >=drive_requirement:
    print(f"You are old enough to learn to drive")
else:
    print(f"You have to wait {years_remaining} before you can learn to drive")

age_me = input("Enter your age: ")
age_different_person = input("Enter your age: ")
age_difference = int (age_me) - int (age_different_person)
positive_age_difference = int(age_different_person) - int(age_me)
if int(age_difference)>0:
    print(f"I am {age_difference} years older than you.")
elif int(age_different_person)>int(age_me):
    print(f"I am {positive_age_difference} years younger than you.")
elif int(age_me)==int(age_different_person):
    print("We are both the same age.")

num_1 = input("Enter your number: ")
num_2 = input("Enter your number: ")
if int(num_1)>int(num_2):
    print(f"{num_1} is greater than {num_2}")
elif int(num_2)>int(num_1):
    print(f"{num_2} is greater than {num_1}")
else:
    print(f"{num_1} is equivalent to {num_2}")



student_grade = input("Enter the student's Score: ")
if int(student_grade)>80 and int(student_grade)<100:
    print(f"This student has scored {student_grade} and earned an A Grade")
if int(student_grade)>70 and int(student_grade)<89:
    print(f"This student has scored {student_grade} and earned an B Grade")
if int(student_grade)>60 and int(student_grade)<69:
    print(f"This student has scored {student_grade} and earned an C Grade")
if int(student_grade)>50 and int(student_grade)<59:
    print(f"This student has scored {student_grade} and earned an D Grade")
if int(student_grade)>0 and int(student_grade)<49:
    print(f"This student has scored {student_grade} and earned an F Grade")
elif int(student_grade)<0 or int(student_grade)>100:
    print(f"The input {student_grade} is invalid. Please reinput a valid number.")

Month = input("Enter the month: ")
Winter_Months = ("December", "January", "Feburary")
Autumn_Months = ("September", "October", "November")
Spring_Months = ("March", "April", "May")
Summer_Months = ("June", "July", "August")
if str(Month) in (Winter_Months):
    print(f"The month of {Month} is Winter!")
elif str(Month) in Autumn_Months:
    print(f"The month of {Month} is Autumn!")
elif str(Month) in Spring_Months:
    print(f"The month of {Month} is Spring!")
elif str(Month) in Summer_Months:
    print(f"The month of {Month} is Summer!")
else:
    print("Please input a valid Month!")

person= {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
         }
}

if person.get('skills'):
    if len(person['skills']) % 2 == 0:
        print(person['skills'][(len(person['skills'])//2) - 1],
              person['skills'][(len(person['skills'])//2)])
    else:
        print(person['skills'][len(person['skills'])//2])
else:
    print("No Skills")

if person.get('skills'):
    if 'Python' in person.get('skills'):
        print("Python is one of the skills")
    else:
        print("No Python in skills")
else:
    print("No Skills")

frontend = ["JavaScript", "React"]
backend = ["Node", "Python", "MongoDB"]
fullstack= ["React", "Node", "MongoDB"]
msg = "unknown title"

if("skills" in person):
    skills = person["skills"] 
    if all(skill in skills for skill in frontend):
        msg = 'He is a front end developer'
    if all(skill in skills for skill in backend):    
        msg = 'He is a backend developer'
    if all(skill in skills for skill in fullstack):   
       msg = 'He is a fullstack developer'
    print(msg)  
else:
    print("No skills found")    

if((person["is_married"] == True) and (person["country"] == "Finland")):
    
    print("%s %s lives in %s and is Married" % (person["first_name"], person["last_name"], person["country"]))