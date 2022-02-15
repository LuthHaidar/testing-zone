import random

import random
import sys

# hangman pictures
hangmanlogo1 =('''
  +---+
  |   |
      |
      |
      |
      |
=========
''')
hangmanlogo2 = ('''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''')
hangmanlogo3 = ('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''')
hangmanlogo4 = ('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''')
hangmanlogo5 = ('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''')
hangmanlogo6 = ('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''')
hangmanlogo7 = ('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''') 
 
def setup():
    global guessnum
    global blanks
    global word
    global originalword
    global already_guessed
    global length
    global play_game
    global chosen_theme
    global maxguess

    themes = ["Animals", "Colours", "Vehicles", "Fruits", "Countries", "Cities", "Metals", "Musical Instruments", "Verbs", "Languages"] # themes
    chosen_theme = random.choice(themes)
    
    Animals = ["cat", "dog", "cow", "pig", "horse", "sheep", "goat", "chicken", "monkey", "snake", "lion", "tiger", "elephant", "zebra", "giraffe", "panda", "bear", "deer", "rhino", "polar bear", "elephant", "rhinoceros"] # word bank
    Colours = ["red", "blue", "green", "yellow", "orange", "purple", "brown", "black", "white", "pink", "grey", "beige", "silver", "gold", "magenta", "cyan", "brown", "beige", "silver", "gold", "magenta", "cyan"]
    Vehicles = ["car", "bus", "truck", "motorcycle", "train", "boat", "airplane", "rocket", "submarine", "space ship", "car", "bus", "truck", "motorcycle", "train", "boat", "airplane", "rocket", "submarine", "space ship"]
    Fruits = ["apple", "banana", "pear", "strawberry", "pineapple", "grapes", "watermelon", "peach", "mango", "kiwi", "lemon", "apricot", "cherry", "coconut", "avocado", "peach", "mango", "kiwi", "lemon", "apricot", "cherry", "coconut", "avocado"]
    Countries = ["canada", "usa", "mexico", "argentina", "brazil", "chile", "colombia", "ecuador", "paraguay", "peru", "uruguay", "venezuela", "argentina", "brazil", "chile", "colombia", "ecuador", "paraguay", "peru", "uruguay", "venezuela"]
    Cities = ["toronto", "vancouver", "ottawa", "montreal", "calgary", "edmonton", "toronto", "vancouver", "ottawa", "montreal", "calgary", "edmonton", "toronto", "vancouver", "ottawa", "montreal", "calgary", "edmonton", "toronto", "vancouver", "ottawa", "montreal", "calgary", "edmonton"]
    Metals = ["iron", "copper", "silver", "gold", "platinum", "aluminum", "lead", "zinc", "tin", "bronze", "steel", "iron", "copper", "silver", "gold", "platinum", "aluminum", "lead", "zinc", "tin", "bronze", "steel"]
    Musical_Instruments = ["guitar", "piano", "violin", "drums", "flute", "saxophone", "trumpet", "trombone", "tuba", "guitar", "piano", "violin", "drums", "flute", "saxophone", "trumpet", "trombone", "tuba", "guitar", "piano", "violin", "drums", "flute", "saxophone", "trumpet", "trombone", "tuba"]
    Verbs = ["run", "jump", "swim", "fly", "walk", "climb", "sneak", "hide", "climb", "sneak", "hide", "run", "jump", "swim", "fly", "walk", "climb", "sneak", "hide", "climb", "sneak", "hide", "run", "jump", "swim", "fly", "walk", "climb", "sneak", "hide"]
    Languages = ["english", "spanish", "french", "german", "italian", "russian", "chinese", "japanese", "korean", "arabic", "portuguese"]
    
    if chosen_theme == "Animals": # selecing a word based on theme chosen
        word = random.choice(Animals)
    elif chosen_theme == "Colours":
        word = random.choice(Colours)
    elif chosen_theme == "Vehicles":
        word = random.choice(Vehicles)
    elif chosen_theme == "Fruits":
        word = random.choice(Fruits)
    elif chosen_theme == "Countries":
        word = random.choice(Countries)
    elif chosen_theme == "Cities":
        word = random.choice(Cities)
    elif chosen_theme == "Metals":
        word = random.choice(Metals)
    elif chosen_theme == "Musical Instruments":
        word = random.choice(Musical_Instruments)
    elif chosen_theme == "Verbs":
        word = random.choice(Verbs)
    elif chosen_theme == "Languages":
        word = random.choice(Languages)
    
    length = len(word)
    guessnum = 0
    blanks = '_' * length
    already_guessed = []
    play_game = ""
    originalword = word
    maxguess =  7
 
def game():
    global guessnum
    global blanks
    global word
    global already_guessed
    global play_game
    global originalword
    global chosen_theme
    global maxguess
    
    guess = input("The word is " + str(length) + " letters long and it's theme is " + chosen_theme + "\n" + blanks + " Enter your guess: ") # asking for guess
    
    guess = guess.lower()
    guess = guess.strip() # removing spaces from guess
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9": # checking if guess is valid
        print("Only enter a single letter. No words, numbers, symbols or anyuthing of that sort is allowed in this household. \n")
        game()
    
    elif guess in word: # if the guess is correct
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        blanks = blanks[:index] + guess + blanks[index + 1:]
        print("Correct! " + blanks + "\n")
    
    elif guess in already_guessed: # if the letter has already been guessed
        print("You've already tried this letter before\n")
    
    else: # if the guess is wrong
        guessnum += 1
        if guessnum == 1:
            print(hangmanlogo1)
            print("Oh no! That wasn't quite right. " + str(maxguess - guessnum) + " guesses left\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif guessnum == 2:
            print(hangmanlogo2)
            print("Again!? Well, third time's the charm! " + str(maxguess - guessnum) + " guesses left\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif guessnum == 3:
           print(hangmanlogo3)
           print("Not again! " + str(maxguess - guessnum) + " guesses left\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif guessnum == 4:
           print(hangmanlogo4)
           print("oops. " + str(maxguess - guessnum) + " guesses left\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif guessnum == 5:
           print(hangmanlogo5)
           print("At this point, it can't hurt to keep trying. " + str(maxguess - guessnum) + " guesses left\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif guessnum == 6:
            print(hangmanlogo6)
            print("You'll get em next time. " + str(maxguess - guessnum) + " guess left\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif guessnum == 7:
            print(hangmanlogo7)
            print("Game over, thanks for playing!\n")
            print("The word was: "+ originalword + "\n")
    if word == '_' * length:
        print("Yeah, you won! For your prize you get... \n")
        exit()
    elif guessnum != maxguess:
        game()
 
print("Welcome to Hangman by LuthHaidar!") # Welcome message
print("The rules are:")
print("You have to guess a word letter by letter.")
print("You have 7 chances to guess the word. Your correct guesses will be displayed.")
print("If you guess the word, you win.")
wannaplay = input("Do you want to play? (y/n): ")
if wannaplay == "n":
    print("Goodbye!")
print("Let's play!") 
setup()
game()