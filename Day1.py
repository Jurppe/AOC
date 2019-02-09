import re

input_data = open("input.txt", "r")

flag = 0

for num in input_data:
    num = int(num)
    flag += num
    print(flag)

print(flag)
