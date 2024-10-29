number=int(input('Enter a number'))
isPrime=True
for i in range(2,number//2+1):
    if number % i ==0:
        isPrime = False
        break
if isPrime:
    print(f'the given number is prime')
else:
    print(f'the given number is not prime')