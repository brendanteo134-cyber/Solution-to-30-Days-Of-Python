#Day 11 (FUNCTIONS)
import keyword
def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(2,3))

import math

def area_of_circle (num3):
    area = math.pi * num3 * num3
    return area
print(area_of_circle(6))

def add_all_nums(arr):
    sum_of_nums = 0
    for i in arr:
        try:
            int(i)
            sum += i
        except:
            return "Only Integers are allowed"
    return sum



def convert_celsius_to_fahrenheit(num6):
    temperature_in_fahrenheit = (num6*1.8) + 32

print(convert_celsius_to_fahrenheit(0))

def check_season(month):
    if month in ["September", "October", "November"]:
        print("Autumn")
    if month in ["December", "January", "February"]:
        print("Winter")
    if month in ["March", "April", "May"]:
        print("Spring")
    else:
        print("Summer")

def calculate_slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    D = b * b - 4 * a * c
    X1 = (-b + D) / (2 * a)
    X2 = (-b - D) / (2 * a)
    print(X1, X2)

def print_list(lst):
    for i in lst:
        print(i)
print_list([1, 2, 6, 8, 3])

def reverse_list(a):
    new_lst = []
    for i in range(-1, -(len(a))-1, -1):
        new_lst.append(a[i])
    return new_lst


print(reverse_list([1, 2, 3, 4]))

def capital_list_terms(a):
    for i in a:
        a[a.index(i)] = i.capitalize()
    return a

def add_item(mutable, tba):
    mutable.append(tba)
    return mutable

def remove_item(mutable, tbr):
    mutable.remove(tbr)
    return mutable

def sum_of_numbers(high):
    sum_of_numbers = 0
    for i in range(high + 1):
        sum_of_numbers += i
    return sum_of_numbers

def sum_of_odds(high):
    sum_of_odd_nums = 0
    for i in range(high + 1):
        if i % 2 == 1:
            sum_of_odd_nums += i
    return sum_of_odd_nums

def sum_of_even(high):
    sum_of_even_nums = 0
    for i in range(high + 1):
        if i % 2 == 0:
            sum_of_even_nums += i
    return sum_of_even_nums

def evens_and_odds(high):
    odds = 0
    evens = 0
    for i in range(high + 1):
        if i % 2 == 0:
            evens += i
        else:
            odds += i
    print(odds, evens)

def factorial(fac):
    fact = 1
    for i in range(fac + 1):
        fact *= i
    return fact

def is_empty(check):
    if check:
        return True
    else:
        return False

def mean(dataset):
    return sum(dataset) / len(dataset)

def median(dataset):
    data = sorted(dataset)
    index = len(data) // 2

    if len(dataset) % 2 != 0:
        return data[index]

    return (data[index - 1] + data[index]) / 2

def mode(dataset):
    frequency = {}

    for value in dataset:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, value in frequency.items() if value == most_frequent]

    return modes

def variance(dataset):
    n = len(dataset)
    mean = sum(dataset) / n
    deviations = [(x - mean) ** 2 for x in dataset]
    variance = sum(deviations) / n
    return variance

def stdev(dataset):
    var = variance(dataset)
    std_dev = var ** 0.5
    return std_dev

def is_prime(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True

def checK_list(test_list):
    return len(set(test_list)) == len(test_list)

def homogeneous_type(seq):
    iseq = iter(seq)
    first_type = type(next(iseq))
    return first_type if all((type(x) is first_type) for x in iseq) else False

test = "potatoes"
def isVar(test):
    if not isinstance(test, str):
        return False  

    if not test.isidentifier():
        return False  

    if keyword.iskeyword(test):
        return False  

    return True

"""countries_data = ["United States", "United Kingdom", "Korea"]
list_data = countries_data
total_languages_initial = []
for i in list_data:
    total_languages_initial.extend(i["languages"])
print("Languages = ", len(set(total_languages_initial)))
counts = {}
for i in total_languages_initial:
    counts[i] = counts.get(i, 0) + 1

def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))

counts = sort_dict_by_value(counts, True)
for i in list(counts.items())[:20]:
    print(i)
populations = {}
for i in list_data:
    populations[i["name"]] = i["population"]
populations = sort_dict_by_value(populations, True)
for i in list(populations.items())[:20]:
    print(i)"""