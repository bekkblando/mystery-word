import random


with open('/usr/share/dict/words') as file_text:
    text = file_text.read()


def game(text):
    lives = 8
    clean_text = text.lower().split('\n')
    computer_rand = random.choice(clean_text)
    underscore = len(computer_rand) * "_"
    underscore = list(underscore)
    print("Number of Letters " + str(len(computer_rand)))
    print("Welcome to Jurassic Park")
    wrong = False
    while True:
        if wrong is True:
            lives -= 1
            if lives <= 0:
                print("You Lose The Word is" + computer_rand)
                break
        print("Guess's Left: " + str(lives))
        Guess = input("Guess a letter ")
        #print(computer_rand)
        wrong = True
        for x in computer_rand:
            if x == Guess:
                print("YOU GUESSED IT!")
                print("YOUS RIGHT!")
                wrong = False
                # print(computer_rand.find(Guess))
                for e, i in enumerate(computer_rand):
                    if Guess == i:
                        underscore[e] = i
                        print(underscore)
                        print(''.join(underscore))
                        if '_' not in underscore:
                            return("You Win")
                # print("Guess's Left '" + lives)
                # print("Not there")



print(game(text))
