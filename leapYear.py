number = int(input('Enter the year: '))

condition = number % 4

if condition == 0 and number % 100 != 0: 
    print('Year is a leap year')
else:
    print('year is not leap year')
