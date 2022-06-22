def calculate_diff(data1, data2):
    diff = {}
    keys = sorted(set(data1.keys()).union(set(data2.keys())))
    for key in keys:
        diff[key] = generate_key_diff(data1, data2, key)
    return diff


def generate_key_diff(data1, data2, key):
    if isinstance(data1.get(key), dict) and isinstance(data2.get(key), dict):
        return {
            'STATUS': 'HASCHILD',
            'CHILDREN': calculate_diff(data1[key], data2[key])
        }
    if data1.get(key) == data2.get(key):
        return {
            'STATUS': 'UNCHANGED',
            'VALUE': data1[key]
        }
    if key in data1.keys() and key not in data2.keys():
        return {
            'STATUS': 'REMOVED',
            'VALUE': data1[key]
        }
    if key in data2.keys() and key not in data1.keys():
        return {
            'STATUS': 'ADDED',
            'VALUE': data2[key]
        }
    return {
        'STATUS': 'CHANGED',
        'VALUE1': data1[key],
        'VALUE2': data2[key]
    }
