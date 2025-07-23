def coincidence(list=None, range=None):
    if list is None or range is None:
        return []
    else:
        for item in list[::-1]:
            if not type(item) in (int, float):
                list.remove(item)
            elif int(item) not in range:
                list.remove(item)

        return list


