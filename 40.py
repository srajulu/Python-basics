#Verify A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
#Verify A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)

A={'a','b','d','e'}
B={'b','c','e','f'}
C={'d','e','f','g'}

t1=B.union(C)
t2=A.intersection(t1)
print(t2)

t3=A.intersection(B)
t4=A.intersection(C)

t5=t3.union(t4)
print(t5)

if t5==t2:
    print("Hence proved = A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)")


t1=B.intersection(C)
t2=A.union(t1)
print(t2)

t3=A.union(B)
t4=A.union(C)

t5=t3.intersection(t4)
print(t5)
if(t5==t2):
    print("Hence proved = A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)")
