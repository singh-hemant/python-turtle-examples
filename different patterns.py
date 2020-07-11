import turtle
from random import randint

def get_input_angle():
    value = input("Please provide an angle: ")
    while not value.isnumeric():
        print("The input must be integer...")
        value = input("Please provide an angle: ")
    return int(value)

def generate_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

print("Setup Screen")
turtle.title("Colorful patterns")
turtle.setup(640, 600)
turtle.hideturtle()
turtle.bgcolor('black')
turtle.colormode(255)
turtle.speed(10)

angle = get_input_angle()

print("Start the drawing")

for i in range(0, 200):
    turtle.color(generate_random_color())
    turtle.forward(i)
    turtle.right(angle)

print("Done")
turtle.done()
