app1 = 'Jira'
app2 = 'Confluence'
app3 = 'Crowd'

list = [1,'Samuel','pastor',1]
set = {'1','Samuel','pastor',1,1,1}     # no-duplicates
tuple = (1,1,1,3,4,5,7,9)               # immutable

print(f"list: {list}")
print(f"set: {set}")
print(f"tuple: {tuple}")

print(type(list[0]))        # type
print(list[-1])             # print last
print(list[:2])             # pint first two (index 0 and 1)
print(list)

list.append("JanDupa")      # add new element to the end
print(list)

list.insert(0,2)            # change element[0] from 1 to 2
print(list)

list2 = [1,10,7,9,3,2,2,8,1,1,8,9,0]
print(f"lista nieposortowana {list2}")
list2.sort()
print(f"lista posortowana {list2}")


print(str(50))              # enforce int 50 will be string


# print("Atlassian stack: " + app1 + ", " + app2 + " and " + app3)

# user_input = input("Hey, napisz cos\n")
# input()
# user_input.split(";")
# print(user_input)




# Using escape characters to include special characters within a string
escaped_string = "This is a \"quoted\" string."
print(escaped_string)

# Another example with newline and tab escape characters
multiline_string = "First line\nSecond line\n\tIndented line"
print(multiline_string)
