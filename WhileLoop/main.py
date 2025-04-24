i = 1

while i <= 10:
    print(i)
    i += 1

#while loop use
def multiplication_table(n):
    for i in range(1, 11):
        print("{} * {} = {}".format(n, i, n * i))


n = input("Enter the number (0 to exit): ")
n = int(n)

while n != 0:
    multiplication_table(n)
    print("")
    n = input("Enter the number (0 to exit): ")
    n = int(n)