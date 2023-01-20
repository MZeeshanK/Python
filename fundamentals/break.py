i = 1
list = []

while i <= 5:
  x = input('Enter any key')

  if x == 'x':
    break

  list.append(x)

  i += 1

print(list)