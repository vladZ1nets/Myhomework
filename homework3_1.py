first_list = []
nums = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# збираємо усі не нулі у список
for element in nums:
    if element != 0:
        first_list.append(element)

# знаходимо кільк нулів в початковому списку(nums) та додаємо їх у кінець
for element in range(len(nums) - len(first_list)):
    first_list.append(0)

print(first_list)