def max_odd(_array):
    max_odd_number = None
    for element in _array:
        if isinstance(element, (int, float)):
            if element % 2 != 0 and (max_odd_number is None or element > max_odd_number):
                max_odd_number = element
    return max_odd_number
