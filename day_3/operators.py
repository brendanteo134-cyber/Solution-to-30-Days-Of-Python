import math
age = 19
height = 183.0
complex_number = 10 + 6j

"""
# Taking integer input
age_str = input("Enter your age: ")
age_int = int(age_str)
print("Your age is:", age_int)

# Taking float input
height_str = input("Enter your height in meters: ")
height_float = float(height_str)
print("Your height is:", height_float)

"""

base = float(input("Enter base: "))
height_1 = float(input("Enter height: "))
Area = base * height_1 * 0.5
print ("The Area of the triangle is " +  str(Area) + " metre squared.")

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))

Perimeter = side_a + side_b + side_c
print ("The perimeter of this triangle is " + str(Perimeter) + " metres.")

length_rect = float(input("Enter lenght: "))
width_rect = float(input("Enter width: "))
Area_rect = length_rect * width_rect
Peri_rect = (length_rect + width_rect) *2
print ("The Area of the rectangle is " +  str(Area_rect) + " metre squared.")
print ("The perimeter of this rectangle is " + str(Peri_rect) + " metres.")

r = float(input("Enter radius: "))
Area_cirle = 3.14 * r * r
Circum_circle = 3.14 * 2 * r

Rounded_Area_circle = int(Area_cirle)
Rounded_Circum_circle = int(Circum_circle)
print ("The Area of the circle is " +  str(Rounded_Area_circle) + " metre squared.")
print ("The circumference of this Circle is " + str(Rounded_Circum_circle) + " metres.")

x_intercept = -(-2)/2
y_intercept = -2
slope = 2
print(f"x_intercept: {x_intercept}")
print(f"y_intercept: {y_intercept}")
print(f"slope: {slope}")

m = (10-2)/(6-2)
print(f"Slope between point (2, 2) and point (6,10) is: {m}")

if slope > m:
    print("Slope of Task 8 is greater")
else:
    print("Slope of Task 9 is greater")

for x in [-4, -3, -2, -1, 0, 1, 2, 3, 4]:
    y = x**2 + 6*x + 9
    if y == 0:
        print(f"y is zero when x is : {x}")
        break

print(not (len("python") or len("jargon")))

if "on" in "python" and "on" in "jargon":
    print("present in both")

if "jargon" in "I hope this course is not full of jargon":
    print("jargon is present in the sentence")

if not ("on" in "dragon" or "on" in "python"):
    print("There is no 'on' in both dragon and python")

length = len("python")
fltval = float(length)
strval = str(fltval)

n = int(input("Enter a number"))
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")

if 7//3 == int(2.7):
    print("The floor division of 7 by 3 is equal to the int converted value of 2.7")

if type('10') == type(10):
    print("Equal types")
else:
    print("Not equal types")

if int(9.8) == 10:
    print("equal")
else:
    print("not equal")

hrs = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print(f"You are earning is {hrs*rate} weekly")

yrs = int(input("Enter number of years you have lived: "))
print(f"You have lived for {yrs*31536000} seconds")

print("Pattern \n")
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1:
            print("1 ", end=' ')
        else:
            if j == 1:
                print(f"{i} ", end=' ')
            elif j == 2:
                print("1 ", end=' ')
            else:
                print(f"{i**(j-2)} ", end=' ')
    print("\n", end='')