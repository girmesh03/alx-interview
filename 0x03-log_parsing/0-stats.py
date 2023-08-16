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

import re

def custom_extract(input_line):
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

    field_patterns = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    extracted_info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(field_patterns[0], field_patterns[1], field_patterns[2], field_patterns[3], field_patterns[4])
    match_result = re.fullmatch(log_format, input_line)
    if match_result is not None:
        status_code = match_result.group('status_code')
        file_size = int(match_result.group('file_size'))
        extracted_info['status_code'] = status_code
        extracted_info['file_size'] = file_size
    return extracted_info

def print_custom_stats(total_size, status_codes):
    """
    Prints statistics about the analyzed HTTP request log.
    """
    print('File size: {:d}'.format(total_size), flush=True)
    for status_code in sorted(status_codes.keys()):
        num = status_codes.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)

def update_custom_metrics(line, total_size, status_codes):
    """Updates metrics of the analyzed HTTP request log."""
    line_info = custom_extract(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes.keys():
        status_codes[status_code] += 1
    return total_size + line_info['file_size']

def run_custom():
    """Starts the analysis of the HTTP request logs."""
    line_number = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_custom_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_number += 1
            if line_number % 10 == 0:
                print_custom_stats(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_custom_stats(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run_custom()
