Information
Classification: ll
Limited
Access

import sys

letter = []
used_letter = []
numtries = 0
letters_found = 0
ip_letter = ""
wordlist = ["starscream", "megatron"]


def lay_board(wordlist):
    for dash in range(len(wordlist[0])):
        sys.stdout.write('__ ')
    return


def accept_input(letter, ip_letter, used_letter):
    print("")
    ip_letter = input()
    if ip_letter not in letter:
        letter.append(ip_letter)
    return ip_letter


def find_letter_in_word(wordlist, letter, letters_found, ip_letter, numtries):
    for pos, char in enumerate(wordlist[0]):
        if char in letter:
            sys.stdout.write(char.upper() + ' ')
            if char == ip_letter:
                letters_found = letters_found + 1
                if numtries >= 0:
                    numtries = numtries - 1
        else:
            sys.stdout.write('__ ')
    return letters_found, numtries


lay_board(wordlist)
print(len(wordlist[0]))
while letters_found < len(wordlist[0]) and numtries < 10:
    ip_letter = accept_input(letter, ip_letter, used_letter)
    if ip_letter in used_letter:
        print("Letter used. Guess another .. ")
        continue
    else:
        used_letter.append(ip_letter)
    letters_found, numtries = find_letter_in_word(wordlist, letter, letters_found, ip_letter, numtries)
    numtries = numtries + 1
    print("tries: ", numtries)
