from collections import defaultdict

def group_items_by_key(dict_list, key):
    """
    Groups items from a list of dictionaries by a given key.

    Args:
        dict_list (list): A list of dictionaries.
        key (str): A key from the given dictionaries.

    Returns:
        dict: A new dictionary with items grouped by the specified key.
    """
    try:
        new_dict = defaultdict(list)
        for dict in dict_list:
            new_dict[dict[key]].append(dict)
        return new_dict
    except KeyError:
        return 'Invalid key given. Please try again.'
