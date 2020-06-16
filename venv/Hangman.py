import random
import string
from words import words


def get_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def game(word):
    numberofTries = 6
    word = get_word()
    word_list = set(word)
    letterstried = set()
    alphabet = set(string.ascii_uppercase)
    wordcorrect = False
    hints = 0
    while not wordcorrect and numberofTries > 0:
        word_print = [letter if letter in letterstried else '_' for letter in word]
        word_print_list = list(word_print)
        print(' '.join(word_print)) 
        if word_print_list.count('_') == 0:
            wordcorrect = True
            break
        letterguess = input("Guess a letter or type * for a hint: ").upper()
        #print("The word is ", word)
        if letterguess == '*':
            while True:
                if hints < 3:
                    while True:
                        letterhint = random.choice(word)
                        if letterhint not in letterstried:
                            hints += 1
                            print('Hints used: ', hints)
                            break
                else:
                    print('You have used up all 3 of your hints')
                    break
                break
            print(letterhint, ' is in the word')
        elif len(letterguess) == 1 and letterguess.isalpha():
            if letterguess in alphabet - letterstried:
                letterstried.add(letterguess)
                if letterguess not in word_list:
                    numberofTries -= 1
                    print(letterguess, ' is not in the word')
                else:
                    print("Good guess, ", letterguess, " is in the word")
            elif letterguess in letterstried:
                print('You have already used that letter')

        else:
            print("That's not a valid input")
    if numberofTries == 0:
        print('You lose')
    elif wordcorrect is True:
        print('You win!')


def main():
    word = get_word()
    game(word)


if __name__ == '__main__':
    main()


