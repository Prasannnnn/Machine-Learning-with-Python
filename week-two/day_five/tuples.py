a = ("apple","pineapple","greenapple","cherry","strawberry")
#tuples are store multiple items in a single variable
#a tuple is collection which is ordered and unchangeable
b = list(a)
print("tuple to lists",b)
b.append("mango")
print("adding values",b)
a = tuple(b)
print("lists to tuple",a)
print(type(a))

#you have to convert the tuple to lists
#use all the lists methods
#output tuple