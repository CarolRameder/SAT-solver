import sys
import numpy as np
import copy
import time
import math
from collections import defaultdict
sys.setrecursionlimit(10000)
sudokus = "4x4.txt"  # argument in line
#sudokus = "16x16.txt"
#sudokus = "1000_sudokus.txt"
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
    literal_count = defaultdict(int)
    literal_count2 = defaultdict(int)
    for clause in lst:
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

    if key_max:
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

# jeroslow wang one-sided
def JWOS(lst):
    literal_count = defaultdict(int)
    #rint(literal_count)
    for clause in lst:
        for lit in clause:
            literal_count[lit] += (2**-len(clause))
    max_key = max(literal_count, key=literal_count.get) #returns value
    return max_key

# jeroslow wang two-sided
def JWTS(lst):
    literal_count = defaultdict(int)
    for clause in lst:
        for lit in clause:
            literal_count[lit] += (2**-len(clause))
    
    abslist = [abs(x) for x in literal_count]
    absdict = dict.fromkeys(abslist, 0)

    for i in literal_count:
        absdict[abs(i)] += literal_count[i]

    max_key = max(absdict, key=absdict.get)

    if literal_count[max_key] >= literal_count[-1*max_key]:
        return max_key
    else:
        return -max_key

#1,2 and 4
heuristics={
    1:select_literal,
    2:DLIS,
    3:DLCS,
    4:JWOS,
    5:JWTS
}

# returns DIMACS representation of the given input - initial configuration
# file as argument on run
def read_game(game_rep):

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
    global total_units, total_bkt
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
        total_units+=1
    else:
        new_lit = heuristics[h](new_clauses)
        total_bkt+=1
    if rec(new_clauses, -new_lit, new_sol):
        return True
    return rec(new_clauses, new_lit, new_sol)


if __name__ == '__main__':
    # unused
    global h,total_bkt,total_units
    h=4
    #h=int(sys.argv[1]) #set heuristc choice
    #input_file=sys.argv[2] #argument for read_game()
    #
    f = open(sudokus, "r")
    game_reps = f.readlines()
    set_dim(int(math.sqrt(len(game_reps[0]) - 1)))
    rules = read_rules()  # DIMACS format
    rules = parse_rules(rules)  # int
    duration=[[],[]]
    bkts = [[], []]
    units = [[], []]
    for game_rep in game_reps[:20]:
        sudoku = read_game(game_rep)  # input file as arg later
        sudoku = parse_game(sudoku)  # int
        if DIM==9:#continue for others?
            if 21<=len(sudoku)<=24:
                gr=0
            elif 26<=len(sudoku)<=29:
                gr=1
            else:
                continue
        elif DIM==4:
            if len(sudoku)==4:
                gr=0
            elif len(sudoku)==6:
                gr=1
            else:
                continue
        print(sudoku)
        start_time = time.time()
        c_rules=copy.deepcopy(rules)
        for field in sudoku:
            c_rules=simplify(c_rules,field)
        total_units=0
        total_bkt=0
        first_lit=heuristics[h](c_rules)
        if not rec(c_rules, first_lit, sudoku):
            rec(c_rules, -first_lit, sudoku)

        running_time=time.time() - start_time
        duration[gr].append(running_time)
        bkts[gr].append(total_bkt)
        units[gr].append(total_units)
    print("Duration")
    print("gr2")
    print(sum(duration[1])/len(duration[1]), np.std(duration[1]))
    print("gr1")
    print(sum(duration[0]) / len(duration[0]), np.std(duration[0]))
    print("Backtracks")
    print("gr2")
    print(sum(bkts[1]) / len(bkts[1]), np.std(bkts[1]))
    print("gr1")
    print(sum(bkts[0]) / len(bkts[0]), np.std(bkts[0]))
    print("Unit rule calls")
    print("gr2")
    print(sum(units[1]) / len(units[1]), np.std(units[1]))
    print("gr1")
    print(sum(units[0]) / len(units[0]), np.std(units[0]))