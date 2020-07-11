import turtle
angles = [60, -120, 60, 0]
size_of_snowflake = 300


def get_input_depth():
    massage = "Please provide the depth: "
    value = input(massage)
    while not value.isnumeric():
        print("Input must ne positive integer!!!")
        value = input(massage)
    return int(value)

def setup_screen():
    print("Setup screen")
    turtle.title("koch Snowflake")
    turtle.setup(640, 600)
    turtle.hideturtle()
    turtle.penup()
    turtle.backward(240)
    turtle.tracer(800)
    turtle.bgcolor('white')

def draw_koch(size, depth):
    if depth> 0:
        for angle in angles:
            draw_koch(size/3, depth-1)
            turtle.left(angle)
    else:
        turtle.forward(size)

depth = get_input_depth()
setup_screen()
turtle.color("sky blue")
turtle.penup()
turtle.setposition(-180, 0)
turtle.left(30)
turtle.pendown()

for _ in range(3):
    draw_koch(size_of_snowflake, depth)
    turtle.right(120)

turtle.update()
print("Done")
turtle.done()
