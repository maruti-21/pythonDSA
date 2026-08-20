def prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input("Enter number: "))

if prime(n):
    print("Prime number")
else:
    print("Not a prime number")
    



p=int(input("Enter the principal amount:"))
t=int(input("Enter the time period:"))
roi=int(input("Enter the rate of interest:"))
ci=p*(1+(roi/100))*t
print("The compound interest is:",ci)