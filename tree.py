import turtle

def draw_sqare(t, size):
    t.begin_fill()
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.fillcolor("green")
    t.end_fill()


def draw_branch(t, angle, n, pen_size):
    if n < 1:
        return
    if n <= 10:
        draw_sqare(t, 10)
        t.color("green")
    else:
        t.color("brown")
    t.pensize(pen_size)
    t.forward(n)
    t.left(angle)
    draw_branch(t, angle-1, n-12, pen_size-1)
    t.right(2*angle)
    draw_branch(t, angle-1, n-12, pen_size-1)
    if n > 10:
        t.color("brown")
    t.left(angle)
    t.backward(n)


def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(100)
    t.penup()
    t.goto(0, -100)
    t.left(90)
    t.pendown()

    angle = 30
    n = 90
    pen_size = 10
    draw_branch(t, angle, n, pen_size)
    screen.exitonclick()


if __name__ == "__main__":
    main()