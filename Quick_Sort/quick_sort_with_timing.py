import random
from random import choice,shuffle
import time

numbers=[random.randint(1,12) for i in range(15)]
shuffle(numbers)
print(numbers)
arr=[]
iteration=0

start=time.time()
def benchmark(func):
    def wrapper(*args):
        global iteration
        iteration+=1
        a=func(*args)
        print('[*]  Итерации {}.'.format(iteration))
        return a
    return wrapper
@benchmark
def QuickSort(numbers):
    if len(numbers)<=1:
        return numbers
    else:
        left=[]
        right=[]
        middle=[]
        random_element=random.choice(numbers)
        left=[i for i in numbers if i<random_element]
        right=[i for i in numbers if i>random_element]
        middle=[i for i in numbers if i==random_element]
        return QuickSort(left)+middle+QuickSort(right)
end=time.time()
print(QuickSort(numbers))
print(end-start)