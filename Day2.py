

def read_input():
    input_data = ['testidata', 'lol', 'aaaa']
    words_data = {}
    for word in input_data:
        processed_word = analyze_word(word)
        words_data[word] = processed_word

    sum_frequency(2, words_data)


def analyze_word(word):
    letter_set = {}
    for letter in word:
        if letter not in letter_set:
            letter_set[letter] = 1
        else:
            letter_set[letter] += 1

    return letter_set


def sum_frequency(letter_count, word_dic):
    total = 0
    for word, values in word_dic.items():
        if letter_count in values.values():
            total += 1
    return total


read_input()
