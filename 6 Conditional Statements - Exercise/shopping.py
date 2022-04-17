budget = float(input())
amount_video_cards = int(input())
amount_processors = int(input())
amount_ram = int(input())

sum_video = amount_video_cards * 250
price_processors = sum_video * 0.35
sum_processors = price_processors * amount_processors
price_ram = sum_video * 0.1
sum_ram = price_ram * amount_ram

total_sum = sum_video + sum_processors + sum_ram
if amount_video_cards > amount_processors:
    discount = total_sum * 0.15
    total_sum -= discount  # total_sum - (total_sum - discount)

needed_money = abs(budget - total_sum)

if budget >= total_sum:
    print(f'You have {needed_money:.2f} leva left!')
else:
    print(f'Not enough money! You need {needed_money:.2f} leva more!')