import numpy as np
import numpy as np
import scipy
from scipy import stats
import matplotlib as plt
from matplotlib import pyplot

doc = "run1_results.txt"
doc2 = "run2_results_4x4.txt"

def read_file(doc):
    lst = []
    with open(doc, "r") as f:
        lines = f.readlines()
        combined = "".join(lines)
    
    return combined

def clear_up(lst):
    lst2 = []
    for element in lst:
        if "\n" in element:
            lst2.append(element.replace("\n", ""))
        elif "[" in element:
            lst2.append(element.strip("["))
        elif "]" in element:
            lst2.append(element.strip("]"))
        else:
            lst2.append(element)
            

    lst3 = [float(x) for x in lst2]
    return lst3
        


# 9x9

test = read_file(doc)

lst = test.split("[")
            
dim_9_dpll_group1 = lst[1].split(",")
dim_9_dpll_group2 = lst[2].split(",")
dim_9_dlis_group1 = lst[3].split(",")
dim_9_dlis_group2 = lst[4].split(",")
dim_9_jwos_group1 = lst[5].split(",")
dim_9_jwos_group2 = lst[6].split(",")

dim_9_dpll_group1[-1] = "46.5501446723938"
dim_9_dpll_group2[-1] = "47.77571940422058"
dim_9_dlis_group1[-1] = "46.31769323348999"
dim_9_dlis_group2[-1] = "38.60492992401123"
dim_9_jwos_group1[-1] = "52.626084327697754"
dim_9_jwos_group2[-1] = "25.998109579086304"

dim_9_dpll_group1 = clear_up(dim_9_dpll_group1)
dim_9_dpll_group2 = clear_up(dim_9_dpll_group2)
dim_9_dpll = dim_9_dpll_group1 + dim_9_dpll_group2
dim_9_dlis_group1 = clear_up(dim_9_dlis_group1)
dim_9_dlis_group2 = clear_up(dim_9_dlis_group2)
dim_9_dlis = dim_9_dlis_group1 + dim_9_dlis_group2
dim_9_jwos_group1 = clear_up(dim_9_jwos_group1)
dim_9_jwos_group2 = clear_up(dim_9_jwos_group2)
dim_9_jwos = dim_9_jwos_group1 + dim_9_jwos_group2

# 4x4

f2 = read_file(doc2)
f2 = f2.split("]")


dim_4_dpll_group1 = f2[0].split(",")
dim_4_dpll_group2 = f2[1].split(",")
dim_4_dpll_group1_bkt = f2[2].split(",")
dim_4_dpll_group2_bkt = f2[3].split(",")
dim_4_dpll_group1_unit = f2[4].split(",")
dim_4_dpll_group2_unit = f2[5].split(",")

dim_4_dpll_group1[0] = "0.08225584030151367"
dim_4_dpll_group2[0] = "0.0512089729309082"
dim_4_dpll_group1_bkt[0] = "0.0"
dim_4_dpll_group2_bkt[0] = "0.0"
dim_4_dpll_group1_unit[0] = "80.0"
dim_4_dpll_group2_unit[0] = "57.0"

dim_4_dpll_group1 = clear_up(dim_4_dpll_group1)
dim_4_dpll_group2 = clear_up(dim_4_dpll_group2)
dim_4_dpll_group1_bkt = clear_up(dim_4_dpll_group1_bkt)
dim_4_dpll_group2_bkt = clear_up(dim_4_dpll_group2_bkt )
dim_4_dpll_group1_unit = clear_up(dim_4_dpll_group1_unit)
dim_4_dpll_group2_unit = clear_up(dim_4_dpll_group2_unit)

#----------------------------


dim_4_dlis_group1 = f2[6].split(",")
dim_4_dlis_group2 = f2[7].split(",")
dim_4_dlis_group1_bkt = f2[8].split(",")
dim_4_dlis_group2_bkt = f2[9].split(",")
dim_4_dlis_group1_unit = f2[10].split(",")
dim_4_dlis_group2_unit = f2[11].split(",")

dim_4_dlis_group1[0] = 0.12261080741882324
dim_4_dlis_group2[0] = 0.11937141418457031
dim_4_dlis_group1_bkt[0] = 0.0
dim_4_dlis_group2_bkt[0] = 0.0
dim_4_dlis_group1_unit[0] = 59.0
dim_4_dlis_group2_unit[0] = 57.0

dim_4_dlis_group1 = clear_up(dim_4_dlis_group1)
dim_4_dlis_group2 = clear_up(dim_4_dlis_group2)
dim_4_dlis_group1_bkt = clear_up(dim_4_dlis_group1_bkt)
dim_4_dlis_group2_bkt = clear_up(dim_4_dlis_group2_bkt)
dim_4_dlis_group1_unit = clear_up(dim_4_dlis_group1_unit)
dim_4_dlis_group2_unit = clear_up(dim_4_dlis_group2_unit)

#--------------------------------------

dim_4_jwos_group1 = f2[6].split(",")
dim_4_jwos_group2 = f2[7].split(",")
dim_4_jwos_group1_bkt = f2[8].split(",")
dim_4_jwos_group2_bkt = f2[9].split(",")
dim_4_jwos_group1_unit = f2[10].split(",")
dim_4_jwos_group2_unit = f2[11].split(",")

dim_4_jwos_group1[0] = "0.12261080741882324"
dim_4_jwos_group2[0] = "0.11937141418457031"
dim_4_jwos_group1_bkt[0] = "0.0"
dim_4_jwos_group2_bkt[0] = "0.0"
dim_4_jwos_group1_unit[0] = "59.0"
dim_4_jwos_group2_unit[0] = "57.0"

dim_4_jwos_group1 = clear_up(dim_4_jwos_group1)
dim_4_jwos_group2 = clear_up(dim_4_jwos_group2 )
dim_4_jwos_group1_bkt = clear_up(dim_4_jwos_group1_bkt)
dim_4_jwos_group2_bkt = clear_up(dim_4_jwos_group2_bkt)
dim_4_jwos_group1_unit = clear_up(dim_4_jwos_group1_unit)
dim_4_jwos_group2_unit = clear_up(dim_4_jwos_group2_unit)


# -----------------------------------------------------------------------------------


# tests

# Boxplots 
### three different graphs?
### for each algorithm both dimensions and both groups

plt.pyplot.boxplot(dim_9_dpll)
plt.title("Box Plots")
# show plot
plt.pyplot.show()



# ttests
### as many as possible and look at the results
### between each dimensions and each group?
### one time merge all algorithms and groups into dimensions/group 1 and two and run 3 big t-test

scipy.stats.ttest_ind(dim_9_jwos_group2, dim_9_jwos_group1)
