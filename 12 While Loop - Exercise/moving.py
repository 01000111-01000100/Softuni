width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height
is_full = False
command = input()
while command != "Done":
    box = int(command)
    free_space -= box
    if free_space < 0:
        is_full = True
        break
    command = input()
if is_full:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
else:
    print(f"{abs(free_space)} Cubic meters left.")