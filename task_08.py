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