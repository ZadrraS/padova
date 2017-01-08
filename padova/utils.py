#!/usr/bin/env python
# encoding: utf-8
"""
Utilities
"""


def compression_type(filename, stream=False):
    """ Detect potential compressed file
    Returns the gz, bz2 or zip if a compression is detected, else None.

    From ezpadova by Morgan Fousneau
    """
    magic_dict = {b"\x1f\x8b\x08": "gz",
                  b"\x42\x5a\x68": "bz2",
                  b"\x50\x4b\x03\x04": "zip"}

    max_len = max(len(x) for x in magic_dict)
    if not stream:
        with open(filename, 'r') as f:
            file_start = f.read(max_len)
            print(file_start)
        for magic, filetype in list(magic_dict.items()):
            if file_start.startswith(magic):
                return filetype
    else:
        for magic, filetype in list(magic_dict.items()):
            if filename[:len(magic)] == magic:
                return filetype

    return None
