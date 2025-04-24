#Number
"""
Operators Order
- (**) = Exponentiation
- (+x, -y, ~z) = Unary plus, Unary Minus, Bitwise not
- (*, /, //(floor division), %, +, -) = General Operators
- (<< , >>) = Bitwise shift
- and(&), or(|), not(!), xor(^) = Bitwise Operators
- ==, !=, >, <, >=, <= = Relational Operators
- is, is not = Identity Operators
- in, not in = Membership Operators
- and, or, not = Logical Operators
----------------------------------------------------------------
Most Uses Operators
+x, -y
*, /, //(floor division), %, +, -
and(&), or(|)
==, !=, >, <, >=, <=

Conversion
- int -> float
- float -> int
- complex
"""

import math

x = 10
y = 20
z = 30
a = 3.1416
b = 10+7j
d = -50.45

result10 = ("Addition ",x + y)
result11 = ("Subtraction ",x - y)
result12 = ("Multiplication ",x * y)
result13 = ("Division ",x / y)
result14 = ("Modulus ",x % y)
result15 = ("Exponentiation ",x ** y)
result16 = ("Floor division ",x // y)
result17 = ("Remainder ",x % y)
result18 = ("Bits ",x % y)
result19 = ("Square ",math.sqrt(x))
result20 = ("Power", math.pow(x, y))
result21 = ("Sin ",math.sin(math.radians(x+y)))
result22 = ("log ",math.log(x))
result23 = ("log10 ",math.log10(x))
result24 = ("factorial ",math.factorial(x))
result25 = ("GCD ",math.gcd(x,y,z))
result26 = ("LCM ",math.lcm(x,y,z))
result27 = math.pi
result28 = ("Constant ", math.e)
result29 = ("Absulate Value ",math.fabs(d))
result30 = ("floor(Positive Value) ",math.floor(a)) #Rounds down to the nearest integer
result31 = ("floor(Negative Value) ",math.floor(d)) #rounds toward negative
result32 = ("Ceiling(Positive Value) ",math.ceil(a)) #Rounds up to the nearest integer
result33 = ("Ceiling(Negative Value) ",math.ceil(d)) #rounds toward positive

print(result10)
print(result11)
print(result12)
print(result13)
print(result14)
print(result15)
print(result16)
print(result17)
print(result18)
print(result19)
print(result20)
print(result21)
print(result22)
print(result23)
print(result24)
print(result25)
print(result26)
print("pi ",round(result27, 4))
print(result28)
print(result29)
print(result30)
print(result31)
print(result32)
print(result33)

print("")

print("Int to Float ", float(x), type(float(x)))
print("Float to Int ", int(a), type(int(a)))
print("Int to Complex ", complex(x), type(complex(x)))
print("Float to Complex ", complex(a), type(complex(a)))
print("Int to String ", str(x), type(str(x)))
print("float to String ", str(a), type(str(a)))
print("Complex to String ", str(b), type(str(b)))

print("")

try:
    print("Complex to int ", int(b), type(int(b)))
    print("Complex to float ", float(b), type(float(b)))
except Exception as error:
    print("Error 1: ", error)

try:
    print("Complex to float ", float(b), type(float(b)))
except Exception as error:
    print("Error 2: ", error)