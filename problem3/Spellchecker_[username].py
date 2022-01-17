import re
import sys

# initialize the global variance
COUNT_UPPER = 0
COUNT_PUNCTUATION = 0
COUNT_NUMBER = 0
COUNT_WORD = 0
COUNT_CURRECT_WORD = 0
COUNT_INCORRECT_WORD = 0


# get the args
english_words_path = sys.argv[1]
input_file_path = sys.argv[2]
output_file_path = sys.argv[3]

# open the english_words_path file and record the dict
dict = []
with open(english_words_path, 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        dict.append(line)


# open the input file
with open(input_file_path, 'r') as f:
    context = f.read()

# count upper letters, numbers, punctuation
for c in context:
    if c.isupper():
        COUNT_UPPER += 1
    elif c.isdigit():
        COUNT_NUMBER += 1
    elif c.isalnum() or c.isspace():
        pass
    else:
        COUNT_PUNCTUATION += 1

# tranform the upper letter to lower
context = context.lower()

# remove punctuations and numbers
remove_chars = '[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
context = re.sub(remove_chars, '', context)

# get the context word list
word_list = context.split()

# get the len of words in file
COUNT_WORD = len(word_list)

# get the correct words and incorrect words in file
for word in word_list:
    if word in dict:
        COUNT_CURRECT_WORD += 1

COUNT_INCORRECT_WORD = COUNT_WORD - COUNT_CURRECT_WORD

# initialize the output
output = ""

# enter user_name
output += "[user_name]" + "\n"

# summarize the result into output
output += "Formatting ###################" + "\n"
output += "Number of upper case words changed: " + str(COUNT_UPPER) + "\n"
output += "Number of punctuations removed: " + str(COUNT_PUNCTUATION) + "\n"
output += "Number of numbers removed: " + str(COUNT_NUMBER) + "\n"
output += "Spellchecking ###################" + "\n"
output += "Number of words in file: " + str(COUNT_WORD) + "\n"
output += "Number of correct words in file: " + str(COUNT_CURRECT_WORD) + "\n"
output += "Number of incorrect words in file: " + str(COUNT_INCORRECT_WORD) + "\n"

#write to a txt
with open(output_file_path, 'w') as f:
    f.write(output)

