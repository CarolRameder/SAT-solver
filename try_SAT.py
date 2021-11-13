from functools import lru_cache
from typing import DefaultDict
import pycosat
import sys, getopt
import time
from collections import defaultdict



class DPLL:

    def __init__(self, clause_list, num_list):
        self.clause_list = clause_list
        self.num_list = num_list
        self.original_dict = {}
        self.value_dict = {}


        

    # set first dictionary based on the list containing the numbers of the sudoku
    def set_up(self):

        for clause in self.clause_list:
            if len(self.clause_list) == 0:
                print("unsatisfiable")
                break
                # => find way in run function to stop everything

        
        # set up empty dictionary to put the numbers and values in
        # set first unit clauses in dict
        for element in self.num_list:
            if element > 0:
                self.original_dict[str(element)] = 1
            elif element < 0:
                self.original_dict[str(element)[1:]] = 0
        
        # copy original dict to work with it as value dict from now on; leave original dict
        self.value_dict = self.original_dict.copy()


    # check for tautologies one time in the beginning         
    def tautology(self):
        # loop through clauses
        for clause in reversed(self.clause_list):
            # set taut to false in order to remonve clause if there is a tautology
            taut = False
            for number in clause:
                for i in range(len(clause)):
                    # if there is a a pos and a neg literal in one clause => remove clause
                    if -number == clause[i]:
                        taut  = True    
            if taut == True:
                self.clause_list.remove(clause)
        # return a list of clauses where the tautoloy clauses are removed
    

    # check for pure literals => atm no return becuase I implememted a self dict; could return a dict with the updated values => then ready to do unit testing again, etc.
    def pure_literal(self):
        # set default dic to have all literals saved as keys
        literal_count = defaultdict(int)
        for clause in self.clause_list:
            for number in clause:
                literal_count[number] += 1
        
        for key in literal_count.keys():
            # look for pure literals and set them to true or false in value dict 
            if key and not -key in literal_count.keys():
                if key > 0:
                    self.value_dict[str(key)] = 1
                elif key < 0:
                    self.value_dict[str(key)] = 0
        

    #based on the first dictionary, loop through clauses again to find unit_clauses and delete then the clauses with one True literal and delete False literals
    def unit_clauses(self):
        new_list = self.clause_list.copy()

        # look if there are unit clauses in clause list
        for clause in self.clause_list:
            if len(clause) == 1:
                if clause[0] > 0:
                    self.value_dict[str(clause[0])] = 1
                elif clause[0] < 0:
                    self.value_dict[str(clause[0])[1:]] = 0

        # remove clause if literal is set to true and remove literal from clauses if it is set to false
        for clause in reversed(new_list):
            for number in clause:
                if str(number) in self.value_dict:
                    if self.value_dict[str(number)] == 1:
                        new_list.remove(clause)
                        break
                    
                    elif self.value_dict[str(number)] == 0:
                        clause.remove(number)

        return new_list


        


        







    def run(self):
        pass


        