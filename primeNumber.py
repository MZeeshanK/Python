num = int(input("Enter a number to check wheter prime or not: "))

i = 2
is_prime = False

if num == 0 or num == 1:
    print(f'{num} is neither prime nor consonant')
elif num == 2:
    print('2 is a prime number')
else:
    while num % i != 0:
        if i == num - 1:
            is_prime = True
        i += 1
    
    if is_prime:
        print(f'{num} is a prime number')
    else: 
        print(f'{num} is a consonant number')