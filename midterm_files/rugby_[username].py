import sys

# get the args
input_file_path = sys.argv[1]
#output_file_path = sys.argv[2]


# char to int
def add(c:str) -> int:
    if c == 't':
        return 5
    elif c == 'p' or c == 'd':
        return 3
    elif c == 'c':
        return 2

# open the input file
with open(input_file_path, 'r') as f:
    context = f.read()


# initialize the score and the output
t1_score = 0
t2_score = 0
output = ""

# summarize the total score
for i in range(0, len(context), 3):
    temp = context[i:i+3]
    if temp[1] == '1':
        t1_score += add(temp[2])
    elif temp[1] == '2':
        t2_score += add(temp[2])

print(str(t1_score) + ":" + str(t2_score))