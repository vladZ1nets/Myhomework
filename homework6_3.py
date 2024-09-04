def second_index(text, some_str):
    iter_count = 0
    index = -1
    while iter_count < 2:
        index = text.find(some_str, index + 1)
        if index == -1:
            return None
        iter_count += 1
    return index

result = second_index("Hello, hello", "lo")
print(result)
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
