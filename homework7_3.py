def find_unique_value(some_list):
    my_dict = {}
    for num_key in some_list:
        if num_key in my_dict:
            my_dict[num_key] += 1
        else:
            my_dict[num_key] = 1
    for num_key, count in my_dict.items():
        if count == 1:
            return num_key

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")