import sys, getopt
import numpy as np
import copy
import time
import math
from collections import defaultdict
sys.setrecursionlimit(10000)
#sudokus = "4x4.txt"  # argument in line
#sudokus = "16x16.txt"
sudokus = "1000_sudokus.txt"
rules_d={
    4:"sudoku-rules-4x4.txt",
    9:"9x9_sudoku-rules.txt",
    16:"sudoku-rules-16x16.txt"
}

def set_dim(val):
    global DIM
    DIM=val

#first unassigned available
def select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal

def DLCS(lst):
    clauses = copy.deepcopy(lst)
    literal_count = defaultdict(int)
    literal_count2 = defaultdict(int)
    for clause in clauses:
        for number in clause:
            literal_count[abs(number)] += 1
            literal_count2[number] += 1
    max_key = max(literal_count, key=literal_count.get)

    if max_key and -max_key in literal_count2:
        if literal_count2[max_key] > literal_count2[-max_key]:
            return max_key
        else:
            return -max_key
    else:
        return max_key

# we can choose if we take the highest positive or negative value => can decide with True
def DLIS(lst, key_max=True):
    clauses = copy.deepcopy(lst)
    pos_literal_count = defaultdict(int)
    neg_literal_count = defaultdict(int)
    for clause in clauses:
        for number in clause:
            if number > 0:
                pos_literal_count[number] += 1
            else:
                neg_literal_count[number] += 1

    # pick two max values => one for positive and one for negative literals
    max_key = max(pos_literal_count, key=pos_literal_count.get)
    min_key = max(neg_literal_count, key=neg_literal_count.get)

    if key_max == True:
        if max_key in pos_literal_count and -max_key in neg_literal_count:
            if pos_literal_count[max_key] > neg_literal_count[-max_key]:
                return max_key
            else:
                return -max_key
        else:
            return max_key

    else:
        if min_key in neg_literal_count and -min_key in pos_literal_count:
            if neg_literal_count[min_key] > pos_literal_count[-min_key]:
                return min_key
            else:
                return -min_key
        else:
            return min_key


#2,3 to be added
heuristics={
    1:select_literal,
    2:DLIS,
    3:DLCS
}

# returns DIMACS representation of the given input - initial configuration
# file as argument on run
def read_game():
    #f = open(file, "r") received arg later
    f = open(sudokus, "r")
    game_rep = f.readline()
    set_dim(int(math.sqrt(len(game_rep)-1)))
    if DIM==16:
        return read_game16(game_rep)
    else:
        game_final = ""
        for i in range(len(game_rep) - 1):
            if game_rep[i] != ".":
                l = int(i / DIM) + 1
                c = i % DIM + 1
                game_final = game_final + str(l) + str(c) + game_rep[i] + " 0\n"
        return game_final


def read_game16(line):
    game_final=""
    for i in range(len(line) - 1):
        if line[i] != ".":
            l = int(i / DIM) + 1
            c = i % DIM + 1
            if line[i] in ["A", "B", "C", "D", "E", "F", "G"]:
                if line[i]=="G":
                    val=16
                else:
                    val=int(line[i], 16)
            else:
                val=int(line[i])
            char_rep=str(l*289+c*17+val)
            game_final=game_final+char_rep+" 0\n"
    return game_final

# hardcoded
def read_rules():
    with open(rules_d[DIM], 'r') as f:
        delete = f.readline()
        rls = f.read()
    return rls

def parse_game(arg):
    arg = arg.split("\n")
    list_rep = []
    for i in range(len(arg) - 1):
        list_rep.append(int(arg[i].split()[0]))
    return list_rep

def parse_rules(arg):
    arg = arg.split("\n")
    list_rep = []
    for i in range(len(arg)):
        arg[i] = arg[i].split()
        curent_list = []
        for j in range(len(arg[i]) - 1):
            curent_list.append(int(arg[i][j]))
        list_rep.append(curent_list)
    return list_rep

def show(solution):
    if len(solution)>1000:
        show_16(solution)
    else:
        solved = np.zeros((DIM, DIM), dtype=int)
        for num in solution:
            if num>0:
                lin = int(str(num)[0]) - 1
                col = int(str(num)[1]) - 1
                val = int(str(num)[2])
                solved[lin][col] = val
        print(solved)

def show_16(solution):
    solved = np.zeros((DIM, DIM), dtype=int)
    letters=["A", "B", "C", "D", "E", "F", "G"]
    for num in solution:
        if num > 0:
            lin = int(num/289) - 1
            col = int((num-289*lin)/17) - 1
            val=num-289*lin-17*col
            solved[lin][col] = val
    for i in range(DIM):
        for j in range(DIM):
            if solved[i][j]>9:
                print(letters[solved[i][j]-10]+" ")
            else:
                print(solved[i][j]+" ")
        print("\n")

def simplify(clauses, lit):
    simplified=copy.deepcopy(clauses)
    for clause in reversed(simplified):
        for num in reversed(clause):
            if num==lit:
                simplified.remove(clause)
                break
            elif num==-lit:
                clause.remove(num)
                if len(clause) == 0:
                    return 0
    if len(simplified) == 0:
        return 1
    return simplified

def unit(clauses):
    for clause in clauses:
        if len(clause)==1:
            return clause[0]
    return 0

def rec(clauses, lit, sol):
    new_sol = copy.deepcopy(sol)
    new_sol.append(lit)
    new_clauses = simplify(clauses, lit)
    if new_clauses == 0:
        return 0
    elif new_clauses == 1:
        print("Sol found!")
        show(new_sol)
        return 1

    #unit rule
    unit_clause=unit(new_clauses)
    if unit_clause!=0:
        new_lit=unit_clause
    else:
        new_lit = heuristics[h](new_clauses)

    if rec(new_clauses, -new_lit, new_sol):
        return True
    return rec(new_clauses, new_lit, new_sol)


if __name__ == '__main__':
    # unused
    global h
    h=2
    #h=int(sys.argv[1]) #set heuristc choice
    #input_file=sys.argv[2] #argument for read_game()
    #
    sudoku = read_game()  # input file as arg later
    sudoku = parse_game(sudoku)  # int
    rules = read_rules()  # DIMACS format
    rules = parse_rules(rules)  # int

    start_time = time.time()
    for field in sudoku:
        rules=simplify(rules,field)
    first_lit=heuristics[h](rules)
    if not rec(rules, first_lit, sudoku):
        rec(rules, -first_lit, sudoku)

    running_time=time.time() - start_time
    print(running_time)