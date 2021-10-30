def combine_anagrams(words_array):
    all_anagrams_inwords_array = []
    current_word = 0
    while current_word < len(words_array) - 1:
        anagrams_for_current_word = [words_array[current_word]]
        supposed_anagram = current_word + 1
        while supposed_anagram < len(words_array):
            if len(words_array[current_word]) == len(words_array[supposed_anagram]):
                if sorted(words_array[current_word]) == sorted(words_array[supposed_anagram]):
                    anagrams_for_current_word.append(words_array[supposed_anagram])
                    words_array.pop(supposed_anagram)
            supposed_anagram += 1
        all_anagrams_inwords_array.append(anagrams_for_current_word)
        current_word += 1
    return all_anagrams_inwords_array


result = combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])
# => [ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"] ]
print(result)
