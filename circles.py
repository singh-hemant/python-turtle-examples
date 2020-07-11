## circle

import turtle

width = 640
height = 360

def setup():
    turtle.title('circle in my mind')
    turtle.setup(width, height, 0, 0)
    turtle.colormode(255)
    turtle.hideturtle()
    turtle.tracer(2000)
    turtle.speed(10)
    turtle.penup()

def draw_circle(x, y, radius, red=50, green=255, blue=10, width=7):
    color = (red, green, blue)
    if radius > 50:
        if red < 216:
            red = red + 33
            green = green - 42
            blue = blue +10
            width -= 1
        else:
            red = 0
            green = 255
        new_radius = int(radius/1.3)
        draw_circle(int(x+new_radius), y, new_radius, red, green, blue, width)
        draw_circle(int(x-new_radius), y, new_radius, red, green, blue, width)
        draw_circle(x, int(y+new_radius), new_radius, red, green, blue, width)
        draw_circle(x, int(y-new_radius), new_radius, red, green, blue, width)

    turtle.goto(x, y)
    turtle.color(color)
    turtle.width(width)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()

print("Start")
setup()
draw_circle(25, -100, 200)
turtle.update()
print("Done")
turtle.done()
