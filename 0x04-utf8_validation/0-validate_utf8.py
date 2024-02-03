#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    num_bytes_to_follow = 0

    for num in data:
        if num & 0x80:
            if num_bytes_to_follow == 0:
                if num & 0xE0 == 0xC0:
                    num_bytes_to_follow = 1
                elif num & 0xF0 == 0xE0:
                    num_bytes_to_follow = 2
                elif num & 0xF8 == 0xF0:
                    num_bytes_to_follow = 3
                else:
                    return False
            else:
                if num & 0xC0 != 0x80:
                    return False
                num_bytes_to_follow -= 1
        else:
            if num_bytes_to_follow > 0:
                return False

    return num_bytes_to_follow == 0
