# Brittany Zimmerman
# PSID: 2219602
if name == 'main':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickles, num_pennies = exact_change(input_val)

    if input_val <= 0:
        print('no change')

    else:
        if num_dollars > 1:
            print(f'{num_dollars} dollars')
        elif num_dollars == 1:
            print(f'{num_dollars} dollar')
        if num_quarters > 1:
            print(f'{num_quarters} quarters')
        elif num_dollars == 1:
            print(f'{num_quarters} quarter')
        if num_quarters > 1:
            print(f'{num_dimes} dimes')
        elif num_dollars == 1:
            print(f'{num_dimes} dime')
        if num_quarters > 1:
            print(f'{num_nickles} nickles')
        elif num_dollars == 1:
            print(f'{num_nickles} nickle')
        if num_quarters > 1:
            print(f'{num_pennies} pennies')
        elif num_dollars == 1:
            print(f'{num_pennies} pennies')


def exact_change(input_val):

    num_dollars = input_val / 100
    input_val -= (num_dollars * 100)
    num_quarters = input_val / 25
    input_val -= (num_quarters * 25)
    num_dimes = input_val / 10
    input_val -= (num_dimes * 10)
    num_nickles = input_val / 5
    input_val -= (num_nickles * 5)
    num_pennies = input_val
    return num_dollars, num_quarters, num_dimes, num_pennies



