countries = ['Argentina', 'Belice', 'Brazil',
              'Canada', 'Denmark', 'Estonia', 
              'Zambia']

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
comprehension = [e*2 for e in list if e<5]
print("Comprehension", comprehension)

print([c + ":" for c in countries if len(c)>3])
 
matrix = [[0, 1], [2, 3], [4, 5]]
x = matrix[1][0]

# new_countries = countries.copy()
new_countries = list[:]
new_countries.append("New Zealand")

# print(countries)