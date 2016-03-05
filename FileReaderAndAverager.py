import numpy
import numpy as np

import numpy as np


def reject_outliers(data):
    u = np.mean(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 3 * s < e < u + 3 * s)]
    return filtered


d = [2, 4, 5, 1, 6, 5, 40]
filtered_d = reject_outliers(d)


# print filtered_d

# [2,4,5,1,6,5]



def read(filename):
    with open(filename) as f:
        content = f.readlines()
    for i in range(0, len(content)):
        content[i] = float(content[i])
    return content


a = read("a.txt")
b = read("b.txt")





def mean(listname):
    avg = sum(listname) / float(len(listname))
    return avg

a = reject_outliers(a)
b = reject_outliers(b)

meana = mean(a)
meanb = mean(b)

print "Mean of A:", meana
print "Mean of B:", meanb


def comparator(x, y):
    return str(((x / y) * 100) - 100) + "%"


if meana > meanb:
    print "Experiment A was more successful. It showed results larger by: "
    print comparator(meana, meanb)
elif meana < meanb:
    print "Experiment B was more successful. It showed results larger by:"
    print comparator(meanb, meana)
else:
    print "The experiments yielded the same result"

print """

Standard deviation of experiment A:"""

print numpy.std(a)

print """

Standard deviation of experiment B:"""

print numpy.std(b)

"""
for i in range (0, len(a)):
    if (a(i) - meana) > 3:
        a.remove(i)
"""



