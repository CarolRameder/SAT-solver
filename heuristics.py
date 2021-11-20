from collections import defaultdict
import copy

# algorithms state to assign either true or fals value, I return the "normal" vs. negated version

def DLCS(lst):
    clauses = copy.deepcopy(lst)
    literal_count = defaultdict(int)
    literal_count2 = defaultdict(int)
    for clause in clauses:
        for number in clause:
            literal_count[abs(number)] += 1
            literal_count2[number] += 1
    max_key = max(literal_count, key=literal_count.get)
    
    if max_key and -max_key in literal_count2:
        if literal_count2[max_key] > literal_count2[-max_key]:
            return max_key
        else:
            return -max_key
    else:
        return max_key

# we can choose if we take the highest positive or negative value => can decide with True
def DLIS(lst, key_max = True):
    clauses = copy.deepcopy(lst)
    pos_literal_count = defaultdict(int)
    neg_literal_count = defaultdict(int)
    for clause in clauses:
        for number in clause:
            if number > 0:
                pos_literal_count[number] += 1
            else:
                neg_literal_count[number] += 1
    
    # pick two max values => one for positive and one for negative literals
    max_key = max(pos_literal_count, key=pos_literal_count.get)
    min_key = max(neg_literal_count, key=neg_literal_count.get)

    if key_max == True:
        if max_key in pos_literal_count and -max_key in neg_literal_count:
            if pos_literal_count[max_key] > neg_literal_count[-max_key]:
                return max_key
            else:
                return -max_key
        else:
            return max_key
    
    else:
        if min_key in neg_literal_count and -min_key in pos_literal_count:
            if neg_literal_count[min_key] > pos_literal_count[-min_key]:
                return min_key
            else:
                return -min_key
        else:
            return min_key

    
        


