from aocd.models import Puzzle

#Credits aan Matthijs de Heus
def GetData(year, day):
    puzzle = Puzzle(day=day, year=year)
    return [line for line in puzzle.input_data.split("\n")]