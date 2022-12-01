from utilities import *

data = GetData(2022, 1)

def cleandata():
    #Clean list to list per elf
    splitlist = []
    organiseddata = []
    sumdata = []
    
    for item in data:
        if item != '':
            splitlist.append(int(item))
        else:
            organiseddata.append(splitlist)
            splitlist = []
    
    for item in organiseddata:
        sumdata.append(sum(item))

    sumdata.sort(reverse=True)
    return sumdata

def returntop(length):
    #Return specified top ranking
    toplist = []
    data = cleandata()
    for i in range(length):
        #Add highest sum to new list
        toplist.append(data[i])
    
    return toplist

print(sum(returntop(3)))