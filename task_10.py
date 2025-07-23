import re

def count_words(string):
    result = {}
    cleaned_str = (re.sub(r'[^a-zA-Z]', ' ', string)).lower()
    for word in cleaned_str.split():
        result.setdefault(word, 0)
        result[word] += 1

    return result 


