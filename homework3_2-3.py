second_list = []
my_sum = 0
for my_index in range(0, len(second_list), 2):
    my_sum += second_list[my_index]

if second_list:
    print(my_sum * second_list[-1])
else:
    #  якщо список порожній
     print(0)

# 3-тє завдання
import random
# встановлюємо рандомну двжину списку з 3 до 10
count_of_el = random.randint(3, 10)
third_list = []
# додаємо рандомні елементи значенням з 3 до 10
for nums in range(count_of_el):
    third_list.append(random.randint(3, 10))

print(third_list)
# робимо список з трьох елементів (перший, третій і другий з кінця) індекси 0 2 -2
print([third_list[0], third_list[2], third_list[-2]])
