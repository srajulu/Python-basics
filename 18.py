#mark and grade

p=float(input("Enter marks of Physics: "))
c=float(input("Enter marks of Chemistry: "))        
b=float(input("Enter marks of Biology: "))

avg=(p+c+b)/3

if(avg>80):
    print(avg," Distinction")
elif(avg>60):
    print(avg," First Division")
elif(avg>45):
    print(avg," Second Division")
elif(avg>40):
    print(avg," Pass")
else:
    print(avg," Promotion not granted")
