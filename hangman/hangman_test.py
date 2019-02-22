import sys
letter = []
numtries = 10
letters_found = 0
wordlist = ["starscream", "megatron"]

def lay_board(wordlist):
    for dash in range(len(wordlist[0])):
        sys.stdout.write ('__ ')
    return

def accept_input(letter):
    print("")
    ip_letter = input()
    if ip_letter not in letter:
        letter.append(ip_letter)
    return

def find_letter_in_word(wordlist, letter, letters_found):
    for pos, char in enumerate(wordlist[0]):
        if char in letter:
            sys.stdout.write(char.upper() + ' ')
            letters_found = letters_found + 1
        else:
            sys.stdout.write('__ ')
    return letters_found

#lay_board(wordlist)

#while letters_found != 10:
letters_found = find_letter_in_word(wordlist, letter, letters_found)
print(letters_found)
accept_input(letter)
letters_found = find_letter_in_word(wordlist, letter, letters_found)
print(letters_found)
accept_input(letter)
letters_found = find_letter_in_word(wordlist, letter, letters_found)
print(letters_found)

