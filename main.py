import time
import sys, getopt
from DPLL import DPLL
# sys.setrecursionlimit(100000)
import time

DIM = 9
sudokus = "1000_sudokus.txt"  # argument
rules = "9x9_sudoku-rules.txt"  # hardcode read


# returns DIMACS representation of the given input - initial configuration
# will be argument on run
def read_game():
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

#first unassigned available
def select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal[0]

def simplify(clauses, lit):
    for clause in reversed(clauses):
        for num in clause:
            if num==lit:
                clauses.remove(clause)
                break
            elif num==-lit:
                clause.remove(num)
        if len(clause) == 0:
            #print("empty list0")
            return 0
    if len(clauses) == 0:
        print("Solution found")
        return 1
    return clauses


def rec(clauses, lit, sol):
    # add argument to simplify
    sol.append(lit)
    result = simplify(clauses, lit)
    if result == 0:
        return 0
    elif result == 1:
        return 1

    new_lit = select_literal(result)



#   if (dpll_2(α,  not P))return true;
#   return dpll_2(α, P);


if __name__ == '__main__':
    # unused
    # heuristic=sys.argv[1]
    # input_file=sys.argv[2] #argument for read_game()
    #

    sudoku = read_game()  # DIMACS format
    sudoku = parse_game(sudoku)  # int
    rules = read_rules()  # DIMACS format
    rules = parse_rules(rules)  # int
    #start_time = time.time()
    clauses=[]
    for field in sudoku:
        clauses=simplify(rules,field)
    new_lit=select_literal(clauses)

    rec(clauses, new_lit)
