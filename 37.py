set1 = { 10, 20, 30, 40, 50 }
set2 = { 30, 40, 50, 60, 70 }

set3=set1.intersection(set2)
print(set3)

set4=set1^set2
print(set4)

set5=set1.symmetric_difference(set2)
print(set5)

if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))
  
