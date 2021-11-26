import numpy as np
import numpy as np
import scipy
from scipy import stats
import matplotlib as plt
from matplotlib import pyplot

doc = "run1_results.txt"

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
