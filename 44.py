#function area of circle
def area(r):
    "Area of circle"
    a=3.14*r*r
    return a
k=int(input("Enter radius: "))
k=area(k)
print("Circle area : ",k)
