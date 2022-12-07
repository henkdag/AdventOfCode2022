from collections import defaultdict
from itertools import accumulate
from utilities import *

dirdict = defaultdict(int)

data = GetData(2022, 7)

for line in data:
    match line.split():
        case '$', 'cd', '/': directory = ['']
        case '$', 'cd', '..': directory.pop()
        case '$', 'cd', dirname: directory.append(dirname + '/')
        case '$', 'ls': pass
        case 'dir', _: pass
        case size, _:
            for fsize in accumulate(directory):
                dirdict[fsize] += int(size)

print(sum(s for s in dirdict.values() if s <= 100_000),
      min(s for s in dirdict.values() if s >= dirdict[''] - 40_000_000))
