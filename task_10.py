def get_word(start, string):
    word, index = '', start
    while index < len(string) and string[index].isalpha():
        word += string[index]
        index += 1
    return word


def count_words(string):
    result_dict, result_array, current_symbol_index = {}, [], 0
    string = string.lower()
    while current_symbol_index < len(string):
        if string[current_symbol_index].isalpha():
            word = get_word(current_symbol_index, string)
            result_array.append(word)
            current_symbol_index += len(word)
        else:
            current_symbol_index += 1

    for word in result_array:
        result_dict[word] = result_array.count(word)

    return result_dict


# => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))  # => {"doo": 3, "bee": 2}
