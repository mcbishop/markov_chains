from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as text_corpus_file:
        text_corpus = text_corpus_file.read()
        return text_corpus


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    text_tokens = text_string.split()

    for i in range(len(text_tokens)):
        if i < (len(text_tokens) - 2):
            ngram = (text_tokens[i], text_tokens[i+1])
            if ngram not in chains:
                chains[ngram] = []
            chains[ngram].append(text_tokens[i+2])

    # if we are at end of text, do something else
    print chains 
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
#     """Make a new key out of the second word in the first key and the random word you pulled out from the list of words that followed it.
    

# Look up that new key in the dictionary, and pull a new random word out of the new list.


    text = ""

    first_ngram = choice(chains.keys()) #gather random first tuple
    # second_word = first_ngram[1] #get random list value
    # ngram = (second_word, choice(chains[first_ngram])) #new key is tuple of key[2], list value

    # text += " {}".format(ngram[1])
    ngram = first_ngram

    while ngram in chains:
        #append to text string
        second_word = ngram[1] #get random list value
        print "-------"
        new_key = (second_word, choice(chains[ngram])) #new key is tuple of key[2], list value
        text += " {}".format(new_key[1]) 
        print new_key
        print text
        ngram = new_key

    return text

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file("green-eggs.txt")

# # Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

print random_text
