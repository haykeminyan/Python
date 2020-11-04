def linear_search(list_arr, target):
    res = []
    for i,j in enumerate(list_arr):
        if j == target:
            res.append(i)
    if len(res) >= 1:
        return res
    return -1

print(linear_search([1,2,3,3,3],5))
