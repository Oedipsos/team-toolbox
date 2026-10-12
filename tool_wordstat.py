from collections import Counter

VOWELS = "AEIOU"

def count_words(string):
    return len(string.split())


def longest_word(string):
    lengths = map(len, string.split())
    return max(lengths)


def count_vowels(string):
    vowels = filter(lambda x: x.upper() in VOWELS, string)
    return len(vowels)


def word_frequency(text):
    words = text.split()
    freqs = Counter(words)
    return freqs


def most_frequent_word(text):
    freqs = word_frequency(text)
    return freqs.most_common(1)[0]


def run():
    pass



if __name__ == "__main__":
    run()
