#odd and even between a range
m=int(input("Enter starting range: "))
n=int(input("Enter end of range: "))
temp=m
print("odd numbers:")
while(temp<=n):
    if(temp%2!=0):
        print(temp,end="\t")
    temp=temp+1
print("\neven numbers:")
while(m<=n):
    if(m%2==0):
        print(m,end="\t")
    m+=1


