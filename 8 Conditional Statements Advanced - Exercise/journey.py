budget = float(input())
season = input()
place = ''
holiday = ''
if budget <= 100:
    place = 'Bulgaria'
    if season == 'summer':
        budget *= 0.30
        holiday = 'Camp'
    elif season == 'winter':
        budget *= 0.70
        holiday = 'Hotel'
elif budget <= 1000:
    place = 'Balkans'
    if season == 'summer':
        budget *= 0.4
        holiday = 'Camp'
    elif season == 'winter':
        budget *= 0.80
        holiday = 'Hotel'
elif budget > 1000:
    budget *= 0.90
    place = 'Europe'
    holiday = 'Hotel'
print(f"Somewhere in {place}")
print(f"{holiday} - {budget:.2f}")