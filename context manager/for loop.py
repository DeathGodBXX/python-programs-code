from itertools import product

list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
for i, j, k in product(list1, list2, list3):
    print(i + j + k)

