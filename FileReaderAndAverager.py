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
b = read("b.txt")

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
