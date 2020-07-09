def sumn(a,b):
    "Sum of natural numbers within a range"
    s=0
    for i in range(a,b+1):
       s=s+i
    return s
a=int(input("Enter start: "))
b=int(input("Enter end: "))
k=sumn(a,b)
print(k)
