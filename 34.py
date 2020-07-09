l=["Swetha","Mazin","Sunder","Navya","Vasanthi"]
print(l)
cin=input("Enter name to append: ")
l.append(cin)
print(l)

k=len(l)
num=int(input("Enter number to use as index: "))
if num>=k:
    print("ERROR : Index out of range")
else:
    print(l[num])
lone=["Kamal","Sanjana"]
l=lone+l
print(l)

name=input("Enter name to check: ") 

if name in l:
    l.remove(name)
else:
    l.append(name)
print("Ordered list:")    #print original list
print(l)
k=len(l)-1

ltwo=[]                 #copy of list in reverse order
while k>=0:
    ltwo.append(l[k])
    k-=1

print("Reverse order")   #print the reverse
print(ltwo)
    
l.pop()   #delete the last element
print(l)   
