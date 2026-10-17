#!/usr/bin/python3
"""Unit tests for the Base class."""

import unittest
from unittest.mock import MagicMock, patch

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base initialization."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test automatically assigned IDs."""
        first = Base()
        second = Base()

        self.assertEqual(first.id, 1)
        self.assertEqual(second.id, 2)

    def test_custom_id(self):
        """Test a manually assigned ID."""
        obj = Base(50)

        self.assertEqual(obj.id, 50)

    def test_custom_id_does_not_increment_counter(self):
        """Test that a custom ID does not increment the counter."""
        Base(50)
        obj = Base()

        self.assertEqual(obj.id, 1)


class TestBaseDraw(unittest.TestCase):
    """Tests for the Base drawing method."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_draw_renders_rectangle_and_square(self):
        """Test drawing a rectangle and a square."""
        fake_turtle = MagicMock()
        rectangles = [Rectangle(10, 20, 1, 2)]
        squares = [Square(5, 3, 4)]

        with patch.dict("sys.modules", {"turtle": fake_turtle}):
            Base.draw(rectangles, squares)

        screen = fake_turtle.Screen.return_value
        pen = fake_turtle.Turtle.return_value

        screen.setup.assert_called_once_with(
            width=800, height=600
        )
        screen.title.assert_called_once_with(
            "Rectangles and Squares"
        )
        screen.bgcolor.assert_called_once_with("white")

        fake_turtle.Screen.assert_called_once_with()
        fake_turtle.Turtle.assert_called_once_with()
        fake_turtle.done.assert_called_once_with()

        pen.goto.assert_any_call(-349, 248)
        pen.goto.assert_any_call(-347, 246)
        pen.forward.assert_any_call(10)
        pen.forward.assert_any_call(20)
        pen.forward.assert_any_call(5)
        pen.right.assert_any_call(90)

    def test_draw_with_empty_lists(self):
        """Test drawing with no shapes."""
        fake_turtle = MagicMock()

        with patch.dict("sys.modules", {"turtle": fake_turtle}):
            Base.draw([], [])

        fake_turtle.Screen.assert_called_once_with()
        fake_turtle.Turtle.assert_called_once_with()
        fake_turtle.done.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
