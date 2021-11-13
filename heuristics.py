from functools import lru_cache
from typing import DefaultDict
import pycosat
import sys, getopt
import time
from collections import defaultdict


def DLCS(lst, value_dict):
    literal_count = defaultdict(int)
    for clause in lst:
        for number in clause:
            literal_count[abs(number)] += 1
    max_key = max(literal_count, key=literal_count.get)
    
    counter_t = 0
    counter_n = 0

    for clause in lst:
        for number in clause:
            if number == max_key:
                counter_t += 1
            elif number == -max_key:
                counter_n += 1
    
    if counter_t > counter_n:
        value_dict[str(max_key)] = 1
    else:
        value_dict[str(max_key)] = 0




def DLIS(lst, value_dict, key_max = True):
    # 2 dictionaries => one for positive and one for negative literals
    pos_literal_count = defaultdict(int)
    neg_literal_count = defaultdict(int)
    for clause in lst:
        for number in clause:
            if number > 0:
                pos_literal_count[number] += 1
            else:
                neg_literal_count[number] += 1
    
    # pick two max values => one for positive and one for negative literals
    max_key = max(pos_literal_count, key=pos_literal_count.get)
    min_key = max(neg_literal_count, key=neg_literal_count.get)

    # if you want to have largest positive literal
    if key_max == True:
        counter_t = 0
        counter_n = 0

        for clause in lst:
            for number in clause:
                if number == max_key:
                    counter_t += 1
                elif number == -max_key:
                    counter_n += 1
        # if more pos versions of literal than neg assign T else F
        if counter_t > counter_n:
            value_dict[str(max_key)] = 1
        else:
            value_dict[str(max_key)] = 0

    # if higest amount of neg literals should be chosen
    else:
        counter_t = 0
        counter_n = 0

        for clause in lst:
            for number in clause:
                if number == min_key:
                    counter_n += 1
                elif number == -min_key:
                    counter_t += 1
        # if more pos versions of literal than neg assign T else F
        if counter_t > counter_n:
            value_dict[str(max_key)] = 1
        else:
            value_dict[str(max_key)] = 0
    return value_dict
        



l2 = [[111,333,111,-113,-114], [222,222,222,222,222,222,333,444,113, -333, -333, -333]]
d = {}

DLIS(l2, d)