num = input("Enter a number: ")
num = int(num)

if num >= 0:
    if num % 2 == 0:
        print(num, "is Positive and is an even number.")
    else:
        print(num, "is Negative and is an Odd number.")

else:
    if num % 2 == 0:
        print(num, "is Negative and is an even number.")
    else:
        print(num, "is Negative and is an Odd number.")

#Two terms

if num >= 0 and num % 2 == 0:
    print(num, "is Positive and is an even number.")

elif num >= 0 and num % 2 !=0:
    print(num, "is Positive and is an odd number.")

elif num < 0 and num % 2 == 0:
    print(num, "is Negative and is an even number.")

else:
    print(num, "is Negative and is an Odd number.")

