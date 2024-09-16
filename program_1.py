'''Write a program that reads a text file, counts the number of lines, words, and characters, and writes the results to a new file.'''


def count_file_statistics(input_file):
    with open(input_file, 'r') as file:
        text = file.read()

    lines = text.splitlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_characters = len(text)

    return num_lines, num_words, num_characters

def write_statistics(output_file, num_lines, num_words, num_characters):
    with open(output_file, 'w') as file:
        file.write(f"Number of lines: {num_lines}\n")
        file.write(f"Number of words: {num_words}\n")
        file.write(f"Number of characters: {num_characters}\n")

input_filename = input("Enter the input file name: ")
output_filename = input("Enter the output file name: ")

lines, words, characters = count_file_statistics(input_filename)

write_statistics(output_filename, lines, words, characters)

print(f"Statistics have been written to {output_filename}")
