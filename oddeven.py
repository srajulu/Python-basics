sumo,sume=0,0
m=int(input("Enter m: "))
n=int(input("Enter n:"))

for i in range(m,n):
    if(i%2==0):
        sumo+=i
    else:
        sume+=i
print("sum of odd numbers ",sumo)
print("sum of even numbers ",sume)
