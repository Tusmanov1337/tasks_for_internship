def connect_dicts(dict1, dict2):
    result = {}
    if sum(dict1.values()) > sum(dict2.values()):
        dict2.update(dict1)
        result.update(dict2)

    elif sum(dict1.values()) < sum(dict2.values()) or sum(dict1.values()) == sum(dict2.values()):
        dict1.update(dict2)
        result.update(dict1)

    result = {key: value for key, value in sorted(result.items(), key=lambda x: x[1]) if value > 10}

    return result



