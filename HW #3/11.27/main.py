
roster = {}

for player in range(5):
    jer = int(input(f"Enter player {player+1}'s jersey number:\n"))
    rate = int(input(f"Enter player {player+1}'s rating:\n"))
    print()
    roster[jer] = rate

my_keys = list(roster.keys())
my_keys.sort()

print('ROSTER')
for player in my_keys:
    print(f'Jersey number: {player}, Rating: {roster[player]}')

user_inp = ''
print()
while user_inp != 'q':
    print(f'MENU\na - Add player\nd - Remove player\nu - Update player rating\n'
          f'r - Output players above a rating\no - Output roster\nq - Quit\n')
    print('Choose an option:')
    user_inp = str(input())
    user_inp.lower()
    if user_inp == 'o':
        print('ROSTER')
        for player in my_keys:
            print(f'Jersey number: {player}, Rating: {roster[player]}')
        print()
    elif user_inp == 'a':
        jer = int(input(f"Enter new player's jersey number:\n"))
        rate = int(input(f"Enter the player's ratings:\n"))
        roster[jer] = rate
        my_keys = list(roster.keys())
        my_keys.sort()
    elif user_inp == 'd':
        delete = int(input('Enter a jersey number:\n'))
        roster.pop(delete)
        my_keys = list(roster.keys())
        my_keys.sort()
    elif user_inp == 'u':
        update = int(input('Enter a jersey number:\n'))
        new = int(input('Enter a new rating for a player:\n'))
        roster[update] = new
        my_keys = list(roster.keys())
        my_keys.sort()
    elif user_inp == 'r':
        rate_check = int(input('Enter a rating:'))
        print(f'ABOVE {rate_check}')
        my_keys = list(roster.keys())
        my_keys.sort()
        for player in my_keys:
            if roster[player] > rate_check:
                print(f'Jersey number: {player}, Rating: {roster[player]}')
        print()