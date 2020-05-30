from random import random
array = []
N = 11
for i in range(N):
    array.append(int(random()*111))
print(array)
print("-------------------------------------------------")
print("-------------------------------------------------")
array.sort()
print(array)
number = int(input())
low = 0
high = N-1
while low <= high:
    mid = (low+high)//2
    if array[mid] > number:
        high = mid-1
    elif array[mid] < number:
        low = mid+1
    else:
        print(mid)
        break
else:
    print("None")

    #[1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 8]
    # 3
    # low=0,high=10,mid=5
    # low=0,high=4,mid=2,
    # low=1,high=4,mid=2,
    # low=2,high=4,mid=3
