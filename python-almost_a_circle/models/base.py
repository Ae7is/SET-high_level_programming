#!/usr/bin/python3
"""Defines the Base class."""


class Base:
    """Base class for the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares using Turtle graphics."""
        import turtle

        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Rectangles and Squares")
        screen.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(0)
        pen.pensize(3)
        pen.hideturtle()

        colors = ["blue", "red", "green", "purple", "orange"]

        for i, rectangle in enumerate(list_rectangles):
            pen.penup()
            pen.goto(-350 + rectangle.x, 250 - rectangle.y)
            pen.setheading(0)
            pen.pencolor(colors[i % len(colors)])
            pen.pendown()

            for _ in range(2):
                pen.forward(rectangle.width)
                pen.right(90)
                pen.forward(rectangle.height)
                pen.right(90)

        for i, square in enumerate(list_squares):
            pen.penup()
            pen.goto(-350 + square.x, 250 - square.y)
            pen.setheading(0)
            pen.pencolor(colors[i % len(colors)])
            pen.pendown()

            for _ in range(4):
                pen.forward(square.size)
                pen.right(90)

        turtle.done()
