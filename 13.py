from pprint import pprint 

inp = input("Please enter a sentence: ")
letters = 0
digits = 0
for i in range(0, len(inp)):
    char = inp[i]
    if ord(char)>=ord('a') and ord(char)<=ord('z'):
        letters += 1
    if ord(char)>=ord('0') and ord(char)<=ord('9'):
        digits += 1
pprint("LETTERS " + str(letters))
pprint("DIGITS " + str(digits))