#!/usr/bin/python3
"""Unit tests for the Base class."""
import json
import os
import sys
import unittest
from unittest.mock import MagicMock, patch

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

FILES = ["Base.json", "Rectangle.json", "Square.json",
         "Rectangle.csv", "Square.csv"]


class CleanTestCase(unittest.TestCase):
    """Reset the id counter and remove created files around each test."""

    def setUp(self):
        """Reset the counter."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Delete files created by the tests."""
        for name in FILES:
            if os.path.exists(name):
                os.remove(name)


def read_file(name):
    """Return the content of a file."""
    with open(name, "r", encoding="utf-8", newline="") as file:
        return file.read()


def write_file(name, text):
    """Write text in a file."""
    with open(name, "w", encoding="utf-8", newline="") as file:
        file.write(text)


class TestBaseId(CleanTestCase):
    """Tests for the id attribute."""

    def test_first_id(self):
        """The first automatic id is 1."""
        self.assertEqual(Base().id, 1)

    def test_ids_increment(self):
        """Automatic ids increase by one."""
        ids = [Base().id for _ in range(3)]
        self.assertEqual(ids, [1, 2, 3])

    def test_explicit_id(self):
        """An explicit id is kept."""
        self.assertEqual(Base(12).id, 12)

    def test_explicit_id_keeps_counter(self):
        """An explicit id does not move the counter."""
        ids = [Base().id, Base(12).id, Base().id]
        self.assertEqual(ids, [1, 12, 2])

    def test_other_values(self):
        """Any non-None value is stored as is."""
        for value in (0, -3, "abc", 3.5, [1], {"a": 1}, True):
            with self.subTest(value=value):
                self.assertEqual(Base(value).id, value)

    def test_none_increments(self):
        """Passing None behaves like no id."""
        self.assertEqual(Base(None).id, 1)

    def test_private_counter(self):
        """The counter is a private class attribute."""
        self.assertEqual(Base._Base__nb_objects, 0)
        Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        Base(5)
        self.assertEqual(Base._Base__nb_objects, 1)
        self.assertFalse(hasattr(Base(), "__nb_objects"))

    def test_id_is_public(self):
        """The id can be changed."""
        base = Base()
        base.id = 99
        self.assertEqual(base.id, 99)

    def test_too_many_args(self):
        """Two arguments are not accepted."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_shared_counter(self):
        """Subclasses share the counter."""
        self.assertEqual(Rectangle(1, 1).id, 1)
        self.assertEqual(Square(1).id, 2)
        self.assertEqual(Base().id, 3)


class TestBaseToJsonString(CleanTestCase):
    """Tests for to_json_string."""

    def test_none(self):
        """None gives an empty list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty(self):
        """An empty list gives an empty list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_one_dict(self):
        """One dictionary is serialized."""
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_type(self):
        """The result is a string."""
        self.assertIs(type(Base.to_json_string([{"id": 1}])), str)

    def test_many_dicts(self):
        """Several dictionaries round trip."""
        data = [{"id": 1, "x": 2}, {"id": 2, "x": 3}]
        self.assertEqual(json.loads(Base.to_json_string(data)), data)

    def test_rectangle_dict(self):
        """A rectangle dictionary is serialized."""
        rect = Rectangle(10, 7, 2, 8)
        text = Base.to_json_string([rect.to_dictionary()])
        self.assertEqual(json.loads(text), [rect.to_dictionary()])

    def test_no_args(self):
        """The argument is required."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_two_args(self):
        """Two arguments are not accepted."""
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])


class TestBaseSaveToFile(CleanTestCase):
    """Tests for save_to_file."""

    def test_rectangles(self):
        """Rectangles are saved in Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        data = json.loads(read_file("Rectangle.json"))
        self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_squares(self):
        """Squares are saved in Square.json."""
        s1 = Square(5)
        Square.save_to_file([s1])
        data = json.loads(read_file("Square.json"))
        self.assertEqual(data, [s1.to_dictionary()])
        self.assertFalse(os.path.exists("Rectangle.json"))

    def test_none(self):
        """None saves an empty list."""
        Rectangle.save_to_file(None)
        self.assertEqual(read_file("Rectangle.json"), "[]")

    def test_empty(self):
        """An empty list saves an empty list."""
        Square.save_to_file([])
        self.assertEqual(read_file("Square.json"), "[]")

    def test_overwrite(self):
        """An existing file is overwritten."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1])
        Rectangle.save_to_file([r2])
        data = json.loads(read_file("Rectangle.json"))
        self.assertEqual(data, [r2.to_dictionary()])

    def test_base_class(self):
        """Base saves an empty list in Base.json."""
        Base.save_to_file(None)
        self.assertEqual(read_file("Base.json"), "[]")

    def test_no_args(self):
        """The argument is required."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_two_args(self):
        """Two arguments are not accepted."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])


