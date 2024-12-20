import sys
import os
import csv
import string
from collections import Counter

# Define input and output files
input_file = "input1.txt"
output_file = "output.csv"

# Make sure that input and output files match
if not input_file.endswith('.txt'):
    print("Error: Input file must have a .txt extension.")
    sys.exit(1)

if not output_file.endswith('.csv'):
    print("Error: Output file must have a .csv extension.")
    sys.exit(1)

# Attempt to read the input file
try:
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error: Input file '{input_file}' does not exist.")
    sys.exit(1)
except Exception as exception:
    print(f"Error: Unable to read the file. {exception}")
    sys.exit(1)

# Check if the file is empty
if not lines:
    print("Error: Input file is empty.")
    sys.exit(1)

# Count words
# Used AI to for the section below  #######
word_count = Counter()
for line in lines:
    # Remove punctuation and convert to lowercase
    line = line.translate(str.maketrans('', '', string.punctuation)).lower()
    # Split line into words and update counter
    words = line.split()
    word_count.update(words)
################


# Find the most common word(s)
if not word_count:
    print("Error: No words found in the input file.")
    sys.exit(1)

# Used Ai to format section below #########
max_count = max(word_count.values())
most_common_words = [word for word, count in word_count.items() if count == max_count]
print(f"Most common word(s): {', '.join(most_common_words)} (appeared {max_count} times)")
############################################

# Write to CSV
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
