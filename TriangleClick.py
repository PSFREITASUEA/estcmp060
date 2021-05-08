import turtle


def draw_triangle(x_axis_coordinate, y_axis_coordinate):
    turtle_pen.penup()
    turtle_pen.goto(x_axis_coordinate, y_axis_coordinate)
    turtle_pen.pendown()

    for i in range(0, 3):
        turtle_pen.forward(100)
        turtle_pen.left(120)
        turtle_pen.forward(100)


if __name__ == '__main__':
    turtle_screen = turtle.Screen()
    turtle_pen = turtle.Turtle()
    turtle_pen.pencolor("black")
    turtle.onscreenclick(draw_triangle, 1)
    turtle.listen()
    turtle.done()
