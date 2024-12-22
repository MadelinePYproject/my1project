user_number = int(input("Vvod: "))
while user_number > 9:
    chislo = 1
    for digit in str(user_number):
        chislo *= int(digit)
    user_number = chislo
print(user_number)