def primecheck(num):
    if num>1:
        for i in range(2, int(num/2)+1):
            if(num%i ==0):
                return False
        else:
            return True
    else:
        return False
n= int(input("Enter a number: "))
if(primecheck(n)):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")