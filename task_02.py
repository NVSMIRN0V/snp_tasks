def coincidence(list=None, range=None):
    result_array = []
    if list == None or range == None:
        return result_array
    for element in list:
        if isinstance(element, (int, float)) and range[0] <= element <= range[len(range) - 1]:
            result_array.append(element)
        else:
            continue
    return result_array
