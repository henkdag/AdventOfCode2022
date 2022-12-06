from utilities import *

data = GetData(2022, 6)
data = data[0]

def half(length):
    index = 0
    while index < len(data) - length:
        substring = data[index:index+length]
        record = []
        for letter in substring:
            if substring.count(letter) > 1:
                record.append(False)
                break
            else:
                record.append(True)

        if False not in record:
            print(index + length)
            break
        index+=1

half(4)
half(14)