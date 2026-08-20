def ispalindrome(string):
    if len(string)==0:
        return True
    if string[0]!=string[len(string)-1]:
        return False
    return ispalindrome(string[1:-1])


print (ispalindrome('oyo'))

# is code mai sidha pehle  1st and last letter ko confirm krega agar same nhi hai toh na false aa jayega varna woh 1:-1 se bacha hua string def function mai lega aur yeh string aseise hi repeat hoti rahegi aur age badegi and so on


def power(base,exponent):
    if exponent==0:
        return 1
    return base*power(base,exponent-1)

print(power(2,0))
print(power(2,7))
print(power(2,5))
