class DPLL:

    def __init__(self, clause_list, num_list):
        self.clause_list = clause_list
        self.num_list = num_list
        self.truth_values={}

    # set first dictionary based on the list containing the numbers of the sudoku
    def set_dict0(self):

        for clause in self.clause_list:
            if len(self.clause_list) == 0:
                print("unsatisfiable")
                break
                # => find way in run function to stop everything

        # set up empty dictionary to put the numbers and values in
        value_dict = {}
        # set first unit clauses in dict
        for element in self.num_list:
            if element > 0:
                value_dict[str(element)] = 1
            elif element < 0:
                value_dict[str(element)[1:]] = 0

        return value_dict

    # based on the first dictionary, loop through clauses again to find unit_clauses and delete then the clauses with one True literal and delete False literals
    def unit_clauses0(self, dictionary):
        new_list = self.clause_list.copy()

        # look if there are unit clauses in clause list
        for clause in self.clause_list:
            if len(clause) == 1:
                if clause[0] > 0:
                    dictionary[str(clause[0])] = 1
                elif clause[0] < 0:
                    dictionary[str(clause[0])[1:]] = 0

        for clause in reversed(new_list):
            for number in clause:
                if str(number) in dictionary:
                    if dictionary[str(number)] == 1:
                        new_list.remove(clause)
                        break

                    elif dictionary[str(number)] == 0:
                        clause.remove(number)

        return new_list

    def set_dict(self):

        for num in self.num_list:
            self.truth_values[num]=1
        #print(self.truth_values)

    def simplify(self):
        for clause in self.clause_list:
            for num in clause:
                if self.truth_values[num]==1 or self.truth_values[-num]==0:
                    self.clause_list.remove(clause)
                    break
                elif self.truth_values[num]==0 or self.truth_values[-num]==1:
                    clause.remove(num)
            if len(clause)==0:
                print("unsatisfiable?")
        if len(self.clause_list)==0:
            print("solution found?")


    def run(self):
        self.set_dict()
        self.simplify()
