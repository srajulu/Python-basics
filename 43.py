#FUNCTION AREA OF RECTANGLE

def area(l,b):
    "Area of rectangle"
    a=l*b
    return a
l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
k=area(l,b)
print("Area of rectangle: ",k)
