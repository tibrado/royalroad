# Clean Text Documents for Analizig 
import json
import numpy as np 
from string import punctuation
import nltk
from nltk.text import Text
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer, porter
from nltk.stem.porter import PorterStemmer


def tokenize(document, sentence = False):
    """
    param: 
        String:  document
        Bool  : sentence default words
    return:
        list 
    """
    if(sentence):
        return sent_tokenize(document)
    
    return word_tokenize(document)

# valid english characters 
def valid_word(word):
    '''
    param: lower case string
    return: True if word else False if number.. None if either
    '''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    alpha = True
    
    # Assume word is alphaets 
    if word[0] in alphabets: pass
    elif word[0] in numbers: alpha = False
    else: return None
    
    
    for letter in word:
        # If alpha bets 
        if alpha:
            if letter not in alphabets:
                return None
        else:
            if letter not in numbers:
                return None
    
    return alpha

def clean(list_words):
    """
    param: 
        List: List of strings 
    return:
        List: List with lower_case string, no punctuations, no stop words 
    """
    
    stop_words = stopwords.words('english')
    result = []
    
    # Lower all letters and check if they are valid 
    for word in list_words:
        word = word.lower()      #  make lower
        valid = valid_word(word) # check if word or number
        
        if valid != None: 
            if valid: result.append(word)
            else: result.append('numeric-word')
    
    # remove stop words 
    result = [w for w in result if w not in stop_words]
    
    return result

def stem_lem(list_words, stem = False):
    """
    param: 
        List: List of strings 
    return:
        List: List of strings 
    """
    # Return Porter stem words 
    if(stem):
        ps = PorterStemmer()
        return [ps.stem(w) for w in list_words]
    
    # Return wordnet 
    wn = WordNetLemmatizer()
    return [wn.lemmatize(w) for w in list_words]

def word_freq(list_words):
    """
    param: 
        List: Word list 
    return: 
        Dictionary 
    """
    return nltk.FreqDist(list_words)