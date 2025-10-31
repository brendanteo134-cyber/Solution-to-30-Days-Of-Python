#30 DAYS OF PYTHON DAY 6 - TUPLES
#Exercises: Level 1
tuple_1 = ()
print (tuple_1)
tuple_2 = ("James", "John", "Nolan")
print (tuple_2)
tuple_3 = ("Christina",)
print (tuple_3)
siblings = tuple_2 + tuple_3
print (siblings)
print(len(siblings))

siblings += ('Benjamin',)
siblings += ('Jenny',)
family_members = siblings
print (family_members)

siblings, parents = family_members[:4], family_members[4:]
print(siblings)
print(parents)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'curd')
food_stuff = fruits + vegetables + animal_products
print(food_stuff)

if len(food_stuff) % 2 == 0:
    print(food_stuff[(len(food_stuff)//2)-1])
    print(food_stuff[len(food_stuff)//2])
else:
    print(food_stuff[len(food_stuff)//2])

newtp = food_stuff[:3] + food_stuff[-3:]
print(newtp)

del food_stuff

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print("Estonia is a nordic country")
else:
    print("Estonia is not a nordic country")
if 'Iceland' in nordic_countries:
    print("Iceland is a nordic country")
else:
    print("Iceland is not a nordic country")