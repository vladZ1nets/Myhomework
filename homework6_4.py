def common_elements():
    numbers3 = set()
    numbers5 = set()
    for num in range(100):
        if num % 3 == 0:
            numbers3.add(num)
        if num % 5 == 0:
            numbers5.add(num)
    intersec = numbers3.intersection(numbers5)
    return intersec
result = common_elements()
print(result)

assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print('ok')
