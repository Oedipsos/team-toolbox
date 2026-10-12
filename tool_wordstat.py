from collections import Counter

VOWELS = "aeiou"

def count_words(text):
    return len(text.split())


def longest_word(text):
    """
    Returns the length of the longest word in given `text`
    """
    lengths = map(len, text.split())
    return max(lengths)


def count_vowels(text):
    """
    Counts the number of vowels in given `text`
    """
    vowels = [c for c in text if c.lower() in VOWELS]
    return len(vowels)


def word_frequency(text):
    """
    Return a Counter object listing each word and its frequency in
    given `text`.
    """
    words = text.lower().split()
    freqs = Counter(words)
    return freqs


def most_frequent_word(text):
    """
    Returns the most common word of given `text`, with its number of
    occurences, packed in a tuple. If `text` is empty, returns None.
    """
    if not text:
        return

    freqs = word_frequency(text)
    return freqs.most_common()[0]


def run():
    user_input = input("Type a sentence: ")
    print(f"Number of words: {count_words(user_input)}")     
    print(f"Longest word: {longest_word(user_input)}")     
    print(f"Number of vowels: {count_vowels(user_input)}")     
    
    w, count = most_frequent_word(user_input)
    print(f"Most frequent word: {w} ({count} times)")     
    

if __name__ == "__main__":
    run()
