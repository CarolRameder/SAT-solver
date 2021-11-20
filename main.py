import time
import sys, getopt
import numpy as np
import copy
import time

#sudokus = "4x4.txt"  # argument in line
sudokus = "1000_sudokus.txt"
#rules = "sudoku-rules-4x4.txt"  # hardcode read
rules= "9x9_sudoku-rules.txt"


def set_dim(val):
    global DIM
    DIM=val

#first unassigned available
def select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal

heuristics={
    1:select_literal
}

# returns DIMACS representation of the given input - initial configuration
# file as argument on run
def read_game():
    #f = open(file, "r") received arg later
    f = open(sudokus, "r")
    game_rep = f.readline()
    game_final = ""
    for i in range(len(game_rep) - 1):
        if game_rep[i] != ".":
            l = int(i / DIM) + 1
            c = i % DIM + 1
            game_final = game_final + str(l) + str(c) + game_rep[i] + " 0\n"
    return game_final

# hardcoded
def read_rules():
    with open(rules, 'r') as f:
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
    solved = np.zeros((DIM, DIM), dtype=int)
    for num in solution:
        if num>0:
            lin = int(str(num)[0]) - 1
            col = int(str(num)[1]) - 1
            val = int(str(num)[2])
            solved[lin][col] = val
    print(solved)

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
    h=1
    #h=int(sys.argv[1]) #set heuristc choice
    #input_file=sys.argv[2] #argument for read_game()
    #

    rules = read_rules()  # DIMACS format
    rules = parse_rules(rules)  # int
    set_dim(len(rules[0]))
    sudoku = read_game()  #input file as arg later
    sudoku = parse_game(sudoku)  # int

    start_time = time.time()

    for field in sudoku:
        rules=simplify(rules,field)
    first_lit=heuristics[h](rules)
    if not rec(rules, first_lit, sudoku):
        rec(rules, -first_lit, sudoku)

    running_time=time.time() - start_time
    print(running_time)