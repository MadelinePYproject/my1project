my_list = [0, 1, 7, 2, 4, 8]
if my_list:
    index_sum = sum([my_list[idx]for idx in range(0, len(my_list),2)])
    result = index_sum * my_list[-1]
print(result)