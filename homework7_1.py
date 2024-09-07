def add_one(some_list):
     some_str = ''.join(str(list_el) for list_el in some_list)
     some_num = int(some_str) + 1
     return [int(num_el) for num_el in str(some_num)]

result = add_one([9])
print(result)

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")