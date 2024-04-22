# def my_function():
#     print("I'm a function")
#     print("I'm still a function")
#     return "I'm done"

# message = my_function()
# print("The output from the function is", message)

def area_rectangle():
    rect_length = 10
    rect_width = 5

    rect_area = rect_length * rect_width
    print("Area of the Rectangle", rect_area)

def area_circle():
    circle_radius = 12
    pi = 3.14159

    circle_area = pi * circle_radius ** 2
    print("Area of the Circle", circle_area)

area_rectangle()
area_circle()
