excursion_price = float(input())

puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

price_puzzles = 2.60
price_dolls = 3
price_teddy_bears = 4.10
price_minions = 8.20
price_trucks = 2

total_quantity = puzzles + dolls + teddy_bears + minions + trucks
price_toys = (puzzles * price_puzzles) + (dolls * price_dolls) + (teddy_bears * price_teddy_bears) + (
        minions * price_minions) + (trucks * price_trucks)

rent_price = price_toys * 0.1
earned_money = price_toys - rent_price

if total_quantity >= 50:
    discount = price_toys * 0.25
else:
    discount = 0

total_price = price_toys - discount
rent_price = total_price * 0.1
earned_money = total_price - rent_price
money_left = abs(earned_money - excursion_price)

if earned_money >= excursion_price:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f'Not enough money! {needed_money:.2f} lv needed.')
