from utilities import *

data = GetData(2022, 2)

def cleandata():
    cleandata = []
    for i in data:
        cleandata.append(i.split(" "))
    return cleandata

def part1():
    results = cleandata()
    plays = ['X','Y','Z']
    score = 0
    for i in results:
        if i[1] == plays[0]:
            score += 1
            if i[0] == 'A':
                score += 3
            elif i[0] == 'C':
                score += 6

        elif i[1] == plays[1]:
            score += 2
            if i[0] == 'B':
                score += 3
            elif i[0] == 'A':
                score += 6

        elif i[1] == plays[2]:
            score += 3
            if i[0] == 'C':
                score += 3
            if i[0] == 'B':
                score += 6
    
    return score

def part2():
    results = cleandata()
    outcomes = ['X','Y','Z']
    score = 0
    rock = 1
    paper = 2
    scissors = 3
    loss = [['A', scissors], ['B', rock], ['C', paper]]
    draw = [['A', rock + 3], ['B', paper + 3], ['C', scissors + 3]]
    win = [['A', paper + 6], ['B', scissors + 6], ['C', rock + 6]]

    for i in results:
        if i[1] == outcomes[0]:
           for choice in loss:
              if i[0] == choice[0]:
                  score += choice[1]

        elif i[1] == outcomes[1]:
           for choice in draw:
              if i[0] == choice[0]:
                  score += choice[1]
    
        elif i[1] == outcomes[2]:
           for choice in win:
              if i[0] == choice[0]:
                  score += choice[1]

    return score

print(part2())