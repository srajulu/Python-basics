#seperate int float and string of list
list1=['Apple','Berry',10,20.4,99.0,199]
lists,listi,listf=[],[],[]

for x in list1:
    if type(x)==str:
        lists.append(x)
    if type(x)==float:
        listf.append(x)
    if type(x)==int:
        listi.append(x)
print(listi)
print(listf)
print(lists)
