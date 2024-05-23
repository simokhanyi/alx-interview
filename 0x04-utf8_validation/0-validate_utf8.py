#!/usr/bin/python3
"""
a method that determines if a given data set represents a valid UTF-8 encoding
"""


def valid_utf8(data):
    def check_following_bytes(data, start, count):
        """ Helper function to check the next 'count' bytes """
        for i in range(start, start + count):
            if i >= len(data) or (data[i] & 0b11000000) != 0b10000000:
                return False
        return True

    i = 0
    while i < len(data):
        byte = data[i]
        if byte & 0b10000000 == 0:
            # 1-byte character (0xxxxxxx)
            i += 1
            continue
        elif byte & 0b11100000 == 0b11000000:
            # 2-byte character (110xxxxx 10xxxxxx)
            if not check_following_bytes(data, i + 1, 1):
                return False
            i += 2
        elif byte & 0b11110000 == 0b11100000:
            # 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
            if not check_following_bytes(data, i + 1, 2):
                return False
            i += 3
        elif byte & 0b11111000 == 0b11110000:
            # 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
            if not check_following_bytes(data, i + 1, 3):
                return False
            i += 4
        else:
            return False

    return True

# Test cases
data = [65]
print(valid_utf8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(valid_utf8(data))

data = [229, 65, 127, 256]
print(valid_utf8(data))
