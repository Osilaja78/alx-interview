#!/usr/bin/python3
"""0-stats.py module"""

import sys
from typing import Tuple


def print_statistics(total_size: int, status_codes: int) -> None:
    """Prints file size and status code to stdout"""

    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count and count != 0:
            print(f"{code}: {count}")


def parse_line(line: str) -> Tuple[int, int]:
    """Parses lines from stdin to get status codes and file sizes"""

    parts = line.strip().split()

    if len(parts) != 9 or parts[4] != '"GET' or parts[5] != '/projects/260':
        return None

    status_code = parts[7]
    file_size = parts[8]

    if not status_code.isdigit():
        return None
    return int(status_code), int(file_size)


def main():
    """Main function, calls both helper functions"""

    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0,
        401: 0, 403: 0, 404: 0,
        405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            parsed = parse_line(line)
            if parsed:
                code, size = parsed
                total_size += size
                status_codes[code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)


if __name__ == "__main__":
    main()
