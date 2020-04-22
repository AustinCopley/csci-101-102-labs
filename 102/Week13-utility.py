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

