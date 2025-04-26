from calendar import weekday
from datetime import date

current_temp = input("Please enter current temperature: ")
reference_temp = input("Please enter reference temperature: ")

current_temp = float(current_temp)
reference_temp = float(reference_temp)

result1 = (current_temp > reference_temp)

print(result1)

if result1 == True:
    print("current temperature is", current_temp, "(Warm)")
elif result1 == (current_temp == reference_temp):
    print("current temperature is", current_temp, "(Normal)")
elif result1 == (current_temp < reference_temp):
    print("current temperature is", current_temp, "(Normal)")
else:
    print("current temperature is", current_temp, "(Normal)")


today = input("Enter the Day: ")
public_holiday = input("Is it public holiday? Y/N: ")
is_sick_today = input("Is sick today? Y/N: ")
print(today)

if today == "Friday" or today == "Saturday" or public_holiday == "Y" or is_sick_today == "Y":
    print("No office today")
else:
    print("I have to go to office today")




def meet_requirments(price, brand, color, milege):

    budget = input("Please enter budget: ")
    my_brand = input("Please enter brand: ")
    my_color = input("Please enter colors: ")
    max_milege = input("Please enter max mileage: ")

    budget = float(budget)
    max_milege = float(max_milege)

    if (price <= budget and brand == my_brand and color == my_color and milege <= max_milege) or (price <= budget // 2 and max_milege < milege <= max_milege):
        return True
    else:
        return False


price = input("what is the asking price? ")
price = int(price)
brand = input("What is the brand? ")
color = input("What is the color? ")
milege = input("What is the mileage? ")
milege = int(milege)

if meet_requirments(price, brand, color, milege):
    print("Yes, I can consider this car")
else:
    print("Sorry, This car doesn't match my criteria.")





