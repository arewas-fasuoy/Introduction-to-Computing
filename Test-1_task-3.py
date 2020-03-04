#calculating factorial
def factorial(n):
    fac=1
    i=1
    while i<=n:
        fac=fac*i
        i+=1
    return fac
while(True):
    cont=input('Do you want to continue: ')
    if(cont == 'y'):
        y = input('Enter a number: ')
        print(factorial(int(y)))
    else:
        break
