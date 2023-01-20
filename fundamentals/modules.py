from Modules import convertors
from Modules import maxNumber

print(convertors.cm_to_m(100))

numbers = []

for i in range(5):
    x = int(input('Enter a number to fill in the list: '))

    numbers.append(x)

max = maxNumber.maxNumber(numbers)

print(f'Max number is = {max}')