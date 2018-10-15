"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:


Implement car and cdr.
"""
def cons(a, b):
    # takes a & b and returns new anonymous function
    # import pdb; pdb.set_trace()
    def pair(f): # takes in a function
        return f(a, b) 
    return pair # returns a function


def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)


