# Name: Brittany Zimmerman
# PSID: 2219602

input_val = str(input())
empty = ''
split_space = input_val.split(' ')
no_space = empty.join(split_space)

reverse_input = no_space[::-1]

if reverse_input == no_space:
    print(f'{input_val} is a palindrome')
else:
    print(f'{input_val} is not a palindrome')
