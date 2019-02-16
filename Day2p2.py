

def read_input():
    input_data = open('input2.txt', 'r')
    words_data = []
    for word in input_data:
        for comparable in words_data:
            if compare_words(word, comparable):
                print("Stopping process")
                return 0
        words_data.append(word)


def compare_words(first, second):
    misses = 0
    i = 0

    print(f"comparing words {first} and {second}")

    while i < len(first):
        if first[i] != second[i]:
            misses += 1
        i += 1

    if misses == 0:
        print("Sanat oli samat?")

    elif misses == 1:
        print(f"######## Correct words were {first} and {second} ########")
        return True

    else:
        return False


read_input()
