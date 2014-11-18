# from http://code.activestate.com/recipes/269554-select-the-nth-smallest-element/
# algorithm to find the kth smallest number in the list.

import random

def select(data, n):
    #print data
    "Find the nth rank ordered element (the least value has rank 0)."
    data = list(data)
    if not 0 <= n < len(data):
        raise ValueError('not enough elements for the given rank')
    while True:
        pivot = random.choice(data)
        print pivot
        pcount = 0
        under, over = [], []
        uappend, oappend = under.append, over.append
        for elem in data:
            if elem < pivot:
                uappend(elem)
            elif elem > pivot:
                oappend(elem)
            else:
                pcount += 1
        if n < len(under):
            data = under
        elif n < len(under) + pcount:
            return pivot
        else:
            data = over
            n -= len(under) + pcount
        print under,over


print select([12,33,42,11,85,6,23,45],5)