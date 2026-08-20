def msg():
    print("hello moto")

msg() #calling function 
msg()
msg()


def arithmatic():
    a=int(input("enter the value of A:"))
    b=int(input ("enter th evalue of B:"))
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div

print(arithmatic())
result=arithmatic()
print("arithmatic=",result)




def cityname(city="goa"):
    print(city)
    
    
    
cityname("delhi")
cityname("nagpur")
cityname()