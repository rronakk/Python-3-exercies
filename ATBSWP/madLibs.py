"""Create a program that reads in text files, and let user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB,
or VERB appear in text file."""
# ask user to input a sentence , with those keyword (ADJECTIVE, NOUN, ADVERB, VERB) , allowed to replace

import re

# Opening a file, and writing question to it
question_file = open('original_file.txt', 'w')
question = input('Enter your text with keyword (ADJECTIVE, NOUN, ADVERB, VERB) intended to be replaced: \n')
question_file.write(question)
question_file.close()

# Reading a file
question_file_to_read = open('original_file.txt')
question_context = question_file_to_read.read()

# Ask user-input for keyword replacement.
adjective = input("Enter an Adjective: \n")
noun = input("Enter a Noun: \n")
adverb = input("Enter an Adverb: \n")
verb = input("Enter a verb: \n")

# Do the replacement
def expand(D, s):
    # tokenize words and punctuation into a list
    t = re.split('(\W+)',  s)
    # create an empty list to hold intermediate results
    b = []
    # iterate over list, if a list element is in the dictionary, append
    # the substitute; otherwise, send the element
    for word in t:
        if word in D:
            b.append(D[word][0])
        else:
            b.append(word)
    # reconstruct the string
    return  ''.join(b)

replacer = {'ADJECTIVE': [adjective], 'NOUN': [noun], 'ADVERB': [adverb], 'VERB': [verb]}

replaced_file = open('replaced_file.txt', 'w')
replaced_file.write(expand(replacer, question_context))
