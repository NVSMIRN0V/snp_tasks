def get_values_sum(dict):
    values_sum = 0

    for value in dict.values():
        if isinstance(value, (int, float)):
            values_sum += value

    return values_sum


def connection(dict_1, dict_2):
    result_dict = {}

    for item in dict_1.items():
        if isinstance(item[1], (int, float)) and len(str(item[1])) > 1 and item[1] > 10:
            result_dict[item[0]] = item[1]

    for item in dict_2.items():
        if item[0] not in result_dict.keys():
            if isinstance(item[1], (int, float)) and len(str(item[1])) > 1 and item[1] > 10:
                result_dict[item[0]] = item[1]
            else:
                continue

    return result_dict


def sort_dict(dict):
    sorted_values, result_dict = sorted(dict.values()), {}

    for value in sorted_values:
        for key in dict.keys():
            if dict[key] == value:
                result_dict[key] = value

    return result_dict


def connect_dicts(dict_1, dict_2):
    values_sum_dict_1, values_sum_dict_2 = get_values_sum(dict_1), get_values_sum(dict_2)

    if values_sum_dict_2 >= values_sum_dict_1:  # dict_2 prior
        result_dict = sort_dict(connection(dict_2, dict_1))
    else:  # dict_1 prior
        result_dict = sort_dict(connection(dict_1, dict_2))

    return result_dict