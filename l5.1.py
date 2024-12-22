user_input = input('Vvedite ryadok: ')
variable_name = True
if user_input[0].isdigit():
    variable_name =  False
elif any(char.isupper() for char in user_input):
    variable_name = False
elif "" in user_input:
    variable_name = False
elif any(char in string.punctuation for char in user_input)and "_" not in user_input:
    variable_name = False
elif user_input in keyword.kwlist:
    variable_name = False
elif "__" in user_input:
    variable_name = False
print(variable_name)