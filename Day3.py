import re

map = {}


def read_input():
    input_file = open("input3_test", "r")

    for line in input_file:
        line = trim_line(line)
        draw_spots_to_map(int(line[0]), int(line[2]), int(line[4]), int(line[6]), int(line[8]))


def draw_spots_to_map(id, from_left, from_top, wide, tall):

    for i in range(tall):
        for j in range(wide):
            map[from_left + j, from_top + i] = id



def trim_line(line):
    trimmed = re.sub("\s{2,}", " ", re.sub('\D', " ", line).strip())
    return trimmed

read_input()
