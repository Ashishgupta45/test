from nltk.stem.snowball import SnowballStemmer
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
import nltk

def remove_punctuation(text):
    '''a function for removing punctuation'''
    import string
    #replace the punctuation with no space
    #which in effect deletes the punctuation marks
    translator = str.maketrans("", "", string.punctuation)
    #return the text stripped of punctuation marks
    return text.translate(translator)

nltk.download("stopwords")
sw = stopwords.words("english")

def stopwords(text):
    '''a function for removing the stopwords'''
    #removing the stopwords and lowercasing the selected words
    text = [word.lower() for word in text.split() if word.lower() not in sw]
    #joing the list of words with space seperator 
    return " ".join(text)

# create an object of stemming function
stemmer = SnowballStemmer("english")

def stemming(text):    
    '''a function which stems each word in the given text'''
    text = [stemmer.stem(word) for word in text.split()]
    return " ".join(text) 
    