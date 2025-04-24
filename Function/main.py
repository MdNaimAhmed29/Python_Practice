def generate_multiplication_table(num):
    print(num, "x 1 =", num * 1)
    print(num, "x 2 =", num * 2)
    print(num, "x 3 =", num * 3)
    print(num, "x 4 =", num * 4)
    print(num, "x 5 =", num * 5)
    print(num, "x 6 =", num * 6)
    print(num, "x 7 =", num * 7)
    print(num, "x 8 =", num * 8)
    print(num, "x 9 =", num * 9)
    print(num, "x 10 =", num * 10)

num = input("Enter a number: ")
num = int(num)
generate_multiplication_table(num)
generate_multiplication_table(num+1)


