deposit = float(input())
months = int(input())
annual_interest_percent = float(input())
annual_interest = deposit * annual_interest_percent /100
mounthly_interest = annual_interest / 12
total_sum = deposit + (months * mounthly_interest)
print(total_sum)
