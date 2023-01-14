def fibonacci(i):
  if i == 0:
    return 0
  elif i == 1:
    return 1
  else:
    return fibonacci(i-2)+fibonacci(i-1)

x = int(input('Enter a number to find the fibonacci sequence upto that number: '))

list = []

for i in range(x):
  l = fibonacci(i)
  list.append(l)

print(list)

