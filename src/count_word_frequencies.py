from collections import defaultdict, Counter
import re

def count_word_frequencies(text):
    """
    Counts word frequencies in a given string.

    Args:
        text (str): A string of text.

    Returns:
        dict: A dictionary with frequency counts for each word in the string.
    """
    word_freq = defaultdict(int)
    if text:
        words = text.lower().split()
        for word in words:
            word = re.sub('[!?.]', '', word)
            word_freq[word] += 1 
    return word_freq


# see alternative solution below using Counter class:

# def count_word_frequencies(text):
#     if not text:
#         return Counter()
#     words = re.findall(r'\b\w+\b', text.lower())
#     return Counter(words)
