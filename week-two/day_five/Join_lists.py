a = ["a","b","z"]
b = ["c","d",1]
# c = a+b
# print(c)

for x in b:
     
     a.append(x)

print(a)

a.extend(b)
print("extend",a)