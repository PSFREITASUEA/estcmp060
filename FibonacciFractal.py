import math
import turtle
from turtle import Turtle


def draw_first_square(
        fibonacci_second_element,
        render_zoom_factor
):
    turtle_pen.forward(fibonacci_second_element * render_zoom_factor)
    turtle_pen.left(90)
    turtle_pen.forward(fibonacci_second_element * render_zoom_factor)
    turtle_pen.left(90)
    turtle_pen.forward(fibonacci_second_element * render_zoom_factor)
    turtle_pen.left(90)
    turtle_pen.forward(fibonacci_second_element * render_zoom_factor)


def fibonacci_rendering(
        fibonacci_iteration_quantity,
        render_zoom_factor
):
    fibonacci_first_element = 0
    fibonacci_second_element = 1
    square_a_size_side = fibonacci_first_element
    square_b_size_side = fibonacci_second_element

    turtle_pen.pencolor("blue")

    draw_first_square(fibonacci_second_element, render_zoom_factor)

    square_a_size_side, square_b_size_side = calculate_fibo(square_a_size_side, square_b_size_side)

    for i in range(1, fibonacci_iteration_quantity):
        draw_square(render_zoom_factor, square_a_size_side, square_b_size_side)
        square_a_size_side, square_b_size_side = calculate_fibo(square_a_size_side, square_b_size_side)

    setup_pen_to_initial_point(render_zoom_factor)

    draw_fibonacci_spiral(fibonacci_first_element, fibonacci_iteration_quantity, fibonacci_second_element,
                          render_zoom_factor)


def draw_fibonacci_spiral(
        fibonacci_first_element,
        fibonacci_iteration_quantity,
        fibonacci_second_element,
        render_zoom_factor
):
    for i in range(fibonacci_iteration_quantity):
        spiral_distance = math.pi * fibonacci_second_element * render_zoom_factor / 2
        spiral_distance /= 90
        for j in range(90):
            turtle_pen.forward(spiral_distance)
            turtle_pen.left(1)
        temp = fibonacci_first_element
        fibonacci_first_element = fibonacci_second_element
        fibonacci_second_element = temp + fibonacci_second_element


def setup_pen_to_initial_point(
        render_zoom_factor
):
    turtle_pen.penup()
    turtle_pen.setposition(render_zoom_factor, 0)
    turtle_pen.seth(0)
    turtle_pen.pendown()
    turtle_pen.pencolor("red")
    turtle_pen.left(90)


def setup_pen_to_initial_position_and_set_color_to_red(
        render_zoom_factor
):
    turtle_pen.penup()
    turtle_pen.setposition(render_zoom_factor, 0)
    turtle_pen.seth(0)
    turtle_pen.speed(10)
    turtle_pen.pendown()
    turtle_pen.pencolor("red")


def calculate_fibo(
        square_a_size_side,
        square_b_size_side
):
    temp = square_b_size_side
    square_b_size_side = square_b_size_side + square_a_size_side
    square_a_size_side = temp
    return square_a_size_side, square_b_size_side


def draw_square(
        render_zoom_factor,
        square_a_size_side,
        square_b_size_side
):
    turtle_pen.backward(square_a_size_side * render_zoom_factor)
    turtle_pen.right(90)
    turtle_pen.forward(square_b_size_side * render_zoom_factor)
    turtle_pen.left(90)
    turtle_pen.forward(square_b_size_side * render_zoom_factor)
    turtle_pen.left(90)
    turtle_pen.forward(square_b_size_side * render_zoom_factor)


if __name__ == '__main__':

    zoom_factor: float = 25
    iteration_quantity: int = 1
    turtle_pen_speed: int = 0

    iteration_quantity = int(input('Insira o número de interações (deve ser > 1): '))

    while iteration_quantity < 1:
        iteration_quantity = int(input('Insira o número de interações (deve ser > 1): '))

    print("Série de Fibonacci para :", iteration_quantity, "elements :")
    turtle_pen: Turtle = turtle.Turtle()
    turtle_pen.speed(turtle_pen_speed)
    fibonacci_rendering(iteration_quantity, zoom_factor)
    turtle.done()