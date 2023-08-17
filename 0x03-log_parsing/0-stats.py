#!/usr/bin/python3
"""This module contains a script that reads stdin line by line and computes
    some statistics."""


import sys

def print_statistics(file_size, status_code):
    """Prints the statistics"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def main():
    """Main function"""
    file_size = 0
    status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}
    counter = 0
    try:
        for line in sys.stdin:
            counter += 1
            data = line.split()
            file_size += int(data[-1])
            status_code[data[-2]] += 1
            if counter % 10 == 0:
                print_statistics(file_size, status_code)
        print_statistics(file_size, status_code)
    except KeyboardInterrupt:
        print_statistics(file_size, status_code)
        raise


if __name__ == "__main__":
    main()
