from random import random
from typing import List
from collections import Counter

a = [[int(random()*(43-4))+41 for i in range(100)] for i in range(12)]


def mean(a: List[int]) -> float:
    res = [sum(a[i])/len(a[i]) for i in range(len(a))]
    return res


def median(a: List[int]) -> float:
    b = [sorted(a[i]) for i in range(len(a))]
    res = []
    for i in range(len(b)):
        c = b[i]
        if len(c) % 2 == 0:
            res.append((c[len(c)//2-1]+c[len(c)//2-1])/2)
        res.append(c[len(c)//2])
    return res


def mode(a: List[int]) -> float:
    counts = [Counter(a[i]) for i in range(len(a))]
    res = [k for i in counts for k, v in i.items() if v == max(i.values())]
    return res


print(mean(a))
print(median(a))
print(mode(a))
