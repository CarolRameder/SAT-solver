import random
import numpy as np


class DPLL:

    def __init__(self, clause_list, num_list, dim):
        self.clause_list = clause_list
        self.num_list = num_list
        self.truth_values = {}
        self.dim = dim

    def set_dict(self):
        for num in self.num_list:
            self.truth_values[num] = 1

    # simplifies based on the two rules
    # return 0 if unsat, 1 if sat, -1 if uncomplete
    def show(self):
        sudoku = np.zeros((9, 9), dtype=int)
        for key in self.truth_values:
            lin = int(str(key)[0]) - 1
            col = int(str(key)[1]) - 1
            val = int(str(key)[2])
            sudoku[lin][col] = val
        print(sudoku)

    def simplify(self):
        for clause in reversed(self.clause_list):
            for num in clause:
                if (num, 1) in self.truth_values.items() or (-num, 0) in self.truth_values.items():
                    self.clause_list.remove(clause)
                    break
                elif (num, 0) in self.truth_values.items() or (-num, 1) in self.truth_values.items():
                    clause.remove(num)
            if len(clause) == 0:
                print("empty list0")
                return 0
        if len(self.clause_list) == 0:
            print("empty list1")
            self.show()
            return 1
        return -1

    # returns the first unit literal found or 0 if no unit literals
    def unit_lit(self):
        for clause in self.clause_list:
            if len(clause) == 1:
                return clause[0]
        return 0

    # !!to be modified for other configurations not 9*9
    def rand_heuristic(self):
        rand_list = list(range(100, 1000))
        for num in self.truth_values.keys():
            rand_list.remove(num)
        return random.choice(rand_list), random.choice([0, 1])

    # assigns value to a random literal in clause_list
    # simplifies
    # tries unit clause assigantion
    # simplifies
    def bkt(self, lit, truth_val):

        # save state
        current_state = self.clause_list.copy(), self.truth_values.copy()
        print("bkt call")
        self.truth_values[lit] = truth_val
        result = self.simplify()
        if result == 0:
            return 0
        elif result == 1:
            return 1

        ul = self.unit_lit()
        while ul != 0:
            if ul > 0:
                self.truth_values[ul] = 1
            else:
                self.truth_values[-ul] = 0

            result = self.simplify()
            if result == 0:
                return 0
            elif result == 1:
                return 1

            ul = self.unit_lit()

        # pure rule?!

        # heuristic assignation
        nex_lit, next_truth_val = self.rand_heuristic()

        if self.bkt(nex_lit, next_truth_val) == 0:
            self.clause_list, self.truth_values = current_state
            return self.bkt(lit, 1 - truth_val)

    def run(self):
        self.set_dict()
        # self.delete_tautologies()
        self.simplify()  # it will not return anything for the first step
        lit, truth_val = self.rand_heuristic()
        print(self.bkt(lit, truth_val))
