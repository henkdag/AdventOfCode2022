from utilities import *

data = GetData(2022, 1)

def cleandata():
    #Clean list to list per elf
    splitlist = []
    cleandata = []
    
    for item in data:
        if item != '':
            splitlist.append(int(item))
        else:
            cleandata.append(splitlist)
            splitlist = []
    
    return cleandata

def biggestsum(cleandata):
    #Find biggest sum with index
    biggestsum = 0
    index = 0
    for item in cleandata:
        sum1 = sum(item)
        #If current biggest lower than next list item, replace and save index
        if biggestsum < sum1:
            biggestsum = sum1
            bigindex = index
        index += 1
    
    return [biggestsum, bigindex]

def returntop(length):
    #Return specified top ranking
    toplist = []
    data = cleandata()
    for i in range(length):
        #Add highest sum to new list, delete from main list
        sumdata = biggestsum(data)
        toplist.append(sumdata[0])
        data.pop(sumdata[1])
    
    return toplist

print(sum(returntop(3)))