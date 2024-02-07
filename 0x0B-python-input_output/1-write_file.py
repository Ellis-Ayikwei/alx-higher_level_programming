#!/usr/bin/python3

"""Defines a text file line-counting function."""


def write_file(filename="", text=""):
    """Return the number of lines in a text file."""

    with open(filename, "w+", encoding="utf-8") as f:
        f.write(text)
        charlen = len(text)
    return charlen
