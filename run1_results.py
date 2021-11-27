import numpy as np
import numpy as np
import scipy
from scipy import stats
import matplotlib as plt
from matplotlib import pyplot

doc = "run1_results.txt"
doc2 = "run2_results_4x4.txt"
doc3 = "run2_9x9.txt"

def read_file(doc):
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
        
#------------------------------------------------

# 9x9
"""
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
"""
#-----------------------------------------------------

f = read_file(doc3)

f = f.split("[")

dim_9_dpll_g1_mean = 45.34244313406114
dim_9_dpll_g2_mean = 45.98124123323159

dim_9_dpll_g1_sd = 17.173147847411876
dim_9_dpll_g2_sd = 14.639968073035606

dim_9_dpll_g1_bkt_mean = 3.154228855721393
dim_9_dpll_g2_bkt_mean = 5.367213114754098

dim_9_dpll_g1_bkt_sd = 4.712753367813131
dim_9_dpll_g2_bkt_sd = 6.25650406001169

dim_9_dpll_g1_unit_mean = 969.7462686567164
dim_9_dpll_g2_unit_mean = 1067.9409836065574

dim_9_dpll_g1_unit_sd = 355.34933452977464
dim_9_dpll_g2_unit_sd = 449.22875598695805

f[14]


dim_9_dpll_group1 = f[1].split(",")
dim_9_dpll_group2 = f[2].split(",")
dim_9_dpll_group1_bkt = f[3].split(",")
dim_9_dpll_group2_bkt = f[4].split(",")
dim_9_dpll_group1_unit = f[5].split(",")
dim_9_dpll_group2_unit = f[6].split(",")


dim_9_dpll_group1[-1] = "44.6946964263916"
dim_9_dpll_group2[-1] = "34.83184766769409"
dim_9_dpll_group1_bkt[-1] = "3.0"
dim_9_dpll_group2_bkt[-1] = "8.0"
dim_9_dpll_group1_unit[-1] = "701.0"
dim_9_dpll_group2_unit[-1] = "701.0"

dim_9_dpll_group1 = clear_up(dim_9_dpll_group1)
dim_9_dpll_group2 = clear_up(dim_9_dpll_group2)
dim_9_dpll_group1_bkt = clear_up(dim_9_dpll_group1_bkt)
dim_9_dpll_group2_bkt = clear_up(dim_9_dpll_group2_bkt )
dim_9_dpll_group1_unit = clear_up(dim_9_dpll_group1_unit)
dim_9_dpll_group2_unit = clear_up(dim_9_dpll_group2_unit)


dim_9_dlis_group1 = f[8].split(",")
dim_9_dlis_group2 = f[9].split(",")
dim_9_dlis_group1_bkt = f[10].split(",")
dim_9_dlis_group2_bkt = f[11].split(",")
dim_9_dlis_group1_unit = f[12].split(",")
dim_9_dlis_group2_unit = f[13].split(",")

dim_9_dlis_group1[-1] = "47.15792894363403"
dim_9_dlis_group2[-1] = "29.863544940948486"
dim_9_dlis_group1_bkt[-1] = "4.0"
dim_9_dlis_group2_bkt[-1] = "6.0"
dim_9_dlis_group1_unit[-1] ="996.0"
dim_9_dlis_group2_unit[-1] = "740.0"

dim_9_dlis_group1 = clear_up(dim_9_dlis_group1)
dim_9_dlis_group2 = clear_up(dim_9_dlis_group2)
dim_9_dlis_group1_bkt = clear_up(dim_9_dlis_group1_bkt)
dim_9_dlis_group2_bkt = clear_up(dim_9_dlis_group2_bkt)
dim_9_dlis_group1_unit = clear_up(dim_9_dlis_group1_unit)
dim_9_dlis_group2_unit = clear_up(dim_9_dlis_group2_unit)


dim_9_jwos_group1 = f[14].split(",")
dim_9_jwos_group2 = f[15].split(",")
dim_9_jwos_group1_bkt = f[16].split(",")
dim_9_jwos_group2_bkt = f[17].split(",")
dim_9_jwos_group1_unit = f[18].split(",")
dim_9_jwos_group2_unit = f[19].split(",")


dim_9_jwos_group1[-1] = "41.198978\n18565369"
dim_9_jwos_group2[-1] = "27.537715673446655"
dim_9_jwos_group1_bkt[-1] = "38.0"
dim_9_jwos_group2_bkt[-1] = "5.0"
dim_9_jwos_group1_unit[-1] = "1901.0"
dim_9_jwos_group2_unit[-1] = "923.0"

dim_9_jwos_group1 = clear_up(dim_9_jwos_group1)
dim_9_jwos_group2 = clear_up(dim_9_jwos_group2 )
dim_9_jwos_group1_bkt = clear_up(dim_9_jwos_group1_bkt)
dim_9_jwos_group2_bkt = clear_up(dim_9_jwos_group2_bkt)
dim_9_jwos_group1_unit = clear_up(dim_9_jwos_group1_unit)
dim_9_jwos_group2_unit = clear_up(dim_9_jwos_group2_unit)

# ------------------------------------------------------
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


dim_4_dlis_group1 = f2[6].split(",")
dim_4_dlis_group2 = f2[7].split(",")
dim_4_dlis_group1_bkt = f2[8].split(",")
dim_4_dlis_group2_bkt = f2[9].split(",")
dim_4_dlis_group1_unit = f2[10].split(",")
dim_4_dlis_group2_unit = f2[11].split(",")

dim_4_dlis_group1[0] = "0.12261080741882324"
dim_4_dlis_group2[0] = "0.11937141418457031"
dim_4_dlis_group1_bkt[0] = "0.0"
dim_4_dlis_group2_bkt[0] = "0.0"
dim_4_dlis_group1_unit[0] = "59.0"
dim_4_dlis_group2_unit[0] = "57.0"

dim_4_dlis_group1 = clear_up(dim_4_dlis_group1)
dim_4_dlis_group2 = clear_up(dim_4_dlis_group2)
dim_4_dlis_group1_bkt = clear_up(dim_4_dlis_group1_bkt)
dim_4_dlis_group2_bkt = clear_up(dim_4_dlis_group2_bkt)
dim_4_dlis_group1_unit = clear_up(dim_4_dlis_group1_unit)
dim_4_dlis_group2_unit = clear_up(dim_4_dlis_group2_unit)


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

plt.pyplot.boxplot(dim_4_dpll_group1)
plt.title("Box Plots")
# show plot
plt.pyplot.show()



# ttests
### as many as possible and look at the results
### between each dimensions and each group?
### one time merge all algorithms and groups into dimensions/group 1 and two and run 3 big t-test

scipy.stats.ttest_ind(dim_4_dlis_group1_unit, dim_4_dlis_group2_unit)
