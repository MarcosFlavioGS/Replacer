#!/usr/bin/env python3
import sys


def replace_word_in_file(input_file, old_word, new_word):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        modified_content = content.replace(old_word, new_word)

        with open(input_file, 'w') as file:
            file.write(modified_content)

        print(
            f"Replacement complete. '{old_word}' was replaced with '{new_word}' in '{input_file}'."
        )
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error: Expected 3 arguments")
        print("Usage: replacer <file> <old_word> <new_word>")
    else:
        input_file = sys.argv[1]
        old_word = sys.argv[2]
        new_word = sys.argv[3]
        replace_word_in_file(input_file, old_word, new_word)
