from functools import lru_cache
from typing import DefaultDict
import sys, getopt
import time
from collections import defaultdict
import math
import random
import copy

# to do => look at representation of values => dictionary ?

def read_soduko(in_file):
    f = open(in_file, "r") 
    sudokus = []
    format_sudokus = []
    for line in f:
        sudokus.append(line.split())

    for sud in sudokus:
        s = []
        for element in sud:
            counter_rows = 1
            counter_columns = 0
            for number in element:
                counter_columns += 1
                if number.isnumeric():
                    s.append(int(str(counter_rows) + str(counter_columns) + str(number)))
                
                if counter_columns == math.sqrt(len(element)):
                    counter_rows += 1
                    counter_columns = 0

        format_sudokus.append(s) 
    f.close()   
    return format_sudokus


def prepare_set(rules_file, input_file):
    f = open(rules_file, "r")
    s = open(input_file, "r")
    cnf = []
    sudoku = []

    with open(rules_file, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            cnf.append(list(map(lambda x: int(x), line.split()[:-1])))
   
    for line in s:
        sudoku.append(line.split()[0])

    s.close()
    return cnf, sudoku





# tautology

def tautology(clause_list):
    for clause in reversed(clause_list):
        taut = False
        for number in clause:
            if -number in clause:
                taut  = True    
        if taut == True:
            clause_list.remove(clause)
          
    return clause_list


# not in use atm

def pure_literal(clause_list, value_dict): 
    literal_count = defaultdict(int)
    for clause in clause_list:
        for number in clause:
            literal_count[number] += 1
        
    for key in literal_count.keys():
        if key and not -key in literal_count.keys():
            if key > 0:
                value_dict[str(key)] = 1
            elif key < 0:
                value_dict[str(key)] = 0

# not in use atm

def unit_clauses(clause_list, value_dict):
    for clause in clause_list:
        if len(clause) == 1:
            if clause[0] > 0:
                value_dict[str(clause[0])] = 1
            elif clause[0] < 0:
                value_dict[str(clause[0])[1:]] = 0
    return clause_list

# remove clauses

def rem_clauses(clause_list, literal):
    for clause in reversed(clause_list):
        for number in clause:
            if number == literal:
                clause_list.remove(clause)
    return clause_list


# remove literal

def rem_lit(clause_list, literal):
    for clause in clause_list:
        for number in reversed(clause):
            if number == literal:
                clause.remove(number)
    return clause_list



# pick random variable

def random_variable(clause_list): 
        rand_clause = random.randint(0, len(clause_list)-1)
        rand_lit = random.randint(0, len(clause_list[rand_clause])-1)

        return clause_list[rand_clause][rand_lit]



# call dpll
index = 0
def dpll(clause_list, literal):
    global values
    global index
    print(f"Index: {index}")
    index += 1

    rem_clauses(clause_list, literal)
    rem_lit(clause_list, -literal)

    if len(clause_list) == 0:
        values.append(literal)
        return True
    
    for clause in clause_list:
        if len(clause) == 0:
            return False

    literal = random_variable(clause_list)
    if dpll(copy.deepcopy(clause_list), -literal):
        values.append(-literal)
        return True
    
    values.append(literal)
    return dpll(copy.deepcopy(clause_list), literal)



sud_1000 = read_soduko("1000_sudokus.txt")
sud_4 = read_soduko("4x4.txt")
try_sud_4 = sud_4[0]
sud_9 = read_soduko("sudoku-example.txt")
value_dict = {}

rules_file, input_file = prepare_set("sudoku-rules-4x4.txt", "sudoku-example.txt")

var = random_variable(rules_file)
values = []
dpll(rules_file, var)

print(sorted(values))
len(values)

# remove clauses

for lit in try_sud_4:
    rem_clauses(rules_file, lit)


# remove literal

for lit in try_sud_4:
    rem_lit(rules_file, -lit)



def main(rules, input):
    #tautology (rules)

    for element in input:
        rem_clauses(rules, element)

    
    for element in input:
        rem_lit(rules, -element)

    var = random_variable(rules)

    values= []
    return dpll(rules, var), values

main(rules_file, try_sud_4)