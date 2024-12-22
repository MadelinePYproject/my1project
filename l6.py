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

def conver_seconds(seconds):
    if seconds < 0 or seconds > 8640000:
        return "shos pishlo ne tydu"
    seconds_per_minute = 60
    seconds_per_hour = 3600
    seconds_per_day = 86400
    days, seconds = divmod(seconds, seconds_per_day)
    hour, seconds = divmod(seconds, seconds_per_hour)
    minutes, seconds = divmod(seconds, seconds_per_minute)
    return f"{days} {'День' if days == 1 else 'Дней'},{str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
user_input = int(input("Vvedite kl-vo secund : "))
print(conver_seconds(user_input))

user_number = int(input("Vvod: "))
while user_number > 9:
    chislo = 1
    for digit in str(user_number):
        chislo *= int(digit)
    user_number = chislo
print(user_number)