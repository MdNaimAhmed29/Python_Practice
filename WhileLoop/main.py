#need start and end point and increment
from operator import index

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


result = 0

"""for i in range(1, 101, 4):
    result = result + i
    print("Result: ", result, "i = ", i)

print(result)"""

i = 1
while i <= 100:
    result = result + i
    i += 4
    print("Result: ", result, "i = ", i)

print(result)


#term two
def add_1_to_n(n):
    result2 = 0
    for x in range(1, n + 1):
        result2 = result2 + x
    return result2

n = input("Enter the number (0 to exit): ")
n = int(n)

while n != 0:
    r = add_1_to_n(n)
    print(r)
    n = input("Enter the number (0 to exit): ")
    n = int(n)


# term three
m = input("Enter the number (0 to exit): ")
m = int(m)
while m != 0:
    k = 0
    for x in range(1, m + 1):
        k = k + x
    print(k)
    m = input("Enter the number (0 to exit): ")
    m = int(m)
#dice calculation
for num1 in range(1, 7):
    for num2 in range(1, 7):
        print("num1: ",num1, "num2: ", num2, "total", num1 + num2)

print("")

#while loop
num3 = 1
while num3 < 7:
    num4 = 1
    while num4 < 7:
        print("num3: ", num3, "num4: ", num4, "total", num3 + num4)
        num4 += 1
    num3 += 1


fruits = ['Apple', 'Banana', 'Mango']

index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

index = 0
end = 10
while index < end:
    if index == 5:
        break
    print(index)
    index += 1

print("")

ind = 0
end = 10
while ind < end:
    if ind == 5:
        ind += 1 #increment index to avoid an infinite loop
        continue
    print(ind)
    ind += 1

examresults = {'phy':90, 'math':89, 'bangla':70} #dictonary
keys = list(examresults.keys())

ind = 0
while ind < len(keys):
    eachkey = keys[ind]
    print(examresults[eachkey])
    ind += 1

