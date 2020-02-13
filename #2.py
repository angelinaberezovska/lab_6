''' Березовська А.О 122Б
Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною
цієї ж суми в гривнях.'''
while True:
    from enum import Enum, auto
    class converter(Enum):
        USD = auto()
        EUR = auto()
        CZK = auto()
        PLN = auto()
    while True:
        try:
            x = float(input('Enter the amount of money: '))
            print('Currency list: USD, EUR, CZK, PLN')
            p = converter[input('Currency: ')]

            break
        except KeyError:
            print('Currency is incorrect')
        except ValueError:
            print('Amount of money is incorrect')

    if p == converter.USD:
        a = 24.58 * x
        print(f'{x} USD is {round(a, 2)} UAH')
    elif p == converter.EUR:
        b = 26.90 * x
        print(f'{x} EUR is {round(b, 2)} UAH')
    elif p == converter.CZK:
        c = 1.08 * x
        print(f'{x} CZK is {round(c, 2)} UAH')
    elif p == converter.PLN:
        d = 6.31 * x
        print(f'{x} PLN is {round(d, 2)} UAH')

    answer = input('Do you want to rerun the program? Yes (1), No (something) ')
    if answer == '1':
        continue
    else:
        break
