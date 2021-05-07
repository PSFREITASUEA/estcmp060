import turtle
from turtle import Turtle


def draw_first_square(fibonacci_second_element, render_zoom_factor):
    turtle_pen.forward(fibonacci_second_element * render_zoom_factor)
    turtle_pen.left(90)
    turtle_pen.forward(fibonacci_second_element * render_zoom_factor)
    turtle_pen.left(90)
    turtle_pen.forward(fibonacci_second_element * render_zoom_factor)
    turtle_pen.left(90)
    turtle_pen.forward(fibonacci_second_element * render_zoom_factor)


def fibonacci_rendering(fibonacci_iteration_quantity, render_zoom_factor):
    fibonacci_first_element = 0
    fibonacci_second_element = 1

    turtle_pen.pencolor("blue")

    draw_first_square(fibonacci_second_element, render_zoom_factor)


if __name__ == '__main__':

    zoom_factor: float = 25
    iteration_quantity: int = 1
    turtle_pen_speed: int = 10

    iteration_quantity = int(input('Insira o número de interações (deve ser > 1): '))

    while iteration_quantity < 1:
        iteration_quantity = int(input('Insira o número de interações (deve ser > 1): '))

    print("Série de Fibonacci para :", iteration_quantity, "elements :")
    turtle_pen: Turtle = turtle.Turtle()
    turtle_pen.speed(turtle_pen_speed)
    fibonacci_rendering(iteration_quantity, zoom_factor)
    turtle.done()
