def sort_list(array):
    if not array:
        return array
    min_max = (min(array),max(array))
    for index in range(len(array)):
        if array[index] == min_max[0]:
            array[index] = min_max[1]
        elif array[index] == min_max[1]:
            array[index] = min_max[0]
    array.append(min_max[0])
    return array

