# -*- coding: utf-8 -*-
# Import Dependencies using regular expressions 

import re

# Declare file location to load and output
load = "raw_data/paragraph_1.txt"
output = "analysis.txt"

# String variable to hold the paragraph contents
paragraph = ""

# Read the text file
with open(load) as txt_data:
    paragraph = txt_data.read().replace("\n", " ")

# Splitting the paragraph using " " to calculate word count
word_split = paragraph.split(" ")
word_count = len(word_split)

# Create list for  all the letter counts
letter_counts = []

# Loop through the word array and calculate the length of each word
for word in word_split:

    letter_counts.append(len(word))

# Find the average letter count
avg_letter_count = sum(letter_counts) / float(len(letter_counts))

sentence_split = re.split("(?<=[.!?]) +", paragraph)

print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []

# Looping through the sentence array and find the number of words in each
for sentence in sentence_split:

    # Calculate the number of words in each sentence and add to the list
    words_per_sentence.append(len(sentence.split(" ")))

# Calculate the average word count for each sentence
avg_sentence_len = sum(words_per_sentence) / float(len(words_per_sentence))

# Paragraph Analysis Output
output = (
    f"\nParagraph Analysis\n"
    f"-----------------\n"
    f"Approximate Word Count: {word_count}\n"
    f"Approximate Sentence Count: {sentence_count}\n"
    f"Average Letter Count: {avg_letter_count}\n"
    f"Average Sentence Length: {avg_sentence_len}\n")

# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
with open(output, "a") as txt_file:
    txt_file.write(output)