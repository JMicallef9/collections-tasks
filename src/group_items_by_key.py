from collections import defaultdict

def group_items_by_key(dict_list, key):
    try:
        new_dict = defaultdict(list)
        for dict in dict_list:
            new_dict[dict[key]].append(dict)
        return new_dict
    except KeyError:
        return 'Invalid key given. Please try again.'
