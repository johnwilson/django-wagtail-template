from datetime import datetime
from random import seed, randint
import functools


def newid(size):
    # seed the generator
    t = datetime.timestamp(datetime.now())
    seed(t)
    # generate list of random numbers
    int_list = []
    for _ in range(size):
        n = randint(0, 9)
        int_list.append(n)

    res = functools.reduce(lambda total, d: 10 * total + d, int_list, 0)
    return res