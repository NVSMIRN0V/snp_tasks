def sort_list(list):
    if not list:
        return list
    else:
        result, min_in_list, max_in_list = [], min(list), max(list)
        for el in list:
            if el == max_in_list:
                result.append(min_in_list)
            elif el == min_in_list:
                result.append(max_in_list)
            else:
                result.append(el)
        result.append(min_in_list)
        list = result
    return list


print(sort_list([]))  # => []
print(sort_list([2, 4, 6, 8]))  # => [8, 4, 6, 2, 2]
print(sort_list([1]))  # => [1, 1]
print(sort_list([1, 2, 1, 3]))  # => [3, 2, 3, 1, 1]
