from functools import lru_cache
from typing import DefaultDict
from collections import defaultdict


### one-sided jeroslow wang
def jw_os(lst, value_dict):
    literal_count = defaultdict(int)
    for clause in lst:
        for number in clause:
            literal_count[number] += (2**-len(clause))
    max_key = max(literal_count, key=literal_count.get)
    if max_key> 0:
        value_dict[str(max_key)] = 1
    else:
        value_dict[str(-max_key)] = 0 
    return value_dict

# two-sided jeroslow wang
def jw_ts(lst, value_dict):
    literal_count = defaultdict(int)
    for clause in lst:
        for number in clause:
            literal_count[number] += (2**-len(clause))
    
    abslist = [abs(x) for x in literal_count]
    absdict = dict.fromkeys(abslist, 0)

    for i in literal_count:
        absdict[abs(i)] += literal_count[i]

    max_key = max(absdict, key=absdict.get)

    if literal_count[max_key] >= literal_count[-1*max_key]:
        value_dict[str(max_key)] = 1
    else:
        value_dict[str(max_key)] = 0
    return value_dict

l2 = [[111,333,111,-113,-114], [222,222,222,222,222,222,333,444,113, -333, -333, -333]]
d = {}

print(jw_ts(l2, d))