#!/usr/bin/python3
import os

'''Write a function that reads a
text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    """reads a textfile and outputs to stdout"""
    with (open(filename, "r", encoding="utf-8")) as f:
        readedfile = f.read()
        print(readedfile)