class TestBaseFromJsonString(CleanTestCase):
    """Tests for from_json_string."""

    def test_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_empty_list(self):
        """An empty JSON list gives an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_values(self):
        """A JSON list is decoded."""
        text = '[{"id": 89, "width": 10, "height": 4}]'
        result = Base.from_json_string(text)
        self.assertEqual(result, [{"id": 89, "width": 10, "height": 4}])
        self.assertIs(type(result), list)

    def test_round_trip(self):
        """Encoding then decoding returns the same data."""
        data = [{"id": 89, "width": 10}, {"id": 7, "width": 1}]
        text = Base.to_json_string(data)
        self.assertEqual(Base.from_json_string(text), data)

    def test_no_args(self):
        """The argument is required."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBaseCreate(CleanTestCase):
    """Tests for create."""

    def test_rectangle(self):
        """A rectangle is rebuilt with the same attributes."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        self.assertIsInstance(r2, Rectangle)

    def test_square(self):
        """A square is rebuilt with the same attributes."""
        s1 = Square(3, 1, 2)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)
        self.assertIsInstance(s2, Square)

    def test_partial_rectangle(self):
        """Missing keys keep the dummy defaults."""
        rect = Rectangle.create(id=5, width=3, height=4)
        self.assertEqual(str(rect), "[Rectangle] (5) 0/0 - 3/4")

    def test_full_rectangle(self):
        """All keys are applied."""
        rect = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(str(rect), "[Rectangle] (89) 3/4 - 1/2")

    def test_partial_square(self):
        """A square can be built with few keys."""
        square = Square.create(id=3, size=4)
        self.assertEqual(str(square), "[Square] (3) 0/0 - 4")

    def test_no_keys(self):
        """No keys gives a default dummy instance."""
        self.assertIsInstance(Rectangle.create(), Rectangle)
        self.assertIsInstance(Square.create(), Square)


class TestBaseLoadFromFile(CleanTestCase):
    """Tests for load_from_file."""

    def test_missing_file(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_rectangles(self):
        """Saved rectangles are loaded back as new objects."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual([str(r) for r in loaded], [str(r1), str(r2)])
        self.assertIsNot(loaded[0], r1)
        self.assertIsInstance(loaded[0], Rectangle)

    def test_squares(self):
        """Saved squares are loaded back as new objects."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual([str(s) for s in loaded], [str(s1), str(s2)])
        self.assertIsInstance(loaded[1], Square)

    def test_empty_list_file(self):
        """A file with an empty list gives an empty list."""
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_class_specific_file(self):
        """Each class reads its own file."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        self.assertEqual(Square.load_from_file(), [])


class TestBaseCsv(CleanTestCase):
    """Tests for the CSV methods."""

    def test_rectangle_content(self):
        """Rectangle rows are id,width,height,x,y."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        text = read_file("Rectangle.csv")
        self.assertEqual(text, "1,10,7,2,8\r\n2,2,4,0,0\r\n")

    def test_square_content(self):
        """Square rows are id,size,x,y."""
        Square.save_to_file_csv([Square(5), Square(7, 9, 1)])
        text = read_file("Square.csv")
        self.assertEqual(text, "1,5,0,0\r\n2,7,9,1\r\n")

    def test_none_and_empty(self):
        """None and an empty list give an empty file."""
        Rectangle.save_to_file_csv(None)
        self.assertEqual(read_file("Rectangle.csv"), "")
        Square.save_to_file_csv([])
        self.assertEqual(read_file("Square.csv"), "")

    def test_overwrite(self):
        """An existing file is overwritten."""
        Rectangle.save_to_file_csv([Rectangle(1, 2)])
        Rectangle.save_to_file_csv([Rectangle(3, 4)])
        self.assertEqual(len(read_file("Rectangle.csv").splitlines()), 1)

    def test_load_rectangles(self):
        """Rectangles round trip through CSV."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        loaded = Rectangle.load_from_file_csv()
        self.assertEqual([str(r) for r in loaded], [str(r1), str(r2)])
        self.assertIsNot(loaded[0], r1)

    def test_load_squares(self):
        """Squares round trip through CSV."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file_csv([s1, s2])
        loaded = Square.load_from_file_csv()
        self.assertEqual([str(s) for s in loaded], [str(s1), str(s2)])
        self.assertIsInstance(loaded[0], Square)

    def test_load_missing_file(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        self.assertEqual(Square.load_from_file_csv(), [])

    def test_load_empty_file(self):
        """An empty file gives an empty list."""
        write_file("Rectangle.csv", "")
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    def test_load_blank_line(self):
        """Blank lines are skipped."""
        write_file("Square.csv", "1,5,0,0\n\n2,3,1,1\n")
        self.assertEqual(len(Square.load_from_file_csv()), 2)


class TestBaseDraw(CleanTestCase):
    """Tests for draw, with a fake turtle module."""

    def test_draw(self):
        """Every shape is drawn with four sides."""
        fake = MagicMock()
        r1 = Rectangle(100, 40)
        r2 = Rectangle(90, 110, 30, 10)
        s1 = Square(35)
        with patch.dict(sys.modules, {"turtle": fake}):
            Base.draw([r1, r2], [s1])
        pen = fake.Turtle.return_value
        self.assertEqual(pen.forward.call_count, 12)
        self.assertEqual(pen.goto.call_count, 3)
        pen.forward.assert_any_call(100)
        pen.forward.assert_any_call(110)
        pen.forward.assert_any_call(35)
        pen.goto.assert_any_call(30, -10)
        fake.done.assert_called_once_with()

    def test_draw_empty(self):
        """Nothing is drawn for empty lists."""
        fake = MagicMock()
        with patch.dict(sys.modules, {"turtle": fake}):
            Base.draw([], [])
        pen = fake.Turtle.return_value
        pen.forward.assert_not_called()
        fake.done.assert_called_once_with()

    def test_draw_none(self):
        """None lists are tolerated."""
        fake = MagicMock()
        with patch.dict(sys.modules, {"turtle": fake}):
            Base.draw(None, None)
        fake.done.assert_called_once_with()

    def test_draw_args(self):
        """Both arguments are required."""
        with self.assertRaises(TypeError):
            Base.draw([])


if __name__ == "__main__":
    unittest.main()
