from random import choice
from sys import argv



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
        if i < (len(text_tokens) - n): 
            ngram = tuple(text_tokens[i:i+n]) 
            if ngram not in chains:
                chains[ngram] = []
            chains[ngram].append(text_tokens[i+n]) 

    return chains


def make_text(chains, char_limit):
    """Takes dictionary of markov chains; returns random text.

    Random text will begin with a capital letter.
    
    char_limit will stop word addition loosely (but possibly exceeding)
    the character count.  Text is then truncated, possibly mid word, to enforce that limit.

    """

    text = ""

    first_ngram = choice(chains.keys()) 
    #check to see if choice first index starts with capital letter and is camelcased
    while not ((first_ngram[1][0].isupper())): #and (first_ngram[1][1].islower())):
        first_ngram = choice(chains.keys())

    ngram = first_ngram
    text += ngram[1]
    char_count = 0
    while ((ngram in chains) and char_count < char_limit):
        end_words = ngram[1:] 
        new_word = choice(chains[ngram])
        new_key = end_words+(new_word,) 
        text += " {}".format(new_word)  
        ngram = new_key
        char_count+=len(new_word)
    
    text = text[:char_limit]

    return text

#TODO: new function to slice text at last punctuation of (?!.) before end, while enforcing hard limit of line length

def clean_end(text):
    """Removes text after last occurance of end or near-end punctionation. Defaults to comma or last space if none found. """
 

    punct = (
        ".", 
        ";", 
        "?", 
        "!",
        ":",
        )

    punct_index = [text.rfind(p) for p in punct]
    print punct_index
    cleaned_end = max(punct_index)+1
    if cleaned_end < 1:
        # check for last comma
        comma_index = text.rfind(",")
        cleaned_end = comma_index+1
        #check for last space
        if comma_index < 1:
            space_index = text.rfind(" ")
            cleaned_end = space_index


    text_cleaned = text[:cleaned_end]

    return text_cleaned



input_path, ngram_length_string = argv[1:3] 
ngram_length = int(ngram_length_string)

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(input_text,ngram_length)
#print chains

# # # Produce random text
char_limit = 140
random_text = make_text(chains,char_limit)
print random_text
cleaned_text = clean_end(random_text)
print "-"*80
print cleaned_text
