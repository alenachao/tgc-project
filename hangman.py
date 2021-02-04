"""
THE GAME OF HANGMAN

P1 will input a word for P2 to guess.

P2 will guess letters (or the word/phrase if they think they know it) until they lose (earn too many strikes) or win (they guess the word/phrase)

If P2 guesses an incorrect letter, they get 1 strike. If Player 2 guesses the inccorect word/phrase, they get 2 strikes!
"""

welcome = """
* * * * * * * * * * * * * * *
Welcome to the game of hangman!
Rules: P1 will input a word/phrase for P2 to guess. P2 will guess a letter or the word/phrase
An incorrect letter is 1 body part while an incorrect guess of the word/phrase is 2 body parts!
If the stick man is fully drawn, P1 wins. If P2 guesses the word, P2 wins. Good luck and have fun!
* * * * * * * * * * * * * * *
"""
print(welcome)

input("Press enter to start")
secret = input("P1: input a word or phrase for P2 to guess! ").upper() # so guesses are not case sensitive
print("\n"*20)
correct_guesses = ' '
incorrect_guesses = ' '
strikes = 0

def print_after_guess(correctness):
    if correctness == "skip": # for when it prints before P2 has guessed
        pass
    else:
        print(correctness + "! Incorrect Guesses:" + incorrect_guesses)

    # optional: printing stick man based on strikes
    if strikes == 0:
        picture = """
 |  T
 |
 |
___
"""
    elif strikes == 1:
        picture = """
 |  T
 |  O
 |
___
"""
    elif strikes == 2:
        picture = """
 |  T
 |  O
 |  |
___
"""
    elif strikes == 3:
        picture = """
 |  T
 |  O
 | /|
___
"""
    elif strikes == 4:
        picture = """
 |  T
 |  O
 | /|\\
___
"""
    elif strikes == 5:
        picture = """
 |  T
 |  O
 | /|\\
___/
"""
    else:
        picture = """
 |  T
 |  O
 | /|\\
___/ \\
"""
        print(picture)
        print("P1 wins! The word/phrase was " + secret)
        return
    print(picture)
    
    #if letter in SECRET has been guessed by P2, it will be printed. Otherwise _ will be printed
    for letter in secret:
        if letter == " ":
            print(" ", end = " ")
        elif letter in correct_guesses:
            print(letter, end = " ")
        else:
            print("_", end = " ")

print_after_guess("skip")
while strikes < 6:
    print("\n")
    guess = input("P2: guess a letter or the word/phrase if you think you know it: ").upper()
    if len(guess) == 1:
        if secret.find(guess) == -1:
            incorrect_guesses += guess + " "
            strikes += 1
            print_after_guess("Incorrect")
        else:
            correct_guesses += guess + " "
            print_after_guess("Correct")
    else:
        if guess == secret:
            print("Correct, P2 Wins!")
            break
        else:
            incorrect_guesses += guess + " "
            strikes += 2
            print_after_guess("Incorrect")
