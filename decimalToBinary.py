num = int(input('Enter the number: '))

binary = 0

i = 1

while num != 0:
  rem = num % 2
  num = num // 2

  binary = rem * i + binary
  i *= 10


print(binary)

  