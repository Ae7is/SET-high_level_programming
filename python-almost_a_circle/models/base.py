#!/usr/bin/python3
"""Module that defines the Base class.

The Base class manages the id attribute of every other class of the
project and handles JSON and CSV serialization.
"""
import csv
import json


class Base:
    """Base class of the project.

    Attributes:
        __nb_objects (int): number of instances created without
            an explicit id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance.

        Args:
            id (int): the id to assign. When None, the private class
                counter is incremented and its value is used.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries (list): list of dictionaries.

        Returns:
            "[]" if the list is None or empty, otherwise the JSON string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objects to a file.

        The file is named <Class name>.json and is overwritten.

        Args:
            list_objs (list): list of instances inheriting Base.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): JSON string representing a list.

        Returns:
            An empty list if json_string is None or empty, otherwise
            the decoded list.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        A dummy instance is created first, then updated with the
        real values.

        Args:
            **dictionary: attributes of the instance to create.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances stored in <Class name>.json.

        Returns:
            An empty list if the file does not exist.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            return []
        return [cls.create(**item) for item in cls.from_json_string(content)]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write a list of objects to <Class name>.csv.

        Rectangle rows: id,width,height,x,y
        Square rows: id,size,x,y

        Args:
            list_objs (list): list of instances inheriting Base.
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow([getattr(obj, key) for key in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances stored in <Class name>.csv.

        Returns:
            An empty list if the file does not exist.
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        instances = []
        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                for row in csv.reader(file):
                    if not row:
                        continue
                    values = [int(value) for value in row]
                    instances.append(cls.create(**dict(zip(fields, values))))
        except FileNotFoundError:
            return []
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw every Rectangle and Square.

        Args:
            list_rectangles (list): list of Rectangle instances.
            list_squares (list): list of Square instances.
        """
        import turtle

        shapes = list(list_rectangles or []) + list(list_squares or [])
        colors = ["#e63946", "#2a9d8f", "#e9c46a", "#264653",
                  "#f4a261", "#6a4c93"]

        screen = turtle.Screen()
        screen.bgcolor("#f1faee")
        pen = turtle.Turtle()
        pen.speed(3)
        pen.pensize(4)

        for index, shape in enumerate(shapes):
            pen.color(colors[index % len(colors)])
            pen.penup()
            pen.goto(shape.x, -shape.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(shape.width)
                pen.right(90)
                pen.forward(shape.height)
                pen.right(90)

        pen.hideturtle()
        turtle.done()
