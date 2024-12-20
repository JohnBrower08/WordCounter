import sys
import os
import csv
import string
from collections import Counter

# Define input and output files
input_file = "input1.txt"
output_file = "output.csv"

# Make sure that input and output files match
def check_file_type(input_file, output_file):
    if not input_file.endswith('.txt'):
        print("Error: Input file must have a .txt extension.")
        sys.exit(1)

    if not output_file.endswith('.csv'):
        print("Error: Output file must have a .csv extension.")
        sys.exit(1)

# Attempt to read the input file
def read_file(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)
    except Exception as exception:
        print(f"Error: Unable to read the file. {exception}")
        sys.exit(1)
    return lines

# Check if the file is empty
def check_file_empty(lines):
    if not lines:
        print("Error: Input file is empty.")
        sys.exit(1)

# Count words
def count_words(lines):
    word_count = Counter()
    for line in lines:
        # Remove punctuation and convert to lowercase
        line = line.translate(str.maketrans('', '', string.punctuation)).lower()
        # Split line into words and update counter
        words = line.split()
        word_count.update(words)
    
    # Find the most common word(s)
    if not word_count:
        print("Error: No words found in the input file.")
        sys.exit(1)

    # Used AI to format below
    max_count = max(word_count.values())
    most_common_words = [word for word, count in word_count.items() if count == max_count]
    print(f"Most common word(s): {', '.join(most_common_words)} (appeared {max_count} times)")
    #########################
    return word_count

# Write to CSV
def write_csv(word_count, output_file):
    """Writes the word count to a CSV file."""
    try:
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Count'])
            for word, count in sorted(word_count.items()):
                writer.writerow([word, count])
    except Exception as e:
        print(f"Error: Unable to write to the output file. {e}")
        sys.exit(1)

    print(f"Word counts successfully saved to '{output_file}'.")


# Main program
# Validate file types
check_file_type(input_file, output_file)

# Read the input file
lines = read_file(input_file)

# Check if the file is empty
check_file_empty(lines)

# Count words
word_count = count_words(lines)

# Write results to CSV
write_csv(word_count, output_file)
