def break_words(stuff):
    """This function breaks down sentence into words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """This function is sorting words (words is a list)"""
    return sorted(words)

def print_first_word(words):
    """Prints first word and deletes from the sentence"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints last word and deletes it from the sentence"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in full sentence, returns sorted words"""
    return sort_words(break_words(sentence))

def print_first_and_last(sentence):
    """Prints first and last word of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts words, then prints first and last."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
