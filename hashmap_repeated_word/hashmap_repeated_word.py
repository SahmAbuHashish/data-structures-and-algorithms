def repeated_word(string):
    word_counts = {}
    # Iterate through the words and check for repetition
    for word in string.split():
        if word.lower() in word_counts:
            # If the word is repeated, return it
            return word
        else:
            word_counts[word.lower()] = True
    # If no repeated words are found, return None
    return None
