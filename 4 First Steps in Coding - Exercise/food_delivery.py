chicken_menu = int(input())
fish_menu = int(input())
vegie_menu = int(input())
price_per_chicken_menu = chicken_menu * 10.35
price_per_fish_menu = fish_menu * 12.40
price_per_vegie_menu = vegie_menu * 8.15
total_sum = price_per_chicken_menu + price_per_fish_menu + price_per_vegie_menu
desert = 0.2 * total_sum
delivery = 2.50
total_price = total_sum + desert + delivery
print(total_price)
