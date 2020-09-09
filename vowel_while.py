#count vowel in a string
vowel=['a','e','i','o','u']
count,i=0,0
k=input("Enter string: ")
l=len(k)
while i!=l:
    if(k[i] in vowel):
        count=count+1
    i=i+1
print("Total vowels: ",count)
