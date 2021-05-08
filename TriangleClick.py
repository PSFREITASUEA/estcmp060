import turtle


def draw_triangle(x, y):
    print(x, y)


if __name__ == '__main__':
    turtle_screen = turtle.Screen()
    turtle_pen = turtle.Turtle()
    turtle.onscreenclick(draw_triangle, 1)
    turtle.listen()
    turtle.done()
