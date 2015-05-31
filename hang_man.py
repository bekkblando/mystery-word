import random


def text(file_to_use):  # brings in file
    with open(file_to_use) as file_text:
        text = file_text.read()
        return text


def get_word(text_to_clean, diff):  # Cleans the text
    print("loading")
    clean_text = text_to_clean.lower().split('\n')  # lower text, put in list
    computer_rand = random.choice(clean_text)  # pick random word
    if difficuluty(computer_rand, diff) == True:
        underscore = len(computer_rand) * "_"  # find the length of text
        underscore = list(underscore)  # make the underscore string "____"
        return ((underscore, computer_rand))  # Send the value out in a tuple
    elif difficuluty(computer_rand, diff) == False:
        pass

# For some reason I dont like tuples


def difficuluty(computer_rand, diff):
    # nothing yet
    if get.diff.lower() == "easy":
        if len(computer_rand) >= 4 and len(computer_rand) <= 6:
            return True
        else:
            pass
            # word = get_word((text('/usr/share/dict/words')), "easy")
    if get.diff.lower() == "normal":
        if len(computer_rand) >= 6 and len(computer_rand) <= 10:
            return True
        else:
            pass
            # word = get_word((text('/usr/share/dict/words')), "normal")

    if get.diff.lower() == "hard":
        if len(computer_rand) >= 10:
            return True
        else:
            pass
            # word = get_word((text('/usr/share/dict/words')), "hard")


def game(tuple):  # Main game
    tried_words = []
    underscore = tuple[0]  # Unpack the tuple
    computer_rand = tuple[1]  # Unpack the tuple
    lives = 8  # Starting Lives
    print("Number of Letters " + str(len(computer_rand)))  # Print word length
    checked = False  # Set to False so player lives arent deducted/initalize
    while True:  # This loop is mvp
        if checked is True:  # deducte lives if checked is True
            lives -= 1
            if lives <= 0:  # IF lives is less then 0 or equal to you're done
                print("You Lose The Word is" + computer_rand)
                break
        if checked == "You Win":  # If checked equals win you win
            print("You Win")  # print you win, Do I really need to explain this
            exit()
        print("Guess's Left: " + str(lives))  # Lives left
        Guess = input("Guess a letter ")  # Player Guess
        if is_guess_allowed(Guess, tried_words) == True:
            checked = check_guess(Guess, computer_rand, underscore)  # Run chek
        elif is_guess_allowed(Guess, tried_words) == False:
            checked = False

"""This will check that the user puts in just 1 letter"""


def is_guess_allowed(Guess, tried_words):
    print(not False)
    if Guess.isalpha is not False:
        print("Not a letter")
        return False
    if len(Guess) != 1:
        print("Not that many")
        return False
    if Guess not in tried_words:
        tried_words.append(Guess)
        print(tried_words)
        return True
    elif Guess in tried_words:
        print("Already Guessed")
        print(tried_words)
        return False
    else:
        return True


"""check_guess will check the guess, print the graphics and check if wrong
if the guess is wrong it will return a True if not it will return False"""


def check_guess(Guess, computer_rand, underscore):
    # print(computer_rand.find(Guess))
    if computer_rand.find(Guess) == -1:  # Check if the letters not in the word
        return(True)  # Return true for wrong no need to keep going
    for x in computer_rand:  # Iterate over the word and find letter
        if x == Guess:  # You guessed it
            print("YOU GUESSED IT!")
            print("YOUS RIGHT!")
            for e, i in enumerate(computer_rand):  # Enumerate over
                if Guess == i:
                    underscore[e] = i  # Change underscore index to the letter
                    # print(underscore)  # Display
                    if '_' not in underscore:  # checks if you win
                        return("You Win")
            print(' '.join(underscore))
            return(False)  # Returns false to show you're right

try:  # error checking
    assert isinstance(text('/usr/share/dict/words'), str) == True
    print("Text funciton works")
    assert type(get_word(text('/usr/share/dict/words'))) == tuple
    print("get_word function works")
    assert check_guess('a', 'anna', list('____')) == False
    assert check_guess('b', 'anna', list('____')) == True
    print("check_guess function works")
    print(chr(27) + "[2J")
except:
    print("You have a problem")


def start_game():  # starts the game
    while True:
        start = input("Want to play? y/n ")  # gets input to start game
        start = start.lower()  # lower case words
        if start == 'y':
            get_word()
        if start == 'n':
            break
        else:
            print("Please y or n")


def get_diff():
    diff = input("Easy, Normal, Hard ")
    if diff.lower() == "easy":
        return 'easy'
    if diff.lower() == "normal":
        return 'normal'
    if diff.lower() == "hard":
        return 'hard'
    else:
        print("Thats not a difficuluty try again")

start_game()
