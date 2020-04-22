        #   Austin Copley
        #   CSCI 102 – Section B
        #   Week 13 - Incremental Development


def print_output(string):
    print("OUTPUT", string)

def load_file(filename):
    output_list = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            output_list = output_list.append(line)
        return output_list

def update_string(string, char, i):
    string = list(string)
    string[i] = char
    string = ''.join(string)
    print("OUTPUT", string)

def find_word_count(list1, string):
    total = 0
    for words in list1:
        word = ''
        i = 0
        j = 0
        while i < len(words):
            if words[i] == ' ' or len(words) == (i + 1):
                word = words[j:(i + 1)]
                j = i + 1
            i += 1
            if string.lower() == word.lower() or (string.lower() + ' ') == word.lower():
                total += 1
                word = ''
    return total

