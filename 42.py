n= {11,12,13,14,15,21,22,23,24,25}
k={}
counte=0
counto=0
for i in n:
    if i%2==0:
        counte+=1
    else:
        counto+=1
k=dict(odd=counto,even=counte)
print(k)
