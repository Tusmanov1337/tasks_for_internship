import re


def is_palindrome(string):
    try:
        result = (re.sub(r'[^a-zA-Z]', '', string)).lower()
    except TypeError:
        result = str(string)

    return result == result[::-1]
