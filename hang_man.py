import random


def text(file_to_use):  # brings in file
    with open(file_to_use) as file_text:
        text = file_text.read()
        return text


def get_word(text_to_clean):  # Cleans the text
    clean_text = text_to_clean.lower().split('\n')  # lower text, put in list
    computer_rand = random.choice(clean_text)  # pick random word
    underscore = len(computer_rand) * "_"  # find the length of text
    underscore = list(underscore)  # make the underscore string "____"
    return (underscore, computer_rand)  # Send the value out in a tuple
# For some reason I dont like tuples


def game(tuple):  # Main game
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
            print("You Win")
            exit()
        print("Guess's Left: " + str(lives))  # Lives left
        Guess = input("Guess a letter ")  # Player Guess
        checked = check_guess(Guess, computer_rand, underscore)  # Run check

"""check_guess will check the guess, print the graphics and check if wrong
if the guess is wrong it will return a True if not it will return False"""


def check_guess(Guess, computer_rand, underscore):
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
                    print(''.join(underscore))  # display graphic
                    if '_' not in underscore:  # checks if you win
                        return("You Win")
            return(False)  # Returns false to show you're right

game(get_word(text('/usr/share/dict/words')))  # Runs it all
