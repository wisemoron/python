import sys
import colorama, random
import urllib.request
keep_playing = 'Y'

word_used = []
wordlist2 = []
wordlist = ["Mansoor Bhai", "Girdhar Niwas", "Rashid Wadia", "Janata Book Depot", "Theobroma", "Sahakari Bhandar", "Cafe Royal",
            "Trattoria", "Strand Book Depot", "Colaba Market", "Radio Club", "Electric House", "Regal Cinema", "Bade Miyan",
            "Gateway of India", "Apollo Bunder", "The Scholar High School", "Campion", "Madras Cafe", "Kailash Parbat", "Navy Nagar",
            "Sasoon Dock", "Cafe Mondegar", "Cafe Leopold", "Tetsuma", "Bayview Cafe"]

losing_taunts = ["Shame on you. Seriously.", "LOOOOSEERRR!", "Hey outsider who's never lived in Colaba - ", "WOW. You know NOTHING.",
                 "Sheeesh, how are you still alive? ", "Wrong Hangman game. You need the Iceland version. Fewer places."]

winning_taunts = ["Fine. You did it. Bleh.", "So you lived in Colaba. You knew the answer. Big deal!", "CLAP ... CLAP.. CL..AP",
                  "Check out the big brains, eh? Quick what's the root of 349 .. ", "Okay, well done. *yawn*",
                  "NOICE! What .. you expecting a reward or something now?"]
colorama.init()
def layout_settings():
#    sys.stderr.write('\x1b[2J\x1b[H')
    print(chr(27) + "[2J")
    sys.stdout.write('\n' * 11)
    print("\t\t\t\t H A N G M A N: The Colaba Edition")
    print("\t\t\t\t==================================\n\n")
    sys.stdout.write('\t' * 4)

    return

def choose_word(wordlist, word_used):
    index = -1
    while index not in word_used:
        if len(wordlist) == len(word_used):
            index = -1
            break
        index = random.randint(0, len(wordlist) - 1)
        if index in word_used:
            index = -1
            continue
        word_used.append(index)
    return index

def choose_losing_taunt(losing_taunts):
    index = random.randint(0, len(losing_taunts) - 1)
    return index

def choose_winning_taunt(winning_taunts):
    index = random.randint(0, len(winning_taunts) - 1)
    return index


def lay_board(word):
    counter = 0
    layout_settings()
    sys.stdout.write("\n\n\t\t\t\tTries: " + str(numtries) + "\n\n\t\t\t\t")
    for pos in range(len(word)):
        if word.find(' ', pos) == pos:
            space_positions.append(pos)

    for dash in range(len(word)):
        if len(space_positions) > 0 and dash == space_positions[counter]:
            sys.stdout.write('   ')
            if counter + 1 < len(space_positions):
                counter = counter + 1
        else:
            sys.stdout.write('__ ')
    return


def accept_input(letter, ip_letter, used_letter):
    ip_letter = input("\n\t\t\t\tGo on. Take a guess: ")
    if ip_letter[0] not in letter:
        letter.append(ip_letter[0])
    return ip_letter[0]


def find_letter_in_word(word, letter, letters_found, ip_letter, numtries):
    counter = 0
    found_letter = 0
    layout_settings()
    for pos, char in enumerate(word):
        if char.lower() in letter or char in letter:
            sys.stdout.write(char.upper() + '  ')
            if (char.lower() == ip_letter[0] or char == ip_letter[0])\
                    and (ip_letter[0] not in used_letter):
                letters_found = letters_found + 1
                found_letter = 1
        else:
            if len(space_positions) > 0 and pos == space_positions[counter]:
                sys.stdout.write('   ')
                if counter + 1 < len(space_positions):
                    counter = counter + 1
            else:
                sys.stdout.write('__ ')

    if numtries >= 0 and found_letter == 1:
        numtries = numtries - 1
    return letters_found, numtries

def populate_wordlist_from_url(wordlist, listurl):
    with urllib.request.urlopen(listurl) as url:
        for line in url:
            line_words = line.decode('utf-8').split('\\n') # handles the b' at the beginning
            for word in line_words:
                wordlist.append(word.replace('\n', ''))
    return


populate_wordlist_from_url(wordlist2, "https://raw.githubusercontent.com/wisemoron/python/master/hangman/test_wordlist.txt")

while keep_playing == "Y":
    index = choose_word(wordlist2, word_used)
    if index == -1:
        print("\n\n\t\t\t\tAll words attempted!")
        break
    word = wordlist2[index]
    space_positions = []
    letter = []
    used_letter = []
    numtries = 0
    letters_found = 0
    ip_letter = ""
    lay_board(word)

    while letters_found < (len(word) - len(space_positions)) and numtries < 10:
        ip_letter = accept_input(letter, ip_letter, used_letter)
        if ip_letter[0] in used_letter:
            letters_found, numtries = find_letter_in_word(word, letter, letters_found, ip_letter[0], numtries)
            print("\n\n\t\t\t\tLetter used. Guess another .. ")
            continue
        else:
            letters_found, numtries = find_letter_in_word(word, letter, letters_found, ip_letter[0], numtries)
            numtries = numtries + 1
            used_letter.append(ip_letter[0])
            print("\n\n\t\t\t\tTries: ", numtries)

    if numtries == 10:
        print("\n\t\t\t\t" + losing_taunts[choose_losing_taunt(losing_taunts)] + " The answer is: ", word)
    elif letters_found == (len(word) - len(space_positions)) and numtries < 10:
        print("\n\t\t\t\t", winning_taunts[choose_winning_taunt(winning_taunts)])


    keep_playing = input("\n\t\t\t\tAnother one? ").upper()