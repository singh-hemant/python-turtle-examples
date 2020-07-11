import turtle
import math

def draw_spiral(t, r):
    if r == 500:
        return
    if r % 3 == 0:
        t.color("blue")
    elif r % 5 == 0:
        t.color("orange")
    elif r % 2 == 0:
        t.color("green")
    else:
        t.color("red")

    x = r*math.cos(1)
    y = r*math.sin(1)
    t.circle(r, 45)
    draw_spiral(t, r+1)


def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(100)
    t.penup()
    t.goto(0, 0)
    t.left(90)
    t.pendown()
    t.pensize(5)


    radius = 10

    draw_spiral(t, radius)

    screen.mainloop()

def trial():
    tt = turtle.Turtle()
    for i in range(100):
        tt.circle(10+i, 45)


if __name__ == "__main__":
    main()
    #trial()
