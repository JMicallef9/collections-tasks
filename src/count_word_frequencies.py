from collections import defaultdict

def count_word_frequencies(text):
    word_freq = defaultdict(int)
    if text:
        word_freq[text] += 1
    return word_freq