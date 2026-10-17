#!/usr/bin/python3
"""Unit tests for the Square class."""
import io
import unittest
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

BAD_TYPES = ["2", 2.5, None, True, [1], (1,), {}, {1}]


def display_of(square):
    """Return what display prints for a square."""
    with patch("sys.stdout", new_callable=io.StringIO) as out:
        square.display()
    return out.getvalue()


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def check(self, exc, msg, func, *args, **kwargs):
        """Assert func raises exc with the exact message."""
        with self.assertRaises(exc) as ctx:
            func(*args, **kwargs)
        self.assertEqual(str(ctx.exception), msg)

    def test_inheritance(self):
        """Square inherits Rectangle and Base."""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_defaults(self):
        """Default attributes."""
        square = Square(5)
        self.assertEqual(square.id, 1)
        self.assertEqual((square.size, square.width, square.height), (5, 5, 5))
        self.assertEqual((square.x, square.y), (0, 0))

    def test_explicit_values(self):
        """Explicit attributes."""
        square = Square(2, 3, 4, 12)
        self.assertEqual(
            (square.size, square.x, square.y, square.id), (2, 3, 4, 12))

    def test_ids(self):
        """Ids increase automatically."""
        self.assertEqual(Square(1).id, 1)
        self.assertEqual(Square(1).id, 2)

    def test_no_new_attributes(self):
        """Square only uses the Rectangle attributes."""
        names = set(vars(Square(1)))
        expected = {"id", "_Rectangle__width", "_Rectangle__height",
                    "_Rectangle__x", "_Rectangle__y"}
        self.assertEqual(names, expected)

    def test_missing_args(self):
        """Size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        """Five arguments are not accepted."""
        with self.assertRaises(TypeError):
            Square(1, 0, 0, 1, 2)

    def test_size_type(self):
        """Size must be an integer."""
        for value in BAD_TYPES:
            with self.subTest(value=value):
                self.check(TypeError, "width must be an integer",
                           Square, value)

    def test_size_value(self):
        """Size must be greater than 0."""
        for value in (0, -1, -50):
            with self.subTest(value=value):
                self.check(ValueError, "width must be > 0", Square, value)

    def test_x_y_validation(self):
        """x and y keep the Rectangle validation."""
        self.check(TypeError, "x must be an integer", Square, 1, "a")
        self.check(TypeError, "y must be an integer", Square, 1, 0, "a")
        self.check(ValueError, "x must be >= 0", Square, 1, -1)
        self.check(ValueError, "y must be >= 0", Square, 1, 0, -1)

    def test_str(self):
        """String representation."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2)), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (3) 1/3 - 3")
        self.assertEqual(str(Square(3, 1, 3, 9)), "[Square] (9) 1/3 - 3")

    def test_area(self):
        """Area is size squared."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_display(self):
        """Display uses x and y."""
        self.assertEqual(display_of(Square(5)), "#####\n" * 5)
        self.assertEqual(display_of(Square(2, 2)), "  ##\n  ##\n")
        self.assertEqual(display_of(Square(3, 1, 3)),
                         "\n\n\n ###\n ###\n ###\n")

    def test_size_getter(self):
        """Size getter returns the width."""
        self.assertEqual(Square(7).size, 7)

    def test_size_setter(self):
        """Size setter changes width and height."""
        square = Square(5)
        square.size = 10
        self.assertEqual((square.width, square.height), (10, 10))
        self.assertEqual(str(square), "[Square] (1) 0/0 - 10")

    def test_size_setter_invalid(self):
        """Size setter validates like width."""
        square = Square(5)
        self.check(TypeError, "width must be an integer",
                   setattr, square, "size", "9")
        self.check(ValueError, "width must be > 0",
                   setattr, square, "size", 0)
        self.check(ValueError, "width must be > 0",
                   setattr, square, "size", -4)
        self.assertEqual(square.size, 5)

    def test_update_args(self):
        """Update with no-keyword arguments."""
        square = Square(5)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 5")
        square.update(10)
        self.assertEqual(str(square), "[Square] (10) 0/0 - 5")
        square.update(1, 2)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 2")
        square.update(1, 2, 3)
        self.assertEqual(str(square), "[Square] (1) 3/0 - 2")
        square.update(1, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")

    def test_update_extra_args(self):
        """Extra arguments are ignored."""
        square = Square(5)
        square.update(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Update with keyword arguments."""
        square = Square(5)
        square.update(1, 2, 3, 4)
        square.update(x=12)
        self.assertEqual(str(square), "[Square] (1) 12/4 - 2")
        square.update(size=7, y=1)
        self.assertEqual(str(square), "[Square] (1) 12/1 - 7")
        square.update(size=7, id=89, y=1)
        self.assertEqual(str(square), "[Square] (89) 12/1 - 7")

    def test_update_args_win(self):
        """Keyword arguments are skipped when args exist."""
        square = Square(5)
        square.update(3, size=9)
        self.assertEqual(str(square), "[Square] (3) 0/0 - 5")

    def test_update_unknown_key(self):
        """Unknown keys are ignored."""
        square = Square(5)
        square.update(color="red", width=99)
        self.assertFalse(hasattr(square, "color"))
        self.assertEqual(square.size, 5)

    def test_update_invalid(self):
        """Update validates the values."""
        square = Square(5)
        self.check(TypeError, "width must be an integer",
                   square.update, 1, "a")
        self.check(ValueError, "width must be > 0", square.update, 1, 0)
        self.check(ValueError, "x must be >= 0", square.update, x=-1)
        self.check(TypeError, "y must be an integer", square.update, y="1")

    def test_to_dictionary(self):
        """Dictionary representation."""
        square = Square(10, 2, 1)
        expected = {"id": 1, "x": 2, "size": 10, "y": 1}
        result = square.to_dictionary()
        self.assertEqual(result, expected)
        self.assertIs(type(result), dict)

    def test_to_dictionary_copy(self):
        """Changing the dictionary does not change the instance."""
        square = Square(10)
        result = square.to_dictionary()
        result["size"] = 99
        self.assertEqual(square.size, 10)

    def test_dictionary_round_trip(self):
        """Dictionary can feed update."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


if __name__ == "__main__":
    unittest.main()
