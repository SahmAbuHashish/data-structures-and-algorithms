from hashmap_repeated_word.hashmap_repeated_word import repeated_word

# Test cases for repeated_word function
def test_repeated_word():
    assert repeated_word("Once upon a time, there was a brave princess who...") == "a"
    assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom...") == "it"
    assert repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs...") == "summer"