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


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))  # => [3, 4, 5]
print(coincidence())  # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))  # => [1, 2, 2.5]
