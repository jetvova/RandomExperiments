import numpy
import numpy as np

import numpy as np

def read(filename):
    with open(filename) as f:
        content = f.readlines()
    for i in range(0, len(content)):
        content[i] = float(content[i])
    return content


def mean(listname):
    avg = sum(listname) / float(len(listname))
    return avg

a = read("a.txt")

print a


print """



   """


aDivisThree = []

for i in range (0, len(a)):
    x = a[i]
    if int(x) == x:
        if x % 3 == 0:
            aDivisThree.append(x)



aDivisThree = [e for e in a if int(e)==e and e % 3 == 0]


print aDivisThree

print numpy.min(aDivisThree), numpy.max(aDivisThree), numpy.sum(aDivisThree)











