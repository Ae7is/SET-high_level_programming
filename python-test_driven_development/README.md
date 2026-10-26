# python-test_driven_development

Python functions written with interactive tests (doctest) and unit tests.

| File | Description |
|---|---|
| `0-add_integer.py` | Adds two integers or floats |
| `2-matrix_divided.py` | Divides all the elements of a matrix |
| `3-say_my_name.py` | Prints "My name is first last" |
| `4-print_square.py` | Prints a square with `#` |
| `5-text_indentation.py` | Prints a text with 2 new lines after `.`, `?` and `:` |
| `100-matrix_mul.py` | Multiplies two matrices |
| `101-lazy_matrix_mul.py` | Multiplies two matrices with NumPy |
| `tests/*.txt` | Doctest files, one for each function above |
| `tests/6-max_integer_test.py` | Unit tests for `max_integer` |

## Running the tests

    python3 -m doctest -v ./tests/0-add_integer.txt
    python3 -m unittest tests.6-max_integer_test
