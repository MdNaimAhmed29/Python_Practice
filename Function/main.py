def generate_multiplication_table(numb):
    print(numb, "x 1 =", numb * 1)
    print(numb, "x 2 =", numb * 2)
    print(numb, "x 3 =", numb * 3)
    print(numb, "x 4 =", numb * 4)
    print(numb, "x 5 =", numb * 5)
    print(numb, "x 6 =", numb * 6)
    print(numb, "x 7 =", numb * 7)
    print(numb, "x 8 =", numb * 8)
    print(numb, "x 9 =", numb * 9)
    print(numb, "x 10 =", numb * 10)

numb = input("Enter a number: ")
numb = int(numb)
generate_multiplication_table(numb)
generate_multiplication_table(numb+1)

numbers = [1, 2, 3, 4, 5]
max_number = max(numbers)

print(max_number)

#linear search

max_num = float('-inf')
for n in numbers:
    if n > max_num:
        max_num = n
print(max_num)

import random

print(dir(random))
print(help(random.randint))
num = []
for _ in range(10):
    num.append(random.randint(1, 100))
    print(num)


def my_function(a, b, c): #paramitar
    a = 5 #local variable
    b = 6
    c = 7
    e = 9
    global d
    d= d*2
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("e = ", e)
    print("d = ", d)
    n = a + b + c

    return n

d = 8 #global variable
x = my_function(1, 2, 3) #arguments
print(x)


