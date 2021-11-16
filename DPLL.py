import random
class DPLL:

    def __init__(self, clause_list, num_list,dim):
        self.clause_list = clause_list
        self.num_list = num_list
        self.truth_values={}
        self.satisf=0
        self.dim=dim

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

    #simplifies based on the two rules
    #make it return sth depending on satisf/unsat?
    def simplify(self):
        for clause in reversed(self.clause_list):
            for num in clause:
                if (num,1) in self.truth_values.items() or (-num,0) in self.truth_values.items():
                    self.clause_list.remove(clause)
                    break
                elif (num,0) in self.truth_values.items() or (-num,1) in self.truth_values.items():
                    clause.remove(num)
            if len(clause)==0:
                #print("unsatisfiable?")
                self.satisf=-1
                break
        if len(self.clause_list)==0:
            print("solution found?")
            self.satisf=1

    #returns the first unit literal found or 0 if no unit literals
    def unit_lit(self):
        for clause in self.clause_list:
            if len(clause)==1:
                return clause[0]
        return 0

    #!!to be modified for other configurations not 9*9
    def rand_heuristic(self):
        rand_list=list(range(100,1000))
        for num in self.truth_values.keys():
            rand_list.remove(num)
        return random.choice(rand_list), random.randint(0, 1)

    # assigns value to a random literal in clause_list
    # simplifies
    # tries unit clause assigantion
    # simplifies
    def bkt(self):
        if self.satisf==1:
            print(self.truth_values)
            return
        else:
            #unit literals
            ul=self.unit_lit()
            while ul!=0:
                if ul>0:
                    self.truth_values[ul]=1
                else:
                    self.truth_values[-ul]=0
                self.simplify()
                ul = self.unit_lit()

            #pure rule?!

            #heuristic assignation
            lit, truth_val=self.rand_heuristic()
            self.truth_values[lit]=truth_val

            self.simplify()
            self.bkt()


    def run(self):
        self.set_dict()
        #self.delete_tautologies()
        self.simplify()
        #self.bkt()
        # if self.satisf==-1 or self.satisf==0:
        #     print("Unsolvable")
