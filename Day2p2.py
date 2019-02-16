

def read_input():
    input_data = open('input2.txt', 'r')
    words_data = {}
    for word in input_data:
        processed_word = analyze_word(word)
        words_data[word] = processed_word


def analyze_word(word):
    letter_set = {}
    for letter in word:
        if letter not in letter_set:
            letter_set[letter] = 1
        else:
            letter_set[letter] += 1

    return letter_set


def compare_words(first, second):
    misses = 0

    for i in first:
        if first[i] != second[i]:
            misses += 1

    if misses == 0:
        print("Sanat oli samat?")

    elif misses == 1:
        return first, second

    else:
        return False

read_input()
