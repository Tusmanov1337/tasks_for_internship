def max_odd(array):
    result = None
    for item in array:
        if result is None and type(item) in (int, float) and item % 2 != 0:
            result = item
        elif (not result is None) and type(item) in (int, float) and item % 2 != 0 and item > result:
            result = item

        elif isinstance(item, list):
            for part in item:
                try:
                    if part > result and part % 2 != 0:
                        result = part
                except:
                    TypeError
    return result

