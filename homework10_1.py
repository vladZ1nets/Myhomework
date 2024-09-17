def is_prime(num):
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 1
    return True
def prime_generator(end):
    for el in range(2, end + 1):
        if is_prime(el):
            yield el

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')