number1 = int(input('First number: '))
number2 = int(input('Second number: '))
symbol = input('Math symbol: ')

match symbol:
    case '+':
        print(number1 + number2)
    case '-':
        print(number1 - number2)
    case '*':
        print(number1 * number2)
    case '/':
          if number2 != 0:
            print(number1 / number2)
          else:
            print('The divisor cannot be equal to 0')
    case _:
        print('incorect')
