def calculate_diff(dict1, dict2):
    res_dict = {}
    keys = sorted(set(dict1.keys()).union(set(dict2.keys())))
    for key in keys:
        res_dict[key] = define_diff(dict1, dict2, key)
    return res_dict


def define_diff(dict1, dict2, key):
    if isinstance(dict1.get(key), dict) and isinstance(dict2.get(key), dict):
        return {
            'STATUS': 'HASCHILD',
            'CHILDREN': calculate_diff(dict1[key], dict2[key])
        }
    if dict1.get(key) == dict2.get(key):
        return {
            'STATUS': 'UNCHANGED',
            'VALUE': dict1[key]
        }
    if key in dict1.keys() and key not in dict2.keys():
        return {
            'STATUS': 'REMOVED',
            'VALUE': dict1[key]
        }
    if key in dict2.keys() and key not in dict1.keys():
        return {
            'STATUS': 'ADDED',
            'VALUE': dict2[key]
        }
    return {
        'STATUS': 'CHANGED',
        'VALUE1': dict1[key],
        'VALUE2': dict2[key]
    }