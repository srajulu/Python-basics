def sum4(l):
    "Print sum of four numbers"
    s=sum(l)
    return s

l=[]
for i in range(0,4):
  l.append(int(input("Enter num: ")))
k=sum4(l)
print("Sum is: ",k)
