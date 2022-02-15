import random

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

themes = ["Animals", "Colours", "Vehicles", "Fruits", "Countries", "Cities", "Metals", "Musical Instruments", "Verbs", "Languages"] # themes
chosen_theme = random.choice(themes)
print("The theme is:", chosen_theme)

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

length = len(word) # length of word
lengthstr = str(length) # length of word as string

guesscount = 0 # number of guesses

blanks = "_ " * length # blanks for the word blanks

letters_guessed = [] # letters guessed

originalword = word

def game(): # game function
    global guesscount
    global blanks
    global letters_guessed
    global word
    global length
    global lengthstr
    global chosen_theme
    global originalword
    guess = input("The word is " + lengthstr + " characters long."" The theme is " + chosen_theme + "\n" + blanks + " Enter your guess: ")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Enter a single letter. \n\n############################################################################################################\n")
        game()
 
    elif guess in word: # if correct guess
        letters_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        if (length % 2) == 0:
            blanks = blanks[:index-1] + guess + blanks[index + 1:]
        else:
            blanks = blanks[:index] + guess + blanks[index + 1:]
        print(blanks + "\n")
        game()
 
    elif guess in letters_guessed: # if guess is repeated
        print("You've tried this already. Here's a recap of your guesses so far:" + str(letters_guessed) + "\n\n############################################################################################################\n")
        game()

    else: # if guess is wrong
        guesscount = guesscount + 1
        letters_guessed.extend([guess])
        if guesscount == 1:
            print(hangmanlogo1)
            print("Wrong guess. " + str(7 - guesscount) + " guesses remaining\n\n############################################################################################################\n")
 
        elif guesscount == 2:
            print(hangmanlogo2)
            print("Wrong guess. " + str(7 - guesscount) + " guesses remaining\n\n############################################################################################################\n")
 
        elif guesscount == 3:
           print(hangmanlogo3)
           print("Wrong guess. " + str(7 - guesscount) + " guesses remaining\n\n############################################################################################################\n")
 
        elif guesscount == 4:
            print(hangmanlogo4)
            print("Wrong guess. " + str(7 - guesscount) + "guesses remaining\n\n############################################################################################################\n")
 
        elif guesscount == 5:
            print(hangmanlogo5)
            print("Wrong guess. " + str(7 - guesscount) + "guesses remaining\n\n############################################################################################################\n")

        elif guesscount == 6:
            print(hangmanlogo6)
            print("Wrong guess. " + str(7 - guesscount) + "guess remaining.\n\n############################################################################################################\n")

        elif guesscount == 7:
            print(hangmanlogo7)
            print("Game over, thanks for playing!\n")
            print("The word was: " + originalword)

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
    
    elif guesscount != 7:
        game()

print("Welcome to Hangman by LuthHaidar!") # Welcome message
print("The rules are:")
print("You have to guess a word letter by letter.")
print("The length and theme of the word will be provided.")
print("You have 7 chances to guess the word. Your correct guesses will be displayed.")
print("If you guess the word, you win.")

want_to_play = input("Do you want to play? (y/n):") # ask if you want to play
if want_to_play == "y":
    print("Let's play!")
    game()
elif want_to_play == "n":
    print("Bye!")