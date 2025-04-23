print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")

print(3 + 5)
print(3 - 5)
print(3 * 5)
print(3 / 5)
print(3 % 5)
print(3 ** 5)
print(3 // 5)

num = 5
print(num , type(num))

print(1, 2, 3)

for i in range(10):
    print("*" * (i+1))

num1 = input("Enter a number: ")
num1 = int(num1)

if num1 % 2 == 0:
    print(num1, "is even")
else:
    print(num1, "is odd")

for i in range(11):
    print(i)

for i in range(1, 11, 3):
    print(i)

for i in range(10, 0, -1):
    print(i)

def add_3(n):
    return n + 3

x = 5
y = add_3(x)
print(x , y)

def greetings():
    print("Hello!")

greetings()

def greetings(name):
    print("Hello,", name)

greetings("Naim")
greetings("Eshan")
greetings("Sidhan")

z = 3.14159265358
z = round(z, 4)
print(z)

def greetings(name):
    print("Hello,", name)

n = input()
greetings(n)

country = "Bangladesh"
for c in country:
    print(c)

print(country[0])

import math

pi = math.pi

print(math.pi)

h = 16
r = math.sqrt(h)
print(r)

k = 5
for i in range(1, 11):
    print(k, "x", i, "=", k * i)

j = input()
j = int(j)
for i in range(1, 11):
    print(j, "x", i, "=", j * i)

def print_multiplication_table(l):
    for i in range (1,11):
        print(l, "x", i, "=", l * i)

l = input()
l = int(l)

print_multiplication_table(l)