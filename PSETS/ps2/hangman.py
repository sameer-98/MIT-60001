# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import inflect

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count = 0
    for char in secret_word:
      if char in letters_guessed:
        count += 1
    return count == len(secret_word)



def get_guessed_word(secret_word, correct_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    new_word = []
    for char in secret_word:
        if char in correct_guessed:
            new_word.append(char)
        else:
            new_word.append('_ ')
    return ''.join(new_word)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabets = string.ascii_lowercase
    for char in letters_guessed:
        alphabets = alphabets.replace(char,'')
    return alphabets
    
def update_vals(guesses, warnings, val=1):
  '''

  '''
  if warnings > 0:
      warnings -= val
  else:
      guesses -= val
  return  guesses, warnings

def isvowel(char):
    '''
    
    '''
    return char in ['a', 'e','i','o','u']

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    p = inflect.engine()

    guesses = 6
    warnings = 3
    has_won = False
    score = 0
    letter_guessed = []
    correct_guessed = []

    word_length = len(secret_word)
    print("Welcome to the game Hangman !")
    print(f"I am thinking of a word that is {word_length} letters long")
    print(f"You have {p.no('warning', warnings)}  left.")
    print('-----------------')

    while guesses > 0:
         
        print(f"You have {p.no('guess', guesses)} left.")
        print(f'Available letter: {get_available_letters(letter_guessed)}')

        #Take input from the user 
        guessed = input('Please guess a letter: ')
        

        #Check whether the user has inputted an alphabet
        if not guessed.isalpha():
            guesses, warnings = update_vals(guesses, warnings)
            print(f"Oops! That is not a valid letter. You have {p.no('warning', warnings)} left: ", end='')
        else:
            guessed = guessed.lower()
             #If the user has already guessed the letter previously
            if guessed in letter_guessed:
                guesses, warnings = update_vals(guesses, warnings)
                print(f"Oops! You've already guessed that letter. You have {p.no('warning', warnings)} left: ", end='')
            #If the user has guessed incorrectly consonent or a vowel
            elif guessed not in secret_word:
                if isvowel(guessed):
                    guesses -= 2
                else:
                    guesses -= 1
                print('Oops! That letter is not in my word: ', end='')
            else:
                print('Good guess: ', end='')
                correct_guessed.append(guessed)

        print(get_guessed_word(secret_word,correct_guessed))    
        print('-----------------')
        letter_guessed.append(guessed)

        if is_word_guessed(secret_word, correct_guessed):
            has_won = True
            score = (guesses) * len(set(correct_guessed)) 
            break
    if has_won:
          print(f'Congratulations, you won!\nYour total score for this game is: {score}')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
  




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    #Replace the spaces with empty string
    word = my_word.replace(' ','')
    #If the two words do not have the same length then false
    if len(word) != len(other_word):
        return False
    else:
        for i in range(len(other_word)):
             if word[i] == '_':
                 continue
             else:
                 char_other_word = other_word[i]
                 char_my_word = word[i]
                 #If the character at the ith position of my word does not match 
                 # the ith position of the other word or if the repeated character is not placed
                 if char_other_word != char_my_word or (other_word.count(char_other_word) != word.count(char_my_word)):
                     return False
    return True       

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=' ')
    print()



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    p = inflect.engine()

    guesses = 6
    warnings = 3
    has_won = False
    score = 0
    letter_guessed = []
    correct_guessed = []

    word_length = len(secret_word)
    print("Welcome to the game Hangman !")
    print(f"I am thinking of a word that is {word_length} letters long")
    print(f"You have {p.no('warning', warnings)}  left.")
    print('-----------------')

    while guesses > 0:
         
        print(f"You have {p.no('guess', guesses)} left.")
        print(f'Available letter: {get_available_letters(letter_guessed)}')

        #Take input from the user 
        guessed = input('Please guess a letter: ')

        if guessed == '*':
            show_possible_matches(get_guessed_word(secret_word, correct_guessed))
            print('-----------------')
            continue

        #Check whether the user has inputted an alphabet
        elif not guessed.isalpha():
            guesses, warnings = update_vals(guesses, warnings)
            print(f"Oops! That is not a valid letter. You have {p.no('warning', warnings)} left: ", end='')
        else:
            guessed = guessed.lower()
             #If the user has already guessed the letter previously
            if guessed in letter_guessed:
                guesses, warnings = update_vals(guesses, warnings)
                print(f"Oops! You've already guessed that letter. You have {p.no('warning', warnings)} left: ", end='')
            #If the user has guessed incorrectly consonent or a vowel
            elif guessed not in secret_word:
                if isvowel(guessed):
                    guesses -= 2
                else:
                    guesses -= 1
                print('Oops! That letter is not in my word: ', end='')
            else:
                print('Good guess: ', end='')
                correct_guessed.append(guessed)

        print(get_guessed_word(secret_word,correct_guessed))    
        print('-----------------')
        letter_guessed.append(guessed)

        if is_word_guessed(secret_word, correct_guessed):
            has_won = True
            score = (guesses) * len(set(correct_guessed)) 
            break
    if has_won:
          print(f'Congratulations, you won!\nYour total score for this game is: {score}')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
