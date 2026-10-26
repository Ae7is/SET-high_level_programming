#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the function max_integer."""

    def test_ordered_list(self):
        """The maximum is at the end of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The maximum is found in an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """The maximum is at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """The maximum is in the middle of the list."""
        self.assertEqual(max_integer([1, 5, 2]), 5)

    def test_one_element(self):
        """A list with one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Calling the function without argument returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """The maximum of negative numbers is the closest to zero."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_positive_and_negative(self):
        """Positive, zero and negative numbers together."""
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_duplicates(self):
        """Repeated values are handled."""
        self.assertEqual(max_integer([3, 3, 3]), 3)
        self.assertEqual(max_integer([1, 4, 4, 2]), 4)

    def test_floats(self):
        """Floats are compared like integers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_integers_and_floats(self):
        """Integers and floats can be mixed."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_big_numbers(self):
        """Very large numbers are handled."""
        self.assertEqual(max_integer([10 ** 100, 5]), 10 ** 100)

    def test_infinity(self):
        """Infinity is bigger than any number."""
        self.assertEqual(max_integer([1, float('inf')]), float('inf'))

    def test_tuple(self):
        """A tuple works as well, since it has a length and indexes."""
        self.assertEqual(max_integer((1, 2, 3)), 3)

    def test_list_not_changed(self):
        """The list is not modified by the function."""
        numbers = [3, 1, 2]
        max_integer(numbers)
        self.assertEqual(numbers, [3, 1, 2])

    def test_none(self):
        """None has no length, so a TypeError is raised."""
        self.assertRaises(TypeError, max_integer, None)

    def test_integer_argument(self):
        """An integer has no length, so a TypeError is raised."""
        self.assertRaises(TypeError, max_integer, 5)

    def test_mixed_types(self):
        """Numbers and strings cannot be compared."""
        self.assertRaises(TypeError, max_integer, [1, "a"])
        self.assertRaises(TypeError, max_integer, ["a", 1])


if __name__ == '__main__':
    unittest.main()
