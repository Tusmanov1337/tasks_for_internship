def combine_anagrams(array):
    result = {}
    for item in array:
        result.setdefault(''.join(sorted(item)), []).append(item)

    return list(result.values())


