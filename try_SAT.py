from functools import lru_cache
from typing import DefaultDict
import pycosat
import sys, getopt
import time
from collections import defaultdict
import math
import random


def read_soduko(in_file):
    f = open(in_file, "r") 
    sudokus = []
    format_sudokus = []
    for line in f:
        sudokus.append(line.split())

    for sud in sudokus:
        s = []
        for element in sud:
            counter_rows = 1
            counter_columns = 0
            for number in element:
                counter_columns += 1
                if number.isnumeric():
                    s.append(int(str(counter_rows) + str(counter_columns) + str(number)))
                
                if counter_columns == math.sqrt(len(element)):
                    counter_rows += 1
                    counter_columns = 0

        format_sudokus.append(s) 
    f.close()   
    return format_sudokus

sud_4 = read_soduko("4x4.txt")
sud_9 = "sudoku-example.txt"



def prepare_set(rules_file, input_file):
    f = open(rules_file, "r")
    s = open(input_file, "r")
    cnf = []
    sudoku = []
    for line in f:
        clause = line.split()
        cnf.append(clause[:-1])

    for line in s:
        sudoku.append(line.split()[0])

    s.close()
    return cnf[1:], sudoku
    
  
rules_file, input_file = prepare_set("sudoku-rules-4x4.txt", "sudoku-example.txt")
rules_file



class DPLL:

    def __init__(self, clause_list, num_list):
        self.clause_list = clause_list
        self.num_list = num_list
        self.value_dict = {}


        

    # set first dictionary based on the list containing the numbers of the sudoku
    # set up empty dictionary to put the numbers and values in
    # set first unit clauses in dict
    # maybe merge cnfs?? => to only have one input file 

    def set_up(self):

        """
        for clause in self.clause_list:
            if len(self.clause_list) == 0:
                print("unsatisfiable")
                break
                # => find way in run function to stop everything
        """

        for clause in self.clause_list:
            for number in clause:
                if number > 0: # also abs works
                    self.value_dict[str(abs(number))] = None
                elif number < 0:
                    self.value_dict[str(abs(number))] = None
                    

        for element in self.num_list:
            if element > 0:
                self.value_dict[str(abs(element))] = 1
            elif element < 0:
                self.value_dict[str(abs(element))] = 0

        

    # check for tautologies one time in the beginning
    # loop through clauses      
    # set taut to false in order to remonve clause if there is a tautology
    # if there is a a pos and a neg literal in one clause => remove clause
    # return a list of clauses where the tautoloy clauses are removed

    def tautology(self):
        for clause in reversed(self.clause_list):
            taut = False
            for number in clause:
                if -number in clause:
                    taut  = True    
            if taut == True:
                self.clause_list.remove(clause)
        
    

    # check for pure literals => atm no return becuase I implememted a self dict; could return a dict with the updated values => then ready to do unit testing again, etc.
    # set default dic to have all literals saved as keys
    # look for pure literals and set them to true or false in value dict 
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
        for clause in self.clause_list:
            if len(clause) == 1:
                if clause[0] > 0:
                    self.value_dict[str(clause[0])] = 1
                elif clause[0] < 0:
                    self.value_dict[str(clause[0])[1:]] = 0


    # remove clause if literal is set to true and remove literal from clauses if it is set to false
    def shorten(self):    
        for clause in reversed(self.clause_list):
            for number in clause:
                if str(abs(number)) in self.value_dict:
                    if number > 0:
                        if self.value_dict[str(abs(number))] == 1:
                            self.clause_list.remove(clause)
                        
                        elif self.value_dict[str(abs(number))] == 0:
                            clause.remove(number)

                    elif number < 0:
                        if self.value_dict[str(abs(number))] == 1:
                            clause.remove(number)

                        elif self.value_dict[str(abs(number))] == 0:
                            self.clause_list.remove(clause)
                            
    """    
    def check(self): 
        if len(self.clause_list) == 0:
            return True, self.value_dict
        
        else:
            for clause in self.clause_list:
                if clause == 0:
                    return False
    """

    def check(self):
        for clause in self.clause_list:
                if clause == 0:
                    return False
        
        

    def backtracking(self):

        if len(self.clause_list) == 0:
            return True, self.value_dict
        else:
            split_key = random.randint(0, len(self.value_dict.keys))
            split_value = random.randint(0,1)
            names_of_keys = [key for key in self.value_dict if self.value_dict[key] == None]
            
            self.value_dict[names_of_keys[split_key]] = split_value

            # -----> make stop and start thingy

            self.unit_clauses()
            self.shorten()
            self.check()

            self.backtracking()


   


        





    def run(self):
        pass


        