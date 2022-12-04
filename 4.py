from utilities import *

data = GetData(2022, 4)

def cleandata():
    cleandata = []
    cleandata2 = []
    for i in data:
        cleandata.append(i.split(','))
    for i in cleandata:
        for item in i:
            cleandata2.append(item.split('-'))

    return cleandata2

def half1():
    data = cleandata()
    index = 0
    duplicates = 0
    while index < len(data):
        str1 = int(data[index][0]) - int(data[index+1][0])
        str2 = int(data[index][1]) - int(data[index+1][1])
        index += 2
    
        dupebool = False
        if str1 == 0 or str2 == 0:
            dupebool = True
        elif str1 > 0:
            if str2 > 0:
                dupebool = False
            elif str2 < 0:
                dupebool = True
        elif str1 < 0:
            if str2 > 0:
                dupebool = True
            elif str2 < 0:
                dupebool = False

        if dupebool == True:
              duplicates += 1
    
    print(duplicates)
        
def half2():
    data = cleandata()
    index = 0
    duplicates = 0
    while index < len(data):
        str1 = int(data[index][0]) - int(data[index+1][1])
        str2 = int(data[index][1]) - int(data[index+1][0])
        dupebool = False
        if str1 == 0 or str2 == 0:
            dupebool = True
        elif str1 > 0 and str2 < 0 or str1 < 0 and str2 > 0:
            dupebool = True

        if dupebool == True:
            duplicates += 1
        index += 2
    print(duplicates)

half1()
half2()