length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage = float(input())
water_liter = 1
percentage_sum = percentage / 100
volume_needed_sum = length_cm * width_cm * height_cm
volume_needed_sum_liter = volume_needed_sum * 0.001
total_sum = volume_needed_sum_liter * (water_liter - percentage_sum)
print(total_sum)