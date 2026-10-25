# python-inheritance

Python inheritance, class checks and doctest unit tests.

| File | Description |
|---|---|
| `0-lookup.py` | Returns the attributes and methods of an object |
| `1-my_list.py` | `MyList`, a list with `print_sorted()` |
| `2-is_same_class.py` | True if an object is exactly an instance of a class |
| `3-is_kind_of_class.py` | True if an object is an instance of a class or a subclass |
| `4-inherits_from.py` | True if an object is an instance of a strict subclass |
| `5-base_geometry.py` | An empty `BaseGeometry` class |
| `6-base_geometry.py` | Adds `area()`, which is not implemented |
| `7-base_geometry.py` | Adds `integer_validator()` |
| `8-rectangle.py` | `Rectangle` with private, validated sides |
| `9-rectangle.py` | Adds `area()` and a string description |
| `10-square.py` | `Square` based on `Rectangle` |
| `11-square.py` | `Square` with its own string description |
| `100-my_int.py` | `MyInt`, an int with `==` and `!=` inverted |
| `101-add_attribute.py` | Adds an attribute to an object if it is possible |

## Tests

Doctest files are in `tests/`:

    python3 -m doctest -v ./tests/1-my_list.txt
    python3 -m doctest -v ./tests/7-base_geometry.txt
