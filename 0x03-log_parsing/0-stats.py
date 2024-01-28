#!/usr/bin/python3
"""0-stats.py module"""

import sys
from typing import Dict, List


def print_statistics(status_codes: Dict[str, int], total_size: int) -> None:
    """
    Prints both status_code and total_size
    Args:
        status_codes: dict of status codes
        total_size: total file size
    Return: nothing
    """

    print("File size: {}".format(total_size))
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


def parse_line(line: str) -> List[str]:
    """
    Parses each line of standard output
    Args:
        line: parsed stdout line
    Return: a list of string
    """

    parts = line.split()
    parts = parts[::-1]

    return parts


status_codes = {
    "200": 0, "301": 0, "400": 0,
    "401": 0, "403": 0, "404": 0,
    "405": 0, "500": 0
}
total_size = 0
line_count = 0

try:
    code = 0
    for lines in sys.stdin:
        parsed = parse_line(lines)

        if len(parsed) > 2:
            line_count += 1
            if line_count <= 10:
                total_size += int(parsed[0])
                code = parsed[1]
                if (code in status_codes.keys()):
                    status_codes[code] += 1
            if (line_count == 10):
                print_statistics(status_codes, total_size)
                line_count = 0
except KeyboardInterrupt:
    print_statistics(status_codes, total_size)
