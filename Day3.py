import re


def read_input():
    input_file = open("input3", "r")

    for line in input_file:
        line = trim_line(line)


def trim_line(line):
    trimmed = re.sub("\s{2,}", " ", re.sub('\D', " ", line).strip())
    return trimmed

read_input()
