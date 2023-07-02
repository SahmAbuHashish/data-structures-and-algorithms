def repeated_word(string):
    # Remove punctuation and convert the string to lowercase
    cleaned_string = ''.join(c.lower() if c.isalpha() else ' ' for c in string)

    # Split the cleaned string into a list of words
    words = cleaned_string.split()

    # Create a dictionary to keep track of word frequencies
    word_counts = {}

    # Iterate through the words and check for repetition
    for word in words:
        if word in word_counts:
            # If the word is repeated, return it
            return word
        else:
            # Update the word count
            word_counts[word] = 1

    # If no repeated words are found, return None
    return None