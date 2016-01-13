from random import choice
from sys import argv

ngram_length = 3


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as text_corpus_file:
        text_corpus = text_corpus_file.read()
        return text_corpus


def make_chains(text_string,ngram_length):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    n = ngram_length

    chains = {}

    text_tokens = text_string.split()

    for i in range(len(text_tokens)):
        if i < (len(text_tokens) - n): # stop at ngram length before end 
            ngram = tuple(text_tokens[i:i+n]) #creates ngram
            if ngram not in chains:
                chains[ngram] = []
            chains[ngram].append(text_tokens[i+n]) #index is based on ngram length

    return chains


def make_text(chains,ngram_length):
    """Takes dictionary of markov chains; returns random text."""
    n = ngram_length

    text = ""

    first_ngram = choice(chains.keys()) 
    ngram = first_ngram
    counter = 0
    while ((ngram in chains) and counter < 500):
        second_word = ngram[1] #ngram end references
        new_key = (second_word, choice(chains[ngram])) #ngram end reference; creates new key as tuple of two words 
        text += " {}".format(new_key[1])  #index based on ngram length
        ngram = new_key
        counter +=1

    return text

input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(input_text,ngram_length)
print chains

# # # Produce random text

#random_text = make_text(chains,ngram_length)

#print random_text
