total_steps = 10000
made_steps = 0

while True:
    steps = input()
    if steps.isnumeric():
        made_steps += int(steps)
        if made_steps >= total_steps:
            break
    else:
        made_steps += int(input())
        break

if made_steps >= total_steps:
    print('Goal reached! Good job!')
    print(f'{abs(total_steps - made_steps)} steps over the goal!')
else:
    print(f'{total_steps - made_steps} more steps to reach goal.')