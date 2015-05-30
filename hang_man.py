import random


def text(file_to_use):
    with open(file_to_use) as file_text:
        text = file_text.read()
        return text


def get_word(text_to_clean):
    clean_text = text_to_clean.lower().split('\n')
    computer_rand = random.choice(clean_text)
    underscore = len(computer_rand) * "_"
    underscore = list(underscore)
    return (underscore, computer_rand)


def game(tuple):
    underscore = tuple[0]
    computer_rand = tuple[1]
    lives = 8
    print("Number of Letters " + str(len(computer_rand)))
    checked = False
    while True:
        if checked is True:
            lives -= 1
            if lives <= 0:
                print("You Lose The Word is" + computer_rand)
                break
        if checked == "You Win":
            print("You Win")
            exit()
        print("Guess's Left: " + str(lives))
        Guess = input("Guess a letter ")
        # print(computer_rand)
        checked = check_guess(Guess, computer_rand, underscore)


def check_guess(Guess, computer_rand, underscore):
    if computer_rand.find(Guess) == -1:
        return(True)
    for x in computer_rand:
        if x == Guess:
            print("YOU GUESSED IT!")
            print("YOUS RIGHT!")
            # print(computer_rand.find(Guess))
            for e, i in enumerate(computer_rand):
                if Guess == i:
                    underscore[e] = i
                    print(underscore)
                    print(''.join(underscore))
                    if '_' not in underscore:
                        return("You Win")
            return(False)
                # print("Guess's Left '" + lives)
                # print("Not there")

game(get_word(text('/usr/share/dict/words')))
