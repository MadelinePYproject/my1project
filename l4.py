my_list = [1, 0, 23, 0, 0, 6, 0, 7]
result = [i for i in my_list if i != 0 ] + [0] * my_list.count(0)
print(result)

my_list = [0, 1, 7, 2, 4, 8]
if my_list:
    index_sum = sum([my_list[idx]for idx in range(0, len(my_list),2)])
    result = index_sum * my_list[-1]
print(result)

import random
list1 = [random.randint(0,100) for i in range(random.randint(3, 10))]
list2 = list((list1[0], list1[2], list1[-2]))
print('list1', list1)
print('list2', list2)