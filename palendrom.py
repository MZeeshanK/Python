n = int(input('Enter the number: '))
# number = n

# rev = 0

# while n != 0:
#   digit = n % 10
#   rev = rev * 10 + digit

#   n = n // 10

# if rev == number:
#   print(f'{number} is palendrom')
# else:
#   print(f'{number} is not palendrom')

number = str(n)

rev = number [::-1]
rev = int(rev)

if n == rev:
  print(f'{number} is a palendrom')
else:
  print(f'{number} is not a palendrom')
