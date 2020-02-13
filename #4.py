'''Березовська А.О 122Б
Розробити програму, яка вводить дійсне число t, що означає час в хвилинах, що
минув з початку чергової години і визначає сигнал якого кольору горить для водіїв в цей
момент.'''
while True:
    while True:
        try:
            x = int(input('Enter the minutes: '))
            break
        except ValueError or NameError:
            print('Error')

    if x in range(1, 60):
        if x in range(1, 60, 6) or x in range(2, 60, 6) or x in range(3, 60, 6):
            print(f'GREEN')
        elif x in range(4, 60, 6):
            print(f'YELLOW')
        elif x in range(5, 60, 6) or x in range(6, 60, 6):
            print(f'RED')
    else:
        print('You can choose only from 1 to 59 minutes.')

    answer = input('Do you want to rerun the program? Yes (1), No (something) ')
    if answer == '1':
        continue
    else:
        break
