import re, math, sympy

def myeval(expr):
    return eval(expr)

def myexec(expr,g,d):
    exec('import sympy \n' + expr,g,d)