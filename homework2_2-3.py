my_list = [1, 2, 3]
# Перевірка на порожній список
if my_list:
    my_list.insert(0, my_list[-1])
    my_list.pop()

print(my_list)
my_list1 = [1, 2, 3, 4, 5]
# Додаємо одиницю для того щоб при непаній кількості перший список був більшим
result = [my_list1[:(len(my_list1)+1)//2], my_list1[(len(my_list1)+1)//2:]]
print(result)