import  string
def get_characters_range(input_str):
        start, end = input_str.split('-')
        all_letters = string.ascii_letters
        start_index = all_letters.index(start)
        end_index = all_letters.index(end)
        return ''.join(all_letters[start_index:end_index+1])

input_data = input("Vvedite diapazon cherez defis: ")
result = get_characters_range(input_data)
print(result)


