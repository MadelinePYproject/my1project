import string
def generate_hashtag(text):
    if not text.strip():
        return None
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    words = clean_text.split()


    if not words:
        return None


    hashtag = '#' + ''.join(word.capitalize() for word in words)
    return hashtag[:140]
print(generate_hashtag('Python Community'))  # #PythonCommunity
print(generate_hashtag('i like python community!'))  # #ILikePythonCommunity
print(generate_hashtag('Should, I. subscribe? Yes!'))  # #ShouldISubscribeYes



while True:

    num_1 = float(input("Ввести число: "))
    num_2 = float(input("Ввести число: "))
    operation = input("Ввести действие(+, -, *, /) ")
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
    continue_calc = input("Бажаєте продовжити? (y/n): ").lower()
    if continue_calc != "y":
        print("Thx for using me, BB!")
        break