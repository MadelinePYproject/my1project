num_1 = float(input("Ввести число"))
num_2 = float(input("Ввести число"))
operation = input("Ввести действие(+, -, *, /)")
if operation == "+" :
    result = num_1 + num_2
    print("Результат:", result)
elif  operation == "-":
    result = num_1 - num_2
    print("Результат:", result)
elif operation == "*" :
    result = num_1 * num_2
    print("Результат:", result)
elif operation == "/" :
    if num_2 == 0 :
        print("Ошибочка:")
    else:
        result = num_1 / num_2
        print("Результат:", result)
else:
    print("Корявая операция")

my_list = [1, 2, 22, 33, 4]
my_list = [my_list[-1]] + my_list[:-1]
print(my_list)



my_list = []

if len(my_list) == 0:
    result = [[], []]

else:
    x = (len(my_list) + 1) // 2

    part1 = my_list[:x]
    part2 = my_list[x:]
    result = [part1, part2]

print(result)
 # [22, 11, 11, 6, 5, 6, 2, 1] => [[22, 11, 11, 6], [5, 6, 2, 1]]
 # [2, 3, 6 ,8 ,9] => [[2, 3, 6], [8, 9]]
 # [] => [[], []]
