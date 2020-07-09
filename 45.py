#function - factorial

def fact(n):
    f=1
    while n>=1:
        f=f*n
        n=n-1
    return f
k=int(input("Enter number to find factorial: "))
n=fact(k)
print("Factorial= ",n)
