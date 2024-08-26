# define the function print_upper_words
def print_upper_words(words, must_start_with):
    """print each word starts with h or y in uppercase."""
    for word in words:
        if word[0] in must_start_with:
            print(word.upper())

# call the function
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

# call the function
def print_words_starting_with_e(words):
    """Print words that start with 'e' or 'E' in uppercase."""
    for word in words:
        if word[0] == "e" or word[0] == "E":
            print(word.upper())

# example usage
print_words_starting_with_e(["apple", "Dog", "Eel", "echo", "orange", "peanut", "elephant", "Eagle", "eleven", "elephant", "Eggplant"])


# define the function print_upper_words for A & E
def print_upper_words(words, must_start_with):
    """print each word starts with A or E in uppercase."""
    for word in words:
        if word[0] in must_start_with:
            print(word.upper())


# call the function
print_upper_words(["billy", "Andy", "Edwin", "spencer", "Alfred", "Eddie", "Eve", "Ashley", "Ella", "bill", "adam", "Elijah", "alex", "Ezra"],
                   must_start_with={"A", "E"})