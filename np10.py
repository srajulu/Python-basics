import numpy as np

arr1,arr2=[],[]

print("first matrix")
for i in range(3):
    for j in range(4):
        x=int(input("Element:"))
        arr1.append(x)
arr1=np.reshape(arr1,(3,4))
print("second matrix")
for i in range(3):
    for j in range(4):
        x=int(input("Element:"))
        arr2.append(x)
arr2=np.reshape(arr2,(3,4))
print(np.add(arr1,arr2))


