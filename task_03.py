def max_odd(_array):
    max_odd_number = None
    for element in _array:
        if isinstance(element, (int, float)):
            if element % 2 != 0 and (max_odd_number is None or element > max_odd_number):
                max_odd_number = element
    return max_odd_number




print(max_odd([1, 2, 3, 4, 4]))  # => 3
print(max_odd([21.0, 2, 3, 4, 4]))  # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))  # => 3
print(max_odd(['ololo', 'fufufu']))  # => None
print(max_odd([2, 2, 4]))  # => None
