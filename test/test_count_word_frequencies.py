from src.count_word_frequencies import count_word_frequencies

def test_empty_dict_returned_if_no_input():
    assert count_word_frequencies('') == {}

def test_counts_single_word_instance():
    assert count_word_frequencies('hello') == {'hello': 1}

def test_counts_multiple_words():
    assert count_word_frequencies('hello world') == {'hello': 1, 'world': 1}

def test_counts_multiple_instances_of_same_word():
    assert count_word_frequencies('hello world hello') == {'hello': 2, 'world': 1}

def test_ignores_capital_letters():
    assert count_word_frequencies('Hello world hello') == {'hello': 2, 'world': 1}

def test_filters_out_punctuation_chars():
    text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
    assert count_word_frequencies(text) == {'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 2, 'was': 1, 'not': 1, 'amused': 1}