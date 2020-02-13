'''Березовська А.О 122Б
За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати
наявність високосних років'''
while True:
    while True:
        try:
            d, m, y = int(input('Enter the day: ')), int(input('Enter the month: ')), int(input('Enter the year: '))
            break
        except ValueError or NameError:
            print('You should enter only the numbers')

    days = range(1, 32)
    months = range(1, 13)
    years = range(1901, 2021)
    years_sp = range(1904, 2021, 4)
    if y in years and m in months:

            if m in range(1, 8, 2) or m in range(8, 13, 2):
                if d in days:
                    if m == 1 and d == 1:
                        ld, lm, ly, nd, nm, ny = 31, 12, y-1, d+1, m, y
                    elif m == 3 and d == 1:
                        if y in years_sp:
                            ld, lm, ly, nd, nm, ny = 29, m-1, y, d+1, m, y
                        else:
                            ld, lm, ly, nd, nm, ny = 28, m-1, y, d+1, m, y
                    elif m == 12 and d == 31:
                        ld, lm, ly, nd, nm, ny = d-1, m, y, 1, 1, y+1
                    elif m == 8 and d == 1:
                        ld, lm, ly, nd, nm, ny = 31, m-1, y, d+1, m, y
                    elif d == 1:
                        ld, lm, ly, nd, nm, ny = 30, m-1, y, d+1, m, y
                    elif d == 31:
                        ld, lm, ly, nd, nm, ny = d-1, m, y, 1, m+1, y
                    else:
                        ld, lm, ly, nd, nm, ny = d-1, m, y, d+1, m, y
                    print(f'The last day is {ld}.{lm}.{ly}.', f'The next day is {nd}.{nm}.{ny}', sep='\n')
                else:
                    print('There are only 31 days in this month.')
            elif m == 2:
                if y in years_sp:
                    if d in range(1, 30):
                        if d == 1:
                            ld, lm, ly, nd, nm, ny = 31, m-1, y, d+1, m, y
                        elif d == 29:
                            ld, lm, ly, nd, nm, ny = d-1, m, y, 1, m+1, y
                        else:
                            ld, lm, ly, nd, nm, ny = d-1, m, y, d+1, m, y
                        print(f'The last day is {ld}.{lm}.{ly}.', f'The next day is {nd}.{nm}.{ny}', sep='\n')
                    else:
                        print(f'There are only 29 days in this month {y} year.')
                else:
                    if d in range(1, 29):
                        if d == 1:
                            ld, lm, ly, nd, nm, ny = 31, m-1, y, d+1, m, y
                        elif d == 29:
                            ld, lm, ly, nd, nm, ny = d-1, m, y, 1, m+1, y
                        else:
                            ld, lm, ly, nd, nm, ny = d-1, m, y, d+1, m, y
                        print(f'The last day is {ld}.{lm}.{ly}.', f'The next day is {nd}.{nm}.{ny}', sep='\n')
                    else:
                        print(f'There are only 28 days in this month {y} year.')
            else:
                if d in range(1, 31):
                    if d == 1:
                        ld, lm, ly, nd, nm, ny = 31, m-1, y, d+1, m, y
                    elif d == 30:
                        ld, lm, ly, nd, nm, ny = d-1, m, y, 1, m+1, y
                    else:
                        ld, lm, ly, nd, nm, ny = d-1, m, y, d+1, m, y
                    print(f'The last day is {ld}.{lm}.{ly}.'
                          f'The next day is {nd}.{nm}.{ny}')
                else:
                    print('There are only 30 days in this month.')

    else:
        print('Error')

    answer = input('Do you want to rerun the program? Yes (1), No (something) ')
    if answer == '1':
        continue
    else:
        break
