number = input('Введіть своє число: ')
while int(number) > 9:
    result = 1
    for nums in number:
        result *= int(nums)
    number = str(result)

print(int(number))