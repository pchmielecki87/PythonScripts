print("zad 1")
print(4/2-2**1)
print(4/2+2**1)
print(1//2+3*4)
print(1**2-4//3)


# print("zad 2")
# power = 1
# while power != 10:
#     power *= 2
#     if power == 5:
#         continue
#     print("@", end="")
# else:
#     print("@")
# ENDLESS LOOP


print("zad 3")
others = -1
for i in range(1,3):
    for j in range(1,2):
        if i == j:
            others += 1
    else:
        others += 1
print(others)


print("zad 4")
planets = 1+1//2*3
if planets > 0:
    print("#")
elif planets > 1:
    print("##")
else:
    print("###")


print("zad 5")
torque = 1
while torque < 2:
    torque *= 2
    print("*", end="")
else:
    print("*")



print("zad 6")
angle = 1
for i in range(2,5):
    if 2*i > 4:
        angle += 1
else:
    angle -= 1
print(angle)


print("zad 7")
answers = (True, False, True)
selection = answers[2:]
points = 0
for answer in selection[-1:]:
    if answer:
        points += 1
print(points)


#####################################################
print("zad 8")
the_data = ['data', -1, 2.71111]
print("")
#####################################################


print("zad 9")
train_speed = {"X": 201, "Y": 320, "Z": 320}
for train in train_speed.values():
    print(str(train)[0], end="")


print("zad 10")
list_one = [1,2]
list_two = list_one
list_two.append(3)
print(list_one[-1])


print("zad 11")
def combine(width, height=10, depth=0, is_3D=False):
    return [is_3D, width, height, depth]
print(combine(height=1, width=2)[3])


print("zad 12")
def walk(top):
    if top == 0:
        return 0
    return top + walk(top - 1)
print(walk(2))


# print("zad 13")
# def sample(value):
#     return total + value
# # MISSING VALUE

# total = 0
# new_total = sample()
# new_total = sample(total)
# print(total)


print("zad 14")
try:
    character = "ABC"[3]
except IndexError:
    print("Mshit")
except:
    print("Failure")




print("zad 15")
def process(data):
    data[1] = 2
    return data[-2]

measurements = [0 for i in range(3)]
process(measurements)
print(measurements[-2])