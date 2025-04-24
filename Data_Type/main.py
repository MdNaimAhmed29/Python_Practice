#Numeric Data Type

age = 34 #integer
print(type(age),age)

marks = 85.6 #float
print(type(marks),marks)

complex_numbers = 3.14+20j #complex
print(type(complex_numbers),complex_numbers)

#String Data Type

name = "MD. NAIM AHMED" #string
print(type(name),name)

#Sequance Data Type

cities = ["dhaka", "savar", "Manikganj"]#list-mutable-order types data
num = [10, 20.5, "age"]
print(type(num),num)
print(type(cities),cities)

numbers = ("A", "B", "C") #tuples-immutable
letter = ("A", "B", 2, 3, 2.2)
print(type(letter),letter)
print(type(numbers),numbers)

n = range(1,10, 2)
print(type(n), *n)

# Boolean Data Type

isNaim = True #boolean
print(type(isNaim),isNaim)

# None Data Type

taka = None #none
print(type(taka),taka)

# Mapping Data type
#dictionary
person = {
    'first_name':'Naim',
    'last_name':'Ahmed',
    'age':29,
    'isBangladeshi':True
}
print(type(person), person)
print(type(person['first_name']), person['first_name'])

#Set Data Types

unique_num = {1, 2, 3, 4, 5} #set-mutable-unorder types data
unique_num2 = {1, 2, 3, 4, 5, 1, 3, 4}
print(type(unique_num2), unique_num2)
print(type(unique_num), unique_num)

unique_num3 = frozenset([1, 2, 3, 4, 5]) #frozenset-immutable
unique_num4 = frozenset([1, 2, 3, 4, 5, 1, 3, 4])
print(type(unique_num3), unique_num3)
print(type(unique_num4), unique_num4)

#immutable data type
#immutable objects cannot be modified after their creation
"""
-integers
-floating point numbers
-string
-tuples
-frozensets
"""

a = 5 #integer
initial_firstID = id(a)

a = 6
initial_secondID = id(a)

print(initial_firstID, initial_secondID)

b = 5.50 #floating point numbers
initial_firstID = id(b)

b = 6.35
initial_secondID = id(b)

print(initial_firstID, initial_secondID)

c = "Naim" #string
initial_firstID = id(c)

c = "Ahmed"
initial_secondID = id(c)

print(initial_firstID, initial_secondID)

d = (1, 2, 3, 4) #tuples
initial_firstID = id(d)

d = (5, 6, 7, 8)
initial_secondID = id(d)

print(initial_firstID, initial_secondID)

e = frozenset([1, 2, 3, 4]) #frozensets
initial_firstID = id(e)

e = ([5, 6, 7, 8])
initial_secondID = id(e)

print(initial_firstID, initial_secondID)

#mutable data types
#immutable objects can be modified after their creation
"""
-Lists
-Dictonaries
-Sets
"""

l = [1, 2, 3, 4] #lists
firstID = id(l)
print(firstID)

l[1]=6
secondID = id(l)
print(secondID)

i = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e} #dictonaries
first = id(i)
print(first)

i['A'] = 5
second = id(i)
print(second)

j = {1, 2, 3} #sets
frs = id(j)
print(frs)

j.add(4)
secd = id(j)
print(secd)

#data type conversion
"""
-explicit=>using python method conversion
-implicit=>automatic converted
some data not conversionable like this name = "Naim"
print this type of error use try and exception
"""

x = '123' #explicit
y = int(x)
z = float(x)
w = complex(x)
print(type(x), x)
print(type(y), y)
print(type(z), z)
print(type(w), w)

k = 10 #implicit
g = 5.5
u = k + g
print(type(u), u)

try:
    name = "Naim"
    o = int(name)
    print(type(o), o)
except Exception as p:
    print(p)




