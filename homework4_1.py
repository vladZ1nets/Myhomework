import keyword

variable = input("Введіть свою змінну: ")
if variable[0].isdigit():
    print(False)
elif any(element.isupper() or element in  ['.',',','!','?',';',' '] for element in variable): #список пунктуацій можна продовжувати
    print(False)
elif '__' in variable:
    print(False)
elif variable in keyword.kwlist:
    print(False)
else:
    print(True)
