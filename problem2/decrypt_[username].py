import sys

# get the args
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# decode the hex text
def decode_hex(s:str) -> str:
    wordlist = s.split(" ")
    res = ""
    for word in wordlist:
        res += chr(int(word, 16))
    return res.lower()

# deocde the caesar text
def decode_caesar(s:str) -> str:
    res = ""
    for c in s:
        if c < 'a' or c > 'z':
            res += c
        else:
            if c == 'a':
                res += 'x'
            elif c == 'b':
                res += 'y'
            elif c == 'c':
                res += 'z'
            else:
                res += chr(ord(c) - 3)
    return res

# decode the morse text
def decode_morse(s:str) -> str:
    res = ""
    slist = s.split(' ')
    dict = {'.-': 'A',
            '-...': 'B',
            '-.-.': 'C',
            '-..': 'D',
            '.': 'E',
            '..-.': 'F',
            '--.': 'G',
            '....': 'H',
            '..': 'I',
            '.---': 'J',
            '-.-': 'K',
            '.-..': 'L',
            '--': 'M',
            '-.': 'N',
            '---': 'O',
            '.--.': 'P',
            '--.-': 'Q',
            '.-.': 'R',
            '...': 'S',
            '-': 'T',
            '..-': 'U',
            '...-': 'V',
            '.--': 'W',
            '-..-': 'X',
            '-.--': 'Y',
            '--..': 'Z',
            '.----': '1',
            '..---': '2',
            '...--': '3',
            '....-': '4',
            '.....': '5',
            '-....': '6',
            '--...': '7',
            '---..': '8',
            '----.': '9',
            '-----': '0',
            '..--..': '?',
            '-..-.': '/',
            '-.--.-': '()',
            '-....-': '-',
            '.-.-.-': '.',
            '/' : ' '
            }
    for val in slist:
        res += dict[val]
    return res.lower()

# output the decode context according to different type
def helper(type:str, text:str) -> str:
    if type[0] == 'H':
        return decode_hex(text)
    elif type[0] == 'C':
        return decode_caesar(text)
    elif type[0] == 'M':
        return decode_morse(text)

# open the input file
with open(input_file_path, 'r') as f:
    context = f.read()

# get the type and the text
type = context.split(":")[0]
text = context.split(":")[1]

# initialize the output
output = helper(type, text)

# write to a txt
with open(output_file_path, 'w') as f:
    f.write(output)

