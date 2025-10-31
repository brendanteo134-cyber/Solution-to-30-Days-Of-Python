#Exercises

a = 'Thirty'
b = 'Days'
c = 'of'
d = 'Python'
e = ' '
str_1 = a + e + b + e + c + e + d
print(str_1)

f = 'Coding'
g = 'For'
h = 'All'
str_2 = f + e + g + e + h
print (str_2)

Company = str_2
print (Company)
print (len(Company))

print(str.upper(Company))
print(str.lower(Company))
print(str.capitalize(Company))
print(str.title(Company))
print(str.swapcase(Company))
print((Company) [0:6])
print(str.find(Company, 'Coding'))

challenge = 'Python for Everyone'
print(challenge.replace('Everyone', 'ALL'))

print(challenge.split())

Companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(Companies.split(" , "))

str_3 = "Coding For ALL"
print(str_3.index(0))

print(str_3[0])
print(str_3[-1])
print(str_3[10])

new_acr = "PFE"
new2_acr = "CFA"

print(str_3.index("C"))
print(str_3.index("F"))

print("Coding For All People".rfind("I"))

print("You cannot end a sentence with because because because is a conjunction".find('because'))

print(
    "You cannot end a sentence with because because because is a conjunction"[31:54])

print("You cannot end a sentence with because because because is a conjunction".find("because"))

print(
    "You cannot end a sentence with because because because is a conjunction"[31:54])

print("Coding For All".startswith("Coding"))

print("Coding For All".endswith("coding"))

print('   Coding For All      '.strip())

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

lst = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(lst))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\nAsabeneh\t250\tFinland")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a cricle with radius {radius} is {area} meters square.")

print(f"8 + 6 = {8+6}\n8 - 6 = {8-6}\n8 * 6 = {8*6}\n8 / 6 = {8/6:.2f}\n8 % 6 = {8%6}\n8 // 6 = {8//6}\n8 ** 6 = {8**6}")