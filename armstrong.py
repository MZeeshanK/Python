number = int(input('Enter a desired digit number: '))

n = number 
result = 0

while n != 0:
  digit = n % 10
  n = n //10

  result = result + (digit ** 3)

if result == number:
  print(f'{number} is an armstrong number')
else:
  print(f'{number} is not an armstrong number')