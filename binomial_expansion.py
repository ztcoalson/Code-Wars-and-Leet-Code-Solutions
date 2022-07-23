import re
from math import comb

def terms(expr):
    _, terms, exponent = re.split('[(, )]', expr)
    exp = int(exponent[1])                          
    operator = "+" if "+" in terms else "-"
    negative = False
    if terms[0] == '-':                             
        negative = True
        terms = terms[1:]
    ax, b = re.split('[+, -]', terms)
    a, x, b = ax[:-1], ax[len(ax)-1], int(b)
    a = 1 if a == '' else int(a)
    if negative == True:
        a = -a
    return a, x, operator, b, exp

def expansion(a, x, operator, b, exp):
    sum = ""
    if operator == '-': b = -b
    for k in range(exp+1):
        combo = comb(exp, k)
        a_term, x_term, b_term = a**(exp-k), x, b**k
        if exp-k == 0:
            x_term = ""
        elif exp-k != 1: 
            x_term += "^" + str(exp-k)
        negative = False if (a_term > 0 and b_term > 0) or (a_term < 0 and b_term < 0) else True
        final_term = combo * abs(a_term) * abs(b_term)
        if negative == True:
            sum += "-"
        elif negative == False and k != 0:
            sum += "+"
        if final_term == 1 and x_term != "":
            sum += x_term
        else: 
            sum += str(final_term) + x_term
    return sum

def expand(expr):
    a, x, operator, b, exp = terms(expr)
    return expansion(a, x, operator, b, exp)
