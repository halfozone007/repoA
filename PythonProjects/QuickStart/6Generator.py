#So a generator function returns an generator object that is iterable, i.e., can be used as an Iterators .

def giveNumbers():
    yield 1
    yield 2
    yield 3
    yield 4


for x in giveNumbers():
    print(x)