def multiply_numbers(*args):
    result = 1
    flag = False
    for arg in args:
        for item in str(arg):
            try:
                result *= int(item)
                flag = True

            except:
                TypeError

    if flag:
        return result
    else:
        return None
