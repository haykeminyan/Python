def linear_search(list_arr, target):
    for i,j in enumerate(list_arr):
        if j == target:
            return i
    return -1    

print(linear_search([1,2,3,4,5],32))
print(linear_search([3,2,1,43,2],43))
