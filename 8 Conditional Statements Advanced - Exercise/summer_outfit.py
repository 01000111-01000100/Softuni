grade = int(input())
time_of_day = input()

if 10 <= grade <= 18:
    if time_of_day == "Morning":
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif time_of_day == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
elif 18 < grade <= 24:
    if time_of_day == "Morning":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
elif grade >= 25:
    if time_of_day == "Morning":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif time_of_day == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    elif time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

print(f"It's {grade} degrees, get your {Outfit} and {Shoes}.")