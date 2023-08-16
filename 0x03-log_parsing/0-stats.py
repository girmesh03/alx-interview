#!/usr/bin/python3
""" This module reads stdin line by line and computes metrics """
import sys

def print_stats(total_size, status_codes):
    """ Prints a summary of the log file """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    i = 0
    try:
        for line in sys.stdin:
            i += 1
            line = line.split()
            total_size += int(line[-1])
            code = line[-2]
            if code in status_codes:
                status_codes[code] += 1
            else:
                status_codes[code] = 1
            if i % 10 == 0:
                print_stats(total_size, status_codes)
        print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
