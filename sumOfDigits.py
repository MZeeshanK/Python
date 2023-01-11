n = int(input('Enter the 4 digit number: '))
sum = 0

while n != 0:
  digit = n % 10
  sum += digit
  n = n // 10

print("Sum of the digits ", sum)