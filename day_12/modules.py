#Day 12 of 30 Days of Python (Modules)

import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
char_list = []
char_list[:0] = chars

def random_user_id ():
    identity = ""
    for _ in range (6):
        identity += random.choice(char_list)
        return identity

def random_user_id():
    identity = ''
    for _ in range(6):
        identity += random.choice(char_list)
    return identity


def user_id_gen_by_user():
    charsize = int(input('Enter Character Size: '))
    charlimit = int(input('Enter how many user ids to generate: '))
    for _ in range(charlimit):
        identity = ''.join([random.choice(char_list) for _ in range(charsize)])
        print(identity)


def rgb_color_gen():
    r = str(random.randint(0, 255))
    g = str(random.randint(0, 255))
    b = str(random.randint(0, 255))
    return "rgb(" + r + "," + g + "," + b + ")"

def list_of_hexa_colors(many=0):
    if many == 0:
        many = random.randint(1, 10)
    hexas = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f".split(",")
    hexCodes = []
    for _ in range(many):
        hexCodes.append("#" + ''.join([random.choice(hexas) for _ in range(6)]))
    return hexCodes


def list_of_rgb_colors(many=0):
    if many == 0:
        many = random.randint(1, 10)
    rgbs = []
    for _ in range(many):
        rgbs.append(rgb_color_gen())
    return rgbs


def generate_colors(type_of_col, many):
    if type_of_col == 'hexa':
        return list_of_hexa_colors(many)
    elif type_of_col == 'rgb':
        return list_of_rgb_colors(many)
    else:
        return "Invalid Input"
    
    def shuffled_list(array):
        return random.sample(array, len(array))


def seven_random():
    arr = []
    length = -1
    while length <= 7:
        num = random.randint(0, 9)
        if num not in arr:
            arr.append(num)
            length = len(arr)
    return arr