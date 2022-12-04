from string import ascii_lowercase, ascii_uppercase
from utilities import *

data = GetData(2022, 3)

def scoregen():
    alphabetscore = {}
    score = 1
    for i in ascii_lowercase:
        alphabetscore.update({i : score})
        score += 1
    for i in ascii_uppercase:
        alphabetscore.update({i : score})
        score += 1
    return alphabetscore

def half1():
    alphabetscore = scoregen()
    priority = 0

    for i in data:
        half1 = []
        half2 = []
        index = 0
        duplicate = ""

        for letter in i:
            if index < (len(i) / 2):
                half1.append(letter)
            else:
                half2.append(letter)
            index += 1

        half1.sort()
        half2.sort()

        for letter in half1:
            if letter in half2:
                duplicate = letter
                break
        priority += alphabetscore[duplicate]
        
    print(priority)

def half2():
    alphabetscore = scoregen()
    index = 0
    priority = 0
    dividedlist = []

    while index < len(data):
        dividedlist.append([data[index], data[index+1], data[index+2]])
        index += 3
    for i in dividedlist:
        for letter in i[0]:
            if letter in i[1] and letter in i[2]:
                duplicate = letter
                break
        priority += alphabetscore[duplicate]
    print(priority)

half1()
half2()