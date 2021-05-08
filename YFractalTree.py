import turtle
from turtle import Turtle


def draw_fractal_tree(function_tree_size, function_tree_level, function_branch_angle):
    if function_tree_level > 0:
        turtle_pen.forward(function_tree_size)
        turtle_pen.right(function_branch_angle)
        draw_fractal_tree(0.8 * function_tree_size, function_tree_level - 1, function_branch_angle)
        turtle_pen.left(2 * function_branch_angle)
        draw_fractal_tree(0.8 * function_tree_size, function_tree_level - 1, function_branch_angle)
        turtle_pen.right(function_branch_angle)
        turtle_pen.forward(-function_tree_size)


if __name__ == '__main__':
    turtle_pen: Turtle = turtle.Turtle()
    tree_level = 7
    tree_size = 80
    branch_angle = 45

    turtle_pen.speed(2)
    turtle_pen.right(-90)
    draw_fractal_tree(tree_size, tree_level, branch_angle)
    turtle.done()
