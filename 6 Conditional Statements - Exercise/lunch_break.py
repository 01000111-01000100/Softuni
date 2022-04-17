import math

name_serial = input()
time_episode = int(input())
time_break = int(input())

time_lunch = time_break * 1 / 8
time_free = time_break * 1 / 4
residue_time = time_break - time_lunch - time_free
if residue_time >= time_episode:
    residue = residue_time - time_episode
    print(f'You have enough time to watch {name_serial} and left with {math.ceil(residue)} minutes free time.')
else:
    residue = abs(residue_time - time_episode)
    print(f"You don't have enough time to watch {name_serial}, you need {math.ceil(residue)} more minutes.")
