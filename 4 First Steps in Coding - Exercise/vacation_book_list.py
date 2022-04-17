number_pages = int(input())
pages_per_hour = int(input())
number_days = int(input())
hours = number_pages / pages_per_hour
hours_per_day = hours / number_days
print(int(hours_per_day))