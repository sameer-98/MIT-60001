# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    valid_words = load_words(WORDLIST_FILENAME)
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.message_text = text
        self.valid_words = SubMessage.valid_words
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        shuffled = {}
        for char in vowels_permutation:
            index = vowels_permutation.index(char)
            shuffled[VOWELS_LOWER[index]] = char
            shuffled[VOWELS_UPPER[index]] = char.upper()
        
        for char in CONSONANTS_LOWER:
            shuffled[char] = char
            shuffled[char.upper()] = char.upper()


        return shuffled
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        message = []
        for char in self.message_text:
            if char not in transpose_dict:
                message.append(char)
            else:
                message.append(transpose_dict[char])
        
        return ''.join(message)
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        vowel_permutations = get_permutations(VOWELS_LOWER)
        perm_dict = {}
        for permutation in vowel_permutations:
        
            word = []
            char_dict = self.build_transpose_dict(permutation)
            for char in self.get_message_text():
                if char not in char_dict:
                    word.append(char)
                else:
                    word.append(char_dict[char])
            word = ''.join(word)
            words = []
            for word in word.split():
                if is_word(self.get_valid_words(), word):
                    words.append(word)
            perm_dict[permutation]  = words
        
        scores = {key: len(val) for key, val in perm_dict.items()}
        perm_val = max(scores, key= scores.get)

        if len(perm_dict[perm_val]) == 0:
            return self.get_message_text()
        else:
            return ' '.join(perm_dict[perm_val])
                

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    war_message = SubMessage("Whiskey Tango")
    war_message_permutation = "oieau"
    war_enc_dict = war_message.build_transpose_dict(war_message_permutation)
    print("Original message: ", war_message.get_message_text(), "Permutation:", war_message_permutation)
    print("Expected encryption:","Wheskiy Tenga")
    print("Actual encryption:", war_message.apply_transpose(war_enc_dict))

    soldier_names = SubMessage("Jon and Mark")
    soldier_permutation = "eaiuo"
    soldier_enc_dict = soldier_names.build_transpose_dict(soldier_permutation)
    print("Original message:", soldier_names.get_message_text(), "Permutation:", soldier_permutation)
    print("Expected encryption:", "Jun end Merk")
    print("Actual encryption:", soldier_names.apply_transpose(soldier_enc_dict))

    enc_war_msg = EncryptedSubMessage(war_message.apply_transpose(war_enc_dict))
    print('Expected decryption:','Whiskey Tango')
    print('Actual decryption:', enc_war_msg.decrypt_message())

    enc_soldier_msg = EncryptedSubMessage(soldier_names.apply_transpose(soldier_enc_dict))
    print('Expected decryption:','Jon and Mark')
    print('Actual decryption:', enc_soldier_msg.decrypt_message())
