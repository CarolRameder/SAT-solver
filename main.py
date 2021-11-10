import time
DIM = 9
sudokus="1000_sudokus.txt" #argument
rules="9x9_sudoku-rules.txt" #read

#returns DIMACS representation of the given input - initial configuration
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


def read_rules():
    with open(rules,'r') as f:
        delete=f.readline()
        rls=f.read()
    return rls

def DPLL(sudoku, rules):
    #print (sudoku + rules)
    pass

start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    sudoku = read_game()
    rules = read_rules()
    start_time = time.time()
    answer = DPLL (sudoku, rules)

