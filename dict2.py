#convert two lists into dictionary

Key = [ 'Mango', 'Banana', 'Apple'] 
Value = [40, 50,100] 
res={}
for keys in Key:
        for values in Value:
            res[keys]=values
print(res)
