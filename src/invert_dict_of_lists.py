from collections import defaultdict

def invert_dict_of_lists(data):
    """
    Inverts the keys and values of a given dictionary.

    Args:
        data (dict): A dictionary in which all values are lists.

    Returns:
        dict: A new dictionary in which the keys are the values from the given dictionary, and the values are the keys.
    """
    try:
        new_data = defaultdict(list)
        for key, value in data.items():
            if not isinstance(value, list):
                return 'Invalid input. Dictionary values must be in the form of a list.'
            for element in value:
                new_data[element].append(key)
        return new_data
    except AttributeError:
        return 'Invalid input. Input must be a dictionary.'

