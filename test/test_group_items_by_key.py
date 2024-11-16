from src.group_items_by_key import group_items_by_key

def test_reformats_dict_with_one_item():
    input = [
    {'type': 'fruit', 'name': 'apple'}]
    key = 'type'
    result = {
        'fruit': [{'type': 'fruit', 'name': 'apple'}]
    }
    assert group_items_by_key(input, key) == result

def test_handles_multiple_dicts_with_same_key_value():
    input = [
    {'type': 'fruit', 'name': 'apple'},
    {'type': 'fruit', 'name': 'banana'}]
    key = 'type'
    result = {
        'fruit': [{'type': 'fruit', 'name': 'apple'}, 
                  {'type': 'fruit', 'name': 'banana'}]
    }
    assert group_items_by_key(input, key) == result

def test_handles_single_dicts_with_different_key_values():
    input = [
    {'type': 'fruit', 'name': 'apple'},
    {'type': 'vegetable', 'name': 'carrot'}]
    key = 'type'
    result = {
        'fruit': [{'type': 'fruit', 'name': 'apple'}],
        'vegetable': [{'type': 'vegetable', 'name': 'carrot'}]
    }
    assert group_items_by_key(input, key) == result

def test_handles_multiple_dicts_with_different_key_values():
    input = [
    {'type': 'fruit', 'name': 'apple'},
    {'type': 'vegetable', 'name': 'carrot'},
    {'type': 'fruit', 'name': 'banana'},
    {'type': 'vegetable', 'name': 'courgette'}]
    key = 'type'
    result = {
        'fruit': [{'type': 'fruit', 'name': 'apple'}, 
                  {'type': 'fruit', 'name': 'banana'}],
        'vegetable': [{'type': 'vegetable', 'name': 'carrot'},
                      {'type': 'vegetable', 'name': 'courgette'}]
    }
    assert group_items_by_key(input, key) == result

def test_empty_dictionary_returned_if_input_empty():
    assert group_items_by_key([], 'type') == {}

def test_error_message_returned_if_key_not_valid():
    input = [
    {'type': 'fruit', 'name': 'apple'},
    {'type': 'vegetable', 'name': 'carrot'},
    {'type': 'fruit', 'name': 'banana'},
    {'type': 'vegetable', 'name': 'courgette'}]
    assert group_items_by_key(input, 'size') == 'Invalid key given. Please try again.'