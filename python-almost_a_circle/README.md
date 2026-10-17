# python-almost_a_circle

A Python project about classes, inheritance, validation, serialization
and unit testing.

## Classes

- `Base`: manages the `id` of all other classes, JSON and CSV
  serialization, and drawing with the Turtle module.
- `Rectangle`: inherits `Base`, with validated `width`, `height`,
  `x` and `y`.
- `Square`: inherits `Rectangle`, with a `size` property.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Code follows pycodestyle 2.8.*
- Drawing needs Tkinter: `sudo apt-get install python3-tk`

## Run the unit tests

    python3 -m unittest discover tests
