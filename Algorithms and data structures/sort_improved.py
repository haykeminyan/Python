def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)-1):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


print(selection_sort([4, 5, 64, 34, 52]))


def bubble_sort(values):
    n = 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(values)-n):
            if values[i] > values[i+1]:
                values[i], values[i+1] = values[i+1], values[i]
                is_sorted = False
        n += 1
    return values


print(bubble_sort([5, 54, 32, 12, 10, 6]))
