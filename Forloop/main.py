fruits = ["Apple", "Banana", "Cherry", "Mango"]

for fruit in fruits:
    print(fruit)

#term two

for i in range(4):
    print(i, fruits[i])

#term three
for i in range(0, 10):
    print(i)

#term four
for i in range(0, 10, 2):
    print(i)

#use loop
def generate_multiplication_table(n):
    print(n, "x 1 =", n * 1)
    print(n, "x 2 =", n * 2)
    print(n, "x 3 =", n * 3)
    print(n, "x 4 =", n * 4)
    print(n, "x 5 =", n * 5)
    print(n, "x 6 =", n * 6)
    print(n, "x 7 =", n * 7)
    print(n, "x 8 =", n * 8)
    print(n, "x 9 =", n * 9)
    print(n, "x 10 =", n * 10)

n = input("Enter n: ")
n = int(n)

for i in range(1, n+1):
    generate_multiplication_table(i)
    print("")

#for loop use two
def multplication_table(n):
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, i * n))

n = input("Enter n: ")
n = int(n)
multplication_table(n)
