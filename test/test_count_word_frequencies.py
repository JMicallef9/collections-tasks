from src.count_word_frequencies import count_word_frequencies

def test_empty_dict_returned_if_no_input():
    assert count_word_frequencies('') == {}

def test_counts_single_word_instance():
    assert count_word_frequencies('hello') == {'hello': 1}