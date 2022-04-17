width = int(input())
length = int(input())

area = width * length

guests = 0
command = ''

while command != 'stop' and area > 0:
    command = input().lower()
    if command.isnumeric():
        area -= int(command)
    else:
        break

if area > 0:
    print(f'{area} pieces are left.')
else:
    print(f'No more cake left! You need {abs(area)} pieces more.')