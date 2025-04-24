#String - Strings in Python are sequences of characters enclosed within single(''), double(""), or triple quotes (""" or ''')
#immutable data type, means they cannot be change once created
"""
Single Quotes('')
- typically used for short strings=> n = 'Hello World'
- string itself contains double qoutes=> n = 'Hello "World"'
"""

"""
Double Quotes("")
- typically used for short or long strings=> n = "Hello World"
- string itself contains single qoutes=> n = "Hello 'World'"
"""

"""
Triple Single Quotes(''')
- typically used for short or long strings=> n = ''' he said, 
                                                     bangladesh is green 
                                                     country'''
- string itself contains double qoutes=> n = ''' he said, 
                                                 "bangladesh" is green 
                                                 country'''
"""

"""
Triple double Quotes
- typically used for short or long strings=> n = Triple double Quotes (he said, 
                                                     bangladesh is green 
                                                     country)Triple double Quotes
- string itself contains single qoutes=> n = Triple double Quotes( he said, 
                                                 'bangladesh' is green 
                                                 country double quote)Triple double Quotes
"""

"""
String indexing
- positive indexing=> n = 'Hello World' - index = 0,1,2,3,4,5,6,7,8,9,10
- negative indexing=> n = 'Hello World' - index = -1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11
"""

"""
String Slicing
-start=> n = 'Hello World' - [0:3] = Hel, [:4] = Hell(if don't mention start index it automatically start from [0] index)
-stop=> n = 'Hello World' - [6:] = Hel, [6:] = World(if don't mention start index it start from index [6] automatically print till end )
-step=> n = 'Hello World' - [0::2] = HloWrd(from index[0-10] every time print it skip 2 character), [::-2] = from index[-1 to -11] every time it skip 2 character when print
"""

"""
String Repetation
- n= "Naim" => repeat=n * 5 => it's repeat 5 times like this(Naim Naim Naim Naim Naim)
"""

"""
String Repetation
- n= "Naim" => repeat=n * 5 => it's repeat 5 times like this(Naim Naim Naim Naim Naim)
"""

"""
String Concatenation - means combine one string with another one
- Using the + Operator => str1 = "Naim", str2 = "Ahmed", combine = str1+" "+str2 = Naim Ahmed
- Using join() method => str1 = "Naim", str2 = "Ahmed", combine = " ".join([str1,str2]) = Naim Ahmed
- Using format() method => str1 = "Naim", str2 = "Ahmed", combine = "{} {} ".format(str1, str2) = Naim Ahmed
- Using %(modulas) formating => str1 = "Naim", str2 = "Ahmed", combine = "%s %s "%(str1, str2) = Naim Ahmed
- Using formatted string/ (f) string => str1 = "Naim", str2 = "Ahmed", combine = f"{str1} {str2}" = Naim Ahmed
"""

"""
String Methods
- convert to uppercase => name = "Naim Ahmed" = text.upper() = NAIM AHMED
- convert to lowercase => name = "Naim Ahmed" = text.lower() = naim ahmed
- capitalize the first letter => name = "naim ahmed" = text.capitalize() = Naim ahmed
- title case(capitalize first letter of each word) => name = "naim ahmed" = text.title() = Naim Ahmed
- swap case (invert case of each letter) => name = "Naim Ahmed" = text.swapcase() = nAIM aHMED
- replace a substring => name = "Naim Ahmed" = text.replace("Naim", "Nobel") = Nobel Ahmed
- split the string into a list => name = "Naim Ahmed" = text.split("delimiter") = ['Naim', 'Ahmed']
- join a list into a string => name = ["Naim", "Ahmed"] = "delimiter".join(text) = Naim Ahmed
- strip whitespace from both ends => text = "      hello naim. how are you?       " = text.strip() = hello naim. how are you?
- remove leading and trailing whitespace => text = "      hello naim. how are you?       " = text.lstrip() = hello naim. how are you?       
                                                                                           = text.rstrip() =       hello naim. how are you?
- Check if string starts with a substring => text.startswith()
- check if string ends with a substring => text.endswith()
- find the positions of a substring => text.find()
- count occurrences of a substring => text.count()
- check if all characters are alphanumeric => text.isalnum()
- check if all characters are alphabetic => text.isalpha()
- check if all characters are digits => text.isdigit()
- check if the string contains only whitespace => text.isspace()
- check if the string is titlecased => text.istitle()
- remove extra space and converting to uppercase => text.strip().upper()
"""



name = "Naim Ahmed"
city = "Dhaka"

print(name)
print(city)

text = "I am 'bangladeshi'"
print(text)

text = 'I am "bangladeshi"'
print(text)

triple_quoted_text = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries,'''
print(triple_quoted_text)

slicing = "python i love"
print(slicing[0])
print(slicing[-1])
print(slicing[0:6])
print(slicing[0:])
print(slicing[:6])
print(slicing[-1::-2])
print(slicing[0::2])

fname = "Naim"
lname = "Ahmed"

fullname = fname + " " + lname
print(fullname)

fullname = f"{fname} {lname}"
print(fullname)

fullname = "{} {}".format(fname, lname)
print(fullname)

fullname = "%s %s" % (fname, lname)
print(fullname)

text = "Ostad On Going "
print(text * 10)
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.split(" "))
print("".join(text))
print(text.swapcase())

newtext = text.replace("Ostad", "Naim")
print(newtext)

text = "      hello naim. how are you?       "
print(text.strip())

text = "  Md Naim Ahmed Nobel  "
print(text.count("N"))
result = text.isdigit()
result2 = text.isalpha()
result3 = text.islower()
result4 = text.isupper()
result5 = text.isalnum()
result6 = text.isspace()
result7 = text.isnumeric()
result8 = text.istitle()
result9 = text.startswith("Md")
result10 = text.endswith("Nobel")
result11 = text.find("Ahmed")


print(result)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)

cleantext = text.strip().upper()
print(cleantext)


