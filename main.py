import time
import sys, getopt
from DPLL import DPLL
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

if __name__ == '__main__':
    sudoku = read_game()
    sudoku = parse_game(sudoku)
    rules = read_rules()
    rules = parse_rules(rules)
    start_time = time.time()
    alg = DPLL(rules,sudoku)
    alg.run()
    #print("--- %s seconds ---" % (time.time() - start_time))


