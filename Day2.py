

def read_input():
    input_data = open('input2.txt', 'r')
    words_data = {}
    for word in input_data:
        processed_word = analyze_word(word)
        words_data[word] = processed_word

    twos = sum_frequency(2, words_data)
    tres = sum_frequency(3, words_data)

    print(f'checksum: {twos*tres}')


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
