'''Березовська А.О 122Б
За s-назвою місяця визначити відповідну пору року.'''
while True:
    from enum import Enum, auto
    class month(Enum):
        January = auto() #1
        February = auto() #2
        March = auto() #3
        April = auto() #4
        May = auto() #5
        June = auto() #6
        July = auto() #7
        August = auto() #8
        September = auto() #9
        October = auto() #10
        November = auto() #11
        December = auto() #12
    class season(Enum):
        Winter = auto() #1
        Spring = auto() #2
        Summer = auto() #3
        Autumn = auto() #4
    while True:
        try:
            s = month[input('month: ')]
            break
        except KeyError:
            print('Error')
        except ValueError:
            print('Error')

    if s == month(12) or s == month(1) or s == month(2):
        s = 1
    elif s == month(3) or s == month(4) or s == month(5):
        s = 2
    elif s == month(6) or s == month(7) or s == month(8):
        s = 3
    else:
        s = 4
    print(f'It is {(season(s))}.')

    answer = input('Do you want to rerun the program? Yes (1), No (something) ')
    if answer == '1':
        continue
    else:
        break
