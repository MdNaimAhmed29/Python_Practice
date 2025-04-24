#String - Strings in Python are sequences of characters enclosed within single(''), double(""), or triple quotes (""" or ''')
#immutable data type, means they cannot be change once created
"""
Single Quotes('')
- typically used for short strings=> n = 'Hello World'
- string itself contains double qoutes=> n = 'Hello "World"'
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
print(slicing[::-2])
print(slicing[::2])

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
print(text.swapcase())

newtext = text.replace("Ostad", "Naim")
print(newtext)

text = "      hello naim. how are you?       "
print(text.strip())

Text = " Md Naim Ahmed Nobel "
print(Text.count("N"))
result = Text.isdigit()
result2 = Text.isalpha()
print(result)
print(result2)

cleantext = Text.strip().lower()
print(cleantext)


