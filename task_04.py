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
