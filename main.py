import time
import sys, getopt
from DPLL import DPLL
sys.setrecursionlimit(10000)
import time
DIM = 9
sudokus="1000_sudokus.txt" #argument
rules="9x9_sudoku-rules.txt" #hardcode read

#returns DIMACS representation of the given input - initial configuration
#will be argument on run
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

#hardcoded
def read_rules():
    with open(rules,'r') as f:
        delete=f.readline()
        rls=f.read()
    return rls

def parse_game(arg):
    arg=arg.split("\n")
    list_rep=[]
    for i in range(len(arg)-1):
        list_rep.append(int(arg[i].split()[0]))
    return list_rep

def parse_rules(arg):
    arg = arg.split("\n")
    list_rep=[]
    for i in range(len(arg)):
        arg[i]=arg[i].split()
        curent_list=[]
        for j in range(len(arg[i])-1):
            curent_list.append(int(arg[i][j]))
        list_rep.append(curent_list)
    return list_rep

#test !!! random din available
def __select_literal(cnf, truth_val):
    for c in cnf:
        for literal in c:
            if literal[0] not in truth_val.keys():
                return literal[0]
#[{("p", True), ("q", False)}, {("p", True), ("r", True)}]

def parse2(clause_list):
    parsed_list=[]
    for clause in clause_list:
        parsed_clause=set()
        for num in clause:
            if num>0:
                p_lit=(num, True)
            else:
                p_lit = (-num, False)
            parsed_clause.add(p_lit)
        parsed_list.append(parsed_clause)
    #print(parsed_list)
    return parsed_list

def dpll(cnf, assignments):
    if len(cnf) == 0:
        return True, assignments

    if any([len(c) == 0 for c in cnf]):
        return False, None

    l = __select_literal(cnf,assignments)

    new_cnf = [c for c in cnf if (l, True) not in c]
    new_cnf = [c.difference({(l, False)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: True}})
    if sat:
        return sat, vals

    new_cnf = [c for c in cnf if (l, False) not in c]
    new_cnf = [c.difference({(l, True)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: False}})
    if sat:
        return sat, vals

    return False, None


if __name__ == '__main__':
    #unused
    #heuristic=sys.argv[1]
    #input_file=sys.argv[2] #argument for read_game()
    #
    sudoku = read_game() #DIMACS format
    sudoku = parse_game(sudoku) #int
    rules = read_rules() #DIMACS format
    rules = parse_rules(rules) #int
    start_time = time.time()
    #alg = DPLL(rules,sudoku,DIM,heuristic)
    #alg.run()

    #second version
    cnf = parse2(rules)
    dict2={129: True, 134: True, 171: True, 183: True, 357: True, 366: True, 392: True, 428: True, 451: True, 523: True, 532: True, 642: True, 686: True, 755: True, 774: True, 868: True, 897: True, 936: True, 943: True, 964: True, 998: True}
    print(dpll(cnf, dict2))
    #print("--- %s seconds ---" % (time.time() - start_time))


