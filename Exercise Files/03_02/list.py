countries = [
    "Brazil",  # 0
    "Denmark", # 1 
    "Canada",  # 2
]

countries.append("Estonia")
countries.insert(2, "Argentina")
countries.append("Belice")
countries.append("Zambia")
# countries.remove("Canada")
# brazil = countries.pop(1)
countries.sort(reverse=True)

print(countries)