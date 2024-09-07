def is_palindrome(text):
        # беремо з тексту і букви і цифри так як в Test2 є цифра 0
        new_text = ''.join(el.lower() for el in text if el.isalnum())
        return new_text == new_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")