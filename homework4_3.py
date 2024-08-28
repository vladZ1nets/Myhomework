import string

new_hashtag = ''
hashtag = input('Введіть стрічку яку ви хочете перетворити на хештег ').title()

# Проходимо по кожному символу в рядку
for element in hashtag:
    # Забираємо символи які не є пунктуацією і не є пробілами
    if element not in string.punctuation and element != ' ':
        new_hashtag += element

# Додаємо # на початок
new_hashtag = '#' + new_hashtag

# Обрізаємо довжину хештегу до 140 символів
if len(new_hashtag) > 140:
    new_hashtag = new_hashtag[:140]

print(new_hashtag)
