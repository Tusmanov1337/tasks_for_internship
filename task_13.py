import time


def cached(seconds=None, size=None):
    cache = {}
    Need_to_check_time = not (seconds is None or type(seconds) != int)
    Need_to_check_size = not (size is None or type(size) != int)

    def cached_func(func):
        def wrapper(*args, **kwargs):
            if Need_to_check_time:
                for key, value in list(cache.items()):
                    if time.time() - value[1] > seconds:
                        cache.pop(key)

            check = args + tuple(kwargs.values())
            if Need_to_check_size and len(cache.keys()) == size and cache.get(check, False) == False:
                del cache[min(cache, key=lambda x: cache[x][1])]
                cache[check] = (func(*args, **kwargs), time.time())

            else:
                if cache.get(check, False) == False:
                    cache[check] = (func(*args, **kwargs), time.time())

            return cache[check][0]

        return wrapper

    return cached_func

