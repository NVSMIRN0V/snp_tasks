def multiply_numbers(inputs=None):
    inputs = str(inputs)
    result, tmp_result, str_has_digit = None, 1, False

    for sym in inputs:
        if sym.isdigit():
            str_has_digit = True
            tmp_result *= int(sym)

    if str_has_digit:
        result = tmp_result
    return result


print(multiply_numbers())  # => None
print(multiply_numbers('1234##'))  # => 24
print(multiply_numbers('ss$$'))  # => None
print(multiply_numbers('###'))  # => None
print(multiply_numbers('ss'))  # => None
print(multiply_numbers('1234'))  # => 24
print(multiply_numbers('sssdd34'))  # => 12
print(multiply_numbers(2.3))  # => 6
print(multiply_numbers([5, 6, 4]))  # => 120
print(multiply_numbers([[5, 6], [4], 4]))
