
def go_trough_input():
    current_value = 0
    used_values = set()
    is_found = False
    while not is_found:
        input_data = open("input.txt", "r")
        for num in input_data:
            num = int(num)
            current_value += num
            if check_duplicate(current_value, used_values):
                is_found = True
                return current_value
            else:
                used_values.add(current_value)


def check_duplicate(current, set):
    if current in set:
        return True
    else:
        return False

print(go_trough_input())

