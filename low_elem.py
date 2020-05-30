from random import random
a = []
N = 10
for i in range(N):
    a.append(int(random()*100))
print(a)
small = a[0]
for i in range(1, len(a)):
    if a[i] < small:
        small = a[i]
print(small)
