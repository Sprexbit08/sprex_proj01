import math
n=int(input("Enter the number:"))
print("The square root of number:",math.sqrt(n))
square=n**2
print("The square of nummber:",square)
cube=n**3
print("The cube of number:",cube)
if(n>1):
    for i in range (2,n):
        if (n%i==0):
            print(n,"is not prime number")
            a=[]
            for j in range(1,n+1):
                if(n%j==0):
                    a.append(j)
                a.append(n)
            print("prime factor of the number:")
            print(" ",a)
            break
        else:
            print(n," is an prime number")
            print("prime factor of number:",n)
            break
else:
    print("can not determine whether the number is prime or not")
    print("prime factor of the number is:",n)
print("The factorial; of number:",math.factorial(n))
                
    
