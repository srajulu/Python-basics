import numpy as np
b=np.genfromtxt("E:\Book1.csv",delimiter=",")
#print("Imported data")
#print(b)

a=b[1:8,1:7]
#print(a)

print("Total individual sales: ")
print(np.sum(a,1))

print("Maximum of each salesman: ")
print(np.max(a,1))

print("Sales of vikas for all months")
c=a[4,:]
print(c)

print("sales data of Ajit for the month of Apr, May, Jun")
c=a[3,3:]
print(c)

print("Sales in april for all salesmen")
c=a[:,3]
print(c)

print("Sales for Feb and June")
print("Feb")
print(a[:,1])
print("June")
print(a[:,5])

print("average of each salesperson")
print(np.average(a,axis=1))

print("Minimum of each person")
print(np.min(a,axis=1))

print("Maximum of each month")
print(np.max(a,axis=0))
