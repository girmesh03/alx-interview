#!/usr/bin/python3
"""
This module contains a function that determines
if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)

Return: True if data is a valid UTF-8 encoding,
else return False

A character in UTF-8 can be 1 to 4 bytes long

The data set can contain multiple characters

The data will be represented by a list of integers

Each integer represents 1 byte of data, therefore
you only need to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes_to_check = 0
    valid_data = [byte & 0xFF for byte in data]

    for byte in valid_data:
        if num_bytes_to_check == 0:
            if (byte >> 7) == 0b0:  # 1-byte character
                num_bytes_to_check = 0
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes_to_check = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes_to_check = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes_to_check = 3
            else:
                return False  # Invalid starting byte for UTF-8 character
        else:
            if (byte >> 6) != 0b10:
                return False  # Continuation byte should start with '10'
            num_bytes_to_check -= 1
    # All expected continuation bytes were found
    return num_bytes_to_check == 0
