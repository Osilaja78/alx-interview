#!/usr/bin/python3
"""0-stats.py module"""

import sys
from typing import Tuple


def print_statistics(total_size: int, status_codes: int) -> None:
    """Prints file size and status code to stdout"""

    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")


def parse_line(line: str) -> Tuple[str, int, int]:
    """Parses lines from stdin to get status codes and file sizes"""

    parts = line.strip().split()
    if len(parts) != 10 or parts[8] != '"GET' or parts[9] != '/projects/260':
        return None
    ip, _, _, date, _, status_code, file_size = parts[:7]
    if not status_code.isdigit():
        return None
    return ip, int(status_code), int(file_size)


def main() -> None:
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
                ip, code, size = parsed
                total_size += size
                status_codes[code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
