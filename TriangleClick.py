import turtle


def draw_triangle(x_axis_coordinate, y_axis_coordinate):
    turtle_pen.penup()
    turtle_pen.goto(x_axis_coordinate, y_axis_coordinate)
    turtle.pendown()


if __name__ == '__main__':
    turtle_screen = turtle.Screen()
    turtle_pen = turtle.Turtle()
    turtle.onscreenclick(draw_triangle, 1)
    turtle.listen()
    turtle.done()
