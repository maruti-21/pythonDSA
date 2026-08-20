p=6
k=13
prices=[10,15,23,14,2,15]
count=0
for i in range(len(prices)):
    for j in range(len(prices)):
        if prices[j] - prices[i]==k:
            count+=1

print(count)