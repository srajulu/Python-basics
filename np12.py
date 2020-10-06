import numpy as np
a= np.array([3,4,6,10,24,89,45,43,46,99,100])

print("elements not divisible by 3:")
d3 = a[a%3!=0]
print(d3)

print("elements divisible by 5:")
d5 = a[a%5==0]
print(d5)

print("Elements of A, which are divisible by 3 and 5:")
print(a[(a%3==0) & (a%5==0)])

print("replacing numbers divisible by 3 with 42")
a[a%3==0]=42
print(a)
