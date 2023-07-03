# Name: Brittany Zimmerman
# PSID: 2219602
a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

solution = 0
for x in range(-10, 10):
    for y in range(-10, 10):
        if a * x + b * y == c and d * x + e * y == f:
            solution = 1
            print(f'{x} {y}')

if solution == 0:
    print('No solution')
