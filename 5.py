from utilities import *

data = GetData(2022, 5)

def cleandata():
    crates = []
    for row in range(8):
        crates.append(data[row])
    crates.reverse()

    cratecoords = []
    for row in crates:
        index = 0
        newlist = []
        for letter in row:
            if letter.isalpha() == True:
                newlist.append([letter, index])
            index += 1
        cratecoords.append(newlist)

    horizontal = [[1,[]], [5,[]], [9,[]], [13,[]], [17,[]], [21,[]], [25,[]], [29,[]], [33,[]]]
    for number in horizontal:
        for row in cratecoords:
            for item in row:
                if item[1] == number[0]:
                    number[1].append(item[0])
    cratedict = {}
    for i in range(9):
        cratedict.update({str(i + 1) : horizontal[i][1]})
    return cratedict
                    
def getinstructions():
    instructions = []
    for row in range(10, len(data)):
        instructions.append(data[row].split())
    
    for list in instructions:
        index = 0
        for item in list:
            if item.isalpha() == True:
                list.pop(index)
            index += 1

    return instructions
    
def half(chosenhalf):
    crates = cleandata()
    arrangement = getinstructions()
    for row in arrangement:
        if chosenhalf == 1:
            for i in range(int(row[0])):
                crates[row[2]].append(crates[row[1]][-1])
                crates[row[1]].pop()
        
        elif chosenhalf == 2:
            for i in reversed(range(int(row[0]))):
               crates[row[2]].append(crates[row[1]][-(i+1)])
            for i in reversed(range(int(row[0]))):
               crates[row[1]].pop()
            
    outputstring = ''
    for i in crates:
        outputstring += crates[i][-1]
    print(f"half {chosenhalf}: " + outputstring)

half(1)
half(2)