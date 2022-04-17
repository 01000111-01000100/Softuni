payment = float(input())
payback = int(payment * 100)
coins = 0
run = True

while run:
    if payback - 200 > 0:
        payback -= 200
        coins += 1
    elif payback - 200 == 0:
        coins += 1
        print(coins)
        run = False
    elif payback - 100 > 0:
        payback -= 100
        coins += 1
    elif payback - 100 == 0:
        coins += 1
        print(coins)
        run = False
    elif payback - 50 > 0:
        payback -= 50
        coins += 1
    elif payback - 50 == 0:
        coins += 1
        print(coins)
        run = False
    elif payback - 20 > 0:
        payback -= 20
        coins += 1
    elif payback - 20 == 0:
        coins += 1
        print(coins)
        run = False
    elif payback - 10 > 0:
        payback -= 10
        coins += 1
    elif payback - 10 == 0:
        coins += 1
        print(coins)
        run = False
    elif payback - 5 > 0:
        payback -= 5
        coins += 1
    elif payback - 5 == 0:
        coins += 1
        print(coins)
        run = False
    elif payback - 2 > 0:
        payback -= 2
        coins += 1
    elif payback - 2 == 0:
        coins += 1
        print(coins)
        run = False
    elif payback - 1 > 0:
        payback -= 1
        coins += 1
    elif payback - 1 == 0:
        coins += 1
        print(coins)
        run = False