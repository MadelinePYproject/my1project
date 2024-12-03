num = input("Введіть 4-х значне число")
num = int(num)
print(num // 1000)
print(num // 100 % 10)
print(num // 10 % 10)
print(num % 10)


number = int(input("5 значне число"))

reversed_number = 0
reversed_number += (number % 10) * 10000
number = number // 10
reversed_number += (number % 10) * 1000
number = number // 10
reversed_number += (number % 10) * 100
number = number // 10
reversed_number += (number % 10) * 10
number = number // 10

reversed_number += number % 10
print(reversed_number)