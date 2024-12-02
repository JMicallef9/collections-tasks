from src.invert_dict_of_lists import invert_dict_of_lists

def test_empty_dict_returns_empty_dict():
    assert invert_dict_of_lists({}) == {}

def test_inverts_single_key_value_pair():
    assert invert_dict_of_lists({'a': [1]}) == {1: ['a']}

def test_inverts_multiple_key_value_pairs():
    input = {
    'a': [1, 2],
    'b': [2, 3],
    'c': [3, 4]}
    expected = {
    1: ['a'],
    2: ['a', 'b'],
    3: ['b', 'c'],
    4: ['c']}
    assert invert_dict_of_lists(input) == expected

def test_returns_error_message_if_invalid_input_type():
    assert invert_dict_of_lists(['hello world']) == 'Invalid input. Input must be a dictionary.'

def test_returns_error_message_if_dict_incorrectly_formatted():
    assert invert_dict_of_lists({'hello': 'world'}) == 'Invalid input. Dictionary values must be in the form of a list.'