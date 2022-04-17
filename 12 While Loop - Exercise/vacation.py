money_needed = float(input())
saved_money = float(input())

days = 0
spend_days = 0
amount = 0

while saved_money < money_needed and spend_days < 5:
    command = input()
    amount = float(input())
    days += 1
    if command == 'save':
        saved_money += amount
        spend_days = 0
    if command == 'spend':
        spend_days += 1
        saved_money -= amount
        if saved_money < 0:
            saved_money = 0

    if saved_money >= money_needed:
        print(f'You saved the money for {days} days.')
        break
else:
    print(f'You can\'t save the money.\n{days}')