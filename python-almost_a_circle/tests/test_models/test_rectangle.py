#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
import unittest
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle

BAD_TYPES = ["2", 2.5, None, True, [1], (1,), {}, {1}]


def display_of(rect):
    """Return what display prints for a rectangle."""
    with patch("sys.stdout", new_callable=io.StringIO) as out:
        rect.display()
    return out.getvalue()


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def check(self, exc, msg, func, *args, **kwargs):
        """Assert func raises exc with the exact message."""
        with self.assertRaises(exc) as ctx:
            func(*args, **kwargs)
        self.assertEqual(str(ctx.exception), msg)

    def test_inheritance(self):
        """Rectangle inherits Base."""
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_ids(self):
        """Ids are automatic or explicit."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_getters(self):
        """Getters return the given values."""
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(
            (rect.width, rect.height, rect.x, rect.y, rect.id),
            (1, 2, 3, 4, 5))

    def test_default_offsets(self):
        """x and y default to 0."""
        rect = Rectangle(1, 2)
        self.assertEqual((rect.x, rect.y), (0, 0))

    def test_private_attributes(self):
        """The attributes are private."""
        rect = Rectangle(1, 2, 3, 4)
        for name in ("width", "height", "x", "y"):
            self.assertTrue(hasattr(rect, "_Rectangle__" + name))

    def test_missing_args(self):
        """Width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        """Six arguments are not accepted."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, 0, 1, 2)

    def test_width_type(self):
        """Width must be an integer."""
        for value in BAD_TYPES:
            with self.subTest(value=value):
                self.check(TypeError, "width must be an integer",
                           Rectangle, value, 1)

    def test_height_type(self):
        """Height must be an integer."""
        for value in BAD_TYPES:
            with self.subTest(value=value):
                self.check(TypeError, "height must be an integer",
                           Rectangle, 1, value)

    def test_x_type(self):
        """x must be an integer."""
        for value in BAD_TYPES:
            with self.subTest(value=value):
                self.check(TypeError, "x must be an integer",
                           Rectangle, 1, 1, value)

    def test_y_type(self):
        """y must be an integer."""
        for value in BAD_TYPES:
            with self.subTest(value=value):
                self.check(TypeError, "y must be an integer",
                           Rectangle, 1, 1, 0, value)

    def test_width_value(self):
        """Width must be greater than 0."""
        for value in (0, -1, -100):
            with self.subTest(value=value):
                self.check(ValueError, "width must be > 0",
                           Rectangle, value, 1)

    def test_height_value(self):
        """Height must be greater than 0."""
        for value in (0, -1, -100):
            with self.subTest(value=value):
                self.check(ValueError, "height must be > 0",
                           Rectangle, 1, value)

    def test_x_value(self):
        """x must be at least 0."""
        self.check(ValueError, "x must be >= 0", Rectangle, 1, 1, -1)

    def test_y_value(self):
        """y must be at least 0."""
        self.check(ValueError, "y must be >= 0", Rectangle, 1, 1, 0, -1)

    def test_zero_offsets_allowed(self):
        """x and y can be 0."""
        rect = Rectangle(1, 1, 0, 0)
        self.assertEqual((rect.x, rect.y), (0, 0))

    def test_validation_order(self):
        """Attributes are validated in order."""
        self.check(TypeError, "width must be an integer",
                   Rectangle, "a", "b", "c", "d")
        self.check(TypeError, "height must be an integer",
                   Rectangle, 1, "b", "c", "d")
        self.check(TypeError, "x must be an integer",
                   Rectangle, 1, 1, "c", "d")
        self.check(ValueError, "width must be > 0", Rectangle, 0, "b")

    def test_setters(self):
        """Setters accept valid values."""
        rect = Rectangle(1, 1)
        rect.width = 5
        rect.height = 6
        rect.x = 7
        rect.y = 8
        self.assertEqual(
            (rect.width, rect.height, rect.x, rect.y), (5, 6, 7, 8))

    def test_setters_invalid(self):
        """Setters reject invalid values."""
        rect = Rectangle(1, 1)
        self.check(TypeError, "width must be an integer",
                   setattr, rect, "width", "1")
        self.check(ValueError, "height must be > 0",
                   setattr, rect, "height", 0)
        self.check(TypeError, "x must be an integer",
                   setattr, rect, "x", {})
        self.check(ValueError, "y must be >= 0", setattr, rect, "y", -1)
        self.assertEqual((rect.width, rect.height), (1, 1))

    def test_area(self):
        """Area is width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_area_large(self):
        """Area works with very large numbers."""
        big = 999999999999999999
        self.assertEqual(Rectangle(big, big).area(), big * big)

    def test_area_args(self):
        """Area takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)

    def test_display_simple(self):
        """Display without offsets."""
        self.assertEqual(display_of(Rectangle(4, 6)), "####\n" * 6)
        self.assertEqual(display_of(Rectangle(2, 2)), "##\n##\n")

    def test_display_offsets(self):
        """Display with x and y."""
        self.assertEqual(display_of(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(display_of(Rectangle(3, 2, 1, 0)),
                         " ###\n ###\n")

    def test_display_single_offset(self):
        """Display with only x or only y."""
        self.assertEqual(display_of(Rectangle(1, 1, 3)), "   #\n")
        self.assertEqual(display_of(Rectangle(1, 1, 0, 2)), "\n\n#\n")

    def test_display_args(self):
        """Display takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).display(1)

    def test_str(self):
        """String representation."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_str_after_change(self):
        """String reflects later changes."""
        rect = Rectangle(1, 1)
        rect.width = 9
        self.assertEqual(str(rect), "[Rectangle] (1) 0/0 - 9/1")

    def test_update_args(self):
        """Update with no-keyword arguments."""
        rect = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect), "[Rectangle] (1) 10/10 - 10/10")
        rect.update(89)
        self.assertEqual(str(rect), "[Rectangle] (89) 10/10 - 10/10")
        rect.update(89, 2)
        self.assertEqual(str(rect), "[Rectangle] (89) 10/10 - 2/10")
        rect.update(89, 2, 3)
        self.assertEqual(str(rect), "[Rectangle] (89) 10/10 - 2/3")
        rect.update(89, 2, 3, 4)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/10 - 2/3")
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_extra_args(self):
        """Extra arguments are ignored."""
        rect = Rectangle(1, 1)
        rect.update(7, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(rect), "[Rectangle] (7) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Update with keyword arguments."""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(height=1)
        self.assertEqual(str(rect), "[Rectangle] (1) 10/10 - 10/1")
        rect.update(width=1, x=2)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/10 - 1/1")
        rect.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rect), "[Rectangle] (89) 3/1 - 2/1")
        rect.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rect), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_args_win(self):
        """Keyword arguments are skipped when args exist."""
        rect = Rectangle(1, 1)
        rect.update(5, width=50, height=60)
        self.assertEqual(str(rect), "[Rectangle] (5) 0/0 - 1/1")

    def test_update_unknown_key(self):
        """Unknown keys are ignored."""
        rect = Rectangle(1, 1)
        rect.update(color="red")
        self.assertFalse(hasattr(rect, "color"))

    def test_update_nothing(self):
        """Update without arguments changes nothing."""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update()
        self.assertEqual(str(rect), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_invalid(self):
        """Update validates the values."""
        rect = Rectangle(1, 1)
        self.check(TypeError, "width must be an integer",
                   rect.update, 1, "a")
        self.check(ValueError, "height must be > 0", rect.update, 1, 1, -3)
        self.check(ValueError, "x must be >= 0", rect.update, x=-1)
        self.check(TypeError, "y must be an integer", rect.update, y="1")

    def test_to_dictionary(self):
        """Dictionary representation."""
        rect = Rectangle(10, 2, 1, 9)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        result = rect.to_dictionary()
        self.assertEqual(result, expected)
        self.assertIs(type(result), dict)

    def test_to_dictionary_copy(self):
        """Changing the dictionary does not change the instance."""
        rect = Rectangle(10, 2)
        result = rect.to_dictionary()
        result["width"] = 99
        self.assertEqual(rect.width, 10)

    def test_dictionary_round_trip(self):
        """Dictionary can feed update."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_to_dictionary_args(self):
        """to_dictionary takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
