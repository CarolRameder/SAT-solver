DIM = 9

#returns DIMACS representation of the given input - initial configuration
def read_game():
    f = open("1000_sudokus.txt", "r")
    game_rep = f.readline()
    game_final = ""
    for i in range(len(game_rep) - 1):
        if game_rep[i] != ".":
            l = int(i / DIM) + 1
            c = i % DIM + 1
            game_final = game_final + str(l) + str(c) + game_rep[i] + " 0\n"
    return game_final


def read_rules():
    with open("9x9_sudoku-rules.txt",'r') as f:
        delete=f.readline()
        rules=f.read()
    return rules

def DPLL(sudoku, rules):
    pass

if __name__ == '__main__':
    sudoku = read_game()
    rules = read_rules()
    answer = DPLL (sudoku, rules)

