def popular_words (text, words):
    """
    Рахує кількість потрібних користувачеві слів у тексті і виводить їх у словнику вказуючи кількість.

    :param text: Текст який потрібно проаналізувати.
    :param words: Список слів.
    :return: Виведення словнику.
    """
    text = text.lower().split()
    my_list = {}
    for elem in words:
        my_list[elem] = 0
    for elem in text:
        if elem in my_list:
            my_list[elem] += 1
    return my_list

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
