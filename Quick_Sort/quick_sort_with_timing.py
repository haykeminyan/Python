import random
from random import choice,shuffle
import time

numbers=[i for i in range(155)]
shuffle(numbers)
print(numbers)
arr=[]
iteration=0
def benchmark(func):
    def wrapper(*args):
        global iteration
        start = time.time()
        iteration+=1
        a=func(*args)
        end = time.time()
        arr.append(end-start)
        res=sum(arr)
        print('[*] Время выполнения: итерации {} {}секунд.'.format(iteration,res))
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
print(QuickSort(numbers))