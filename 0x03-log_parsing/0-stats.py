#!/usr/bin/python3
"""This module contains a script that reads stdin line by line and computes
    some statistics."""


import sys


def print_statistics(file_size, status_code):
    """Prints the accumulated statistics."""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0
    file_size = 0

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            file_size += int(data[-1])
            if data[-2] in status_code:
                status_code[data[-2]] += 1
            if count % 10 == 0:
                print_statistics(file_size, status_code)
                status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
                               "403": 0, "404": 0, "405": 0, "500": 0}
                file_size = 0
    except KeyboardInterrupt:
        print_statistics(file_size, status_code)
        raise
