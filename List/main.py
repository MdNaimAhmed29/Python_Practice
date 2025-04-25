country = ["Bangladesh", "USA", "UK", "UAE"]
print(type(country))
print(country)
print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[-1])
print(country[-2])
print(country[-3])
print(country[-4])

country.append("Canada")
print(country)

print(len(country))

print("USA" in country)
print("Germany" in country)

country.pop()
print(country)

