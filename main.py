
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


