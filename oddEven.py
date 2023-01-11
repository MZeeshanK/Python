i = 1
odd = 0
even = 0

while i<=20:
  if i%2 ==0:
        even += i
  else: 
        odd += i
  i += 1

print('Sum of odd numbers from 1-20: ',odd)
print('Sum of even numbers from 1-20: ',even)