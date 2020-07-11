import turtle
turtle.title("My turtle drawing!!!")
turtle.setup(width=900, height=700, startx=0, starty=0)

turtle.pencolor('red')
turtle.speed(1)
#turtle.hideturtle()


def draw_square(size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)

def draw_octagon(size):
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size)

def draw_hexagon(size):
##    turtle.penup()
##    turtle.setx(x)
##    turtle.sety(y)
##    turtle.pendown()
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.right(60)

    
##for _ in range(12):
##    draw_square(50)
##    turtle.right(120)

#draw_octagon(50)

for _ in range(6):
    draw_hexagon(60)
    turtle.forward(60)
    turtle.left(60)

#draw_hexagon(100, 100, 60)

turtle.exitonclick()
