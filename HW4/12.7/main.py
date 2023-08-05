# Brittany Zimmerman
# 2219602

def get_age():
        age = int(input())
        if age < 18 or age > 75:
            raise ValueError('Invalid age.')

        return age


def fat_burning_heart_rate(age):
    heart_rate = float(.70 * (220-age))
    return heart_rate

if __name__ == "__main__":


    try:
        age = get_age()
        if age < 18 or age > 75:
            raise ValueError
        else:
            print(f'Fat burning heart rate for a {age} year-old: {fat_burning_heart_rate(age):.1f} bpm')

    except ValueError as error:
        print(error)
        print('Could not calculate heart rate info.\n')
