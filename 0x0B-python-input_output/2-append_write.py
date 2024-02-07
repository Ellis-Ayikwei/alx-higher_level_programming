#!/usr/bin/python3

"""Defines a text file line-counting function."""


def append_write(filename="", text=""):
    """Return the number of lines in appended text file."""

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        charlen = len(text)
    return charlen
