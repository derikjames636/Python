


def factorial(n):
    if n==0:
        return 1
    else :
        return  n*factorial(n-1)
t=int(input('Enter a number'))
f=factorial(t)
print(f)

n1=int(input('Enter a number 1 '))
n2=int(input('Enter number 2 '))
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
a=add_numbers(n1,n2)
print(f'sum of number 1 and number 2 is {a}')


def multiply_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+ multiply_numbers(n1,n2-1)
b=multiply_numbers(n1,n2)
print(f'product of number 1 and number 2 is {b}')

def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
c=gcd(n1,n2)
print(f"gcd of number 1 and number 2 is {c}")

