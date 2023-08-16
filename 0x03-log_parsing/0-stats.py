#!/usr/bin/python3
"""
This script reads log lines from stdin, computes metrics, and prints statistics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
After every 10 lines and/or a keyboard interruption (CTRL + C), print statistics:
- Total file size: File size: <total size>
- Number of lines by status code

Possible status codes: 200, 301, 400, 401, 403, 404, 405 and 500
If a status code doesn't appear or is not an integer, it's skipped.

Format for status code statistics: <status code>: <number>
Status codes are printed in ascending order.
"""

import sys

def print_stats(total_size, status_codes):
    """
    Print statistics including total file size and lines per status code.

    Args:
        total_size (int): The total file size.
        status_codes (dict): Dictionary containing status code frequencies.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def main():
    """
    Read log lines from stdin, compute metrics, and print statistics.
    """
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            tokens = line.split(" ")
            try:
                total_size += int(tokens[-1])
            except:
                pass
            try:
                status_codes[tokens[-2]] += 1
            except:
                pass
            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    """Main function."""
    main()
