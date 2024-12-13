# num1 = int(input("Vvedite chislo : "))
# num2 = int(input("Vvedite chislo : "))
# num1 -= 3
# print('Result', num1 + num2)
# print('Result', num1 - num2)
# print('Result', num1 * num2)
# print('Result', num1 / num2)
# from itertools import count
#
# from l3 import result
import random

from l4 import my_list

# word = "Hi"
# print(word * 2)

# print(any([2 > 2, True, 5 < 5]))
# first_list = [2, 4, 7, 11 , '0', -2, 8]
# max(first_list)
# n = 1 # присвоюємо початкове значення змінній n
# while n <= 10: # запускаємо цикл при умові n <= 10
# 	print(n) # друкуємо значення n
# 	n = n + 1 # збільшуємо значення n на 1
# print('End')

# number = 0
# while number <= 10:
#     number = number + 2
#     if number == 6:
#         break
#     print(number)



# number = 0
# while True:
#     number = number + 1
#     if number == 5:
#         continue
#     if number == 35:
#         break
#     print(number)

# number = int(input("vvedite positive chislo: "))
# i = 2
# while i < number:
#     if number % i == -1:
#         print("Eto ne prime chislo")
#         break
#     i = i +1
# else:
#     print("eto prime chislo")

# a = int(input('Input a '))
# b = int(input('Input b '))
# i = 0
# while i < a:
#     j = 0
#     while j < b:
#         print('*', end= '')
#         j += 1
#     print()
#     i += 1

# first_list = [[1, 2, 3], [4, 5, 5]]
# i = 0
# while i < len(first_list):
#     j = 0
#     lst = first_list[i]
#     while j < len(lst):
#         print((lst[j]))
#         j += 1
#     i += 1

# print("Hello", "world", sep="!")

# for i in range(1,24):
#     if i < 24:
#         end = "-"
#     else:
#         end = "\n"
#     print(i, end=end)

# lst = [4, 5, 6, 6]
# i = 0
# while i < len(lst):
#     l = lst[i]
#     print(l)
#     i += 1

# lst = [4, 6, 8, 10]
# for l in lst:
#     print(l)

# first_list = [[1, 2, 3], [4, 5, 6]]
# for lst in first_list:
#     for j in lst:
#         print(j)

# lst = [4, 5, 6, 6]
# for i, el in enumerate(lst):
#     print(i,"->", el)


# r = range(1, 10, 1)
# for i in r:
#      print(i)


 # import random
 # my_list =[]
 # for i in range(random.randint(1, 10)):
 #     my_list.append((random.randint(1, 100)))
 #     print(my_list)


# for i in range(6):
#     print(i)
# word = "Hello world!"
# for i in word:
#     if i == "!":
#         print('Yes')


# count = 0
# word = 'hello world'
# for i in word:
#     if i == 'o':
#         count += 1
#         print('Count:', count)

# i = 33
# while i <= 999:
#     print(i)
#     i += 111

# isMyCar = True
# while isMyCar:
#     if input('vvedite chet :') == 'STOP':
#         isMyCar = False

# for i in range(1, 11,):
#     if i == 7:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)


# import random
# list1 = [random.randint(0,100) for i in range(random.randint(3, 10))]
# list2 = [list1[0]],[list1[2]],[list1[-2]]
# print('list1', list1)
# print('list2', list2)

my_list = [0, 1, 7, 2, 4, 8]
if my_list:
    index_sum = sum([my_list[idx]for idx in range(0, len(my_list),2)])
    result = index_sum * my_list[-1]
else:
    result = 0
print(result)