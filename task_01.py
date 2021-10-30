def is_palindrome(sentence):
    if not isinstance(sentence, str):
        return False
    else:
        sentence = sentence.lower()
        start_of_line, end_of_line = 0, len(sentence) - 1
        while start_of_line < end_of_line:
            if not sentence[start_of_line].isalpha():
                start_of_line += 1
            elif not sentence[end_of_line].isalpha():
                end_of_line -= 1
            elif sentence[start_of_line] != sentence[end_of_line]:
                return False
            else:
                start_of_line += 1
                end_of_line -= 1
        return True


print(1, is_palindrome("LEvEL"))
print(2, is_palindrome("A man, a plan, a canal -- Panama"))
print(3, is_palindrome("Madam, I'm Adam!"))
print(4, is_palindrome(333))
print(5, is_palindrome("333"))
print(6, is_palindrome(None))
print(7, is_palindrome("Abraca7778876dabra"))
