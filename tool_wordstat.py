def count_words(string):
    return len(string.split())


def longest_word(string):
    lengths = map(len, string.split())
    return max(lengths)




def run():
    pass    



if __name__ == "__main__":
    run()
