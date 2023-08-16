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

def extract_input(input_line):
    """
    Extract relevant parts from a log input line.

    Args:
        input_line (str): A line of log input.

    Returns:
        tuple: A tuple containing status code (int) and file size (int).
    """
    parts = input_line.split()
    if len(parts) == 10 and parts[8].isdigit():
        status_code = int(parts[8])
        file_size = int(parts[9])
        return status_code, file_size
    return None, None

def print_statistics(total_file_size, status_codes_stats):
    """
    Print statistics including total file size and lines per status code.

    Args:
        total_file_size (int): The total file size.
        status_codes_stats (dict): Dictionary containing status code frequencies.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_stats.keys()):
        print("{}: {}".format(code, status_codes_stats[code]))

def update_metrics(line, total_file_size, status_codes_stats):
    """
    Update metrics and status code statistics based on a log input line.

    Args:
        line (str): A line of log input.
        total_file_size (int): The running total file size.
        status_codes_stats (dict): Dictionary containing status code frequencies.

    Returns:
        int: Updated total file size.
    """
    status_code, file_size = extract_input(line)
    if status_code is not None and file_size is not None:
        total_file_size += file_size
        if status_code in status_codes_stats:
            status_codes_stats[status_code] += 1
    return total_file_size

def run():
    """
    Starts the log parser.
    """
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()
