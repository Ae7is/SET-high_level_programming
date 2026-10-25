#!/usr/bin/python3
"""Read stdin line by line and compute metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print the total file size and the number of lines by status code.

    Args:
        total_size (int): the sum of all file sizes read so far.
        status_counts (dict): the number of lines for each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    valid_codes = ("200", "301", "400", "401", "403", "404", "405", "500")
    total_size = 0
    status_counts = {}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            try:
                total_size += int(parts[-1])
                if parts[-2] in valid_codes:
                    code = parts[-2]
                    status_counts[code] = status_counts.get(code, 0) + 1
            except (IndexError, ValueError):
                pass
            if count % 10 == 0:
                print_stats(total_size, status_counts)
        if count % 10 != 0:
            print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
