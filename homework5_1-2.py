import string

letter = input('Введіть дві букви латиницею та через дефіс: ').strip()
start = letter[0]
end = letter[2]
letters = string.ascii_letters
result = letters[letters.index(start):letters.index(end) + 1]
print(result)


#Ex2
sec = int(input('Введіть кількість секунд, яку хочете перевести: '))

days, remainder = divmod(sec, 86400)  # розділяє секунди на дні і залишок
hours, remainder = divmod(remainder, 3600)  # розділяє залишок на години і залишок
minutes, seconds = divmod(remainder, 60)  # розділяє залишок на хвилини і залишок (секунди)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and days % 100 != [12, 13, 14]:
    day_word = "дні"
else:
    day_word = "днів"
# zfill гарантує, що години, хвилини і секунди завжди мають два знаки
result2 = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

print(result2)
