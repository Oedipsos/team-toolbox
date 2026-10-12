from collections import Counter

VOWELS = "aeiou"

def count_words(text):
    return len(text.split())


def longest_word(text):
    lengths = map(len, text.split())
    return max(lengths)


def count_vowels(text):
    vowels = [c for c in text if c.lower() in VOWELS]
    return len(vowels)


def word_frequency(text):
    words = text.lower().split()
    freqs = Counter(words)
    return freqs


def most_frequent_word(text):
    freqs = word_frequency(text)
    try:
        return freqs.most_common()[0]
    except:
        return None


def run():
    user_input = input("Type a sentence: ")
    print(f"Number of words: {count_words(user_input)}")     
    print(f"Longest word: {longest_word(user_input)}")     
    print(f"Number of vowels: {count_vowels(user_input)}")     
    
    w, count = most_frequent_word(user_input)
    print(f"Most frequent word: {w} ({count} times)")     
    

if __name__ == "__main__":
    run()
