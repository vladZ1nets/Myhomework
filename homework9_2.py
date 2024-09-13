import re
def first_word(text):
    """ Пошук першого слова в рядку """
    match = re.search(r"[a-zA-Z']+", text)# шукає всі літери та апострофи які йдуть один за одним та знайшлись першими
    if match:
        return match.group() #  переводить об'єкт типу матч(посилання на знайдений рег виразами обєкт) в рядок тексту
    return ""

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')