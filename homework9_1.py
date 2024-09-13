def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    for el in range(end):
        yield func(begin)
        begin += 1

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [4, 9, 16, 25], 'Test2'   #  Я так зрозумів там помилка була в оригінальній перевірці, бо мають бути квадрати чисел
print('OK')