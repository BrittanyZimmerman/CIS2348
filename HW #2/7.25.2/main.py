def exact_change(val):

    num_dollar = (val // 100)
    val %= 100
    num_quarter = (val // 25)
    val %= 25
    num_dime = (val // 10)
    val %= 10
    num_nickel = (val // 5)
    val %= 5
    num_pennie = val

    return num_dollar, num_quarter, num_dime, num_nickel, num_pennie


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if input_val >= 1:

        if num_dollars > 1:
            print(f'{num_dollars} dollars')
        elif num_dollars == 1:
            print(f'{num_dollars} dollar')

        if num_quarters > 1:
            print(f'{num_quarters} quarters')
        elif num_quarters == 1:
            print(f'{num_quarters} quarter')

        if num_dimes > 1:
            print(f'{num_dimes} dimes')
        elif num_dimes == 1:
            print(f'{num_dimes} dime')

        if num_nickels > 1:
            print(f'{num_nickels} nickels')
        elif num_nickels == 1:
            print(f'{num_nickels} nickel')

        if num_pennies > 1:
            print(f'{num_pennies} pennies')
        elif num_pennies == 1:
            print(f'{num_pennies} penny')
    else:
        print('no change')
