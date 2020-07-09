#Example
#Input : T1 = {10,30,50 }
#T2= {20,40,60}
#Output :
#T3= {10,20,30,40,50,60}
n=int(input("Enter n: "))
tn=2*n
t1=set()
t2=set()
t3=set()
for i in range(0,n):
    k=int(input("input elements of set1: "))
    t1.add(k)
for i in range(0,n):
    l=int(input("input elements of set2: "))
    t2.add(l)
print(t1)
print(t2)
t3.update(t2)
t3.update(t1)   
print(t3)
    
