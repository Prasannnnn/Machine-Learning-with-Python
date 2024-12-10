#Data types
'''
Python Data types
integer -> int is an data type it contains 0-100,
floating point -> float it contains 0.5 - 100.99
string -> str -> "Hello World"
boolean -> bool -> True or False
list -> [] -> ["Popcorn Chicken", "Burger", "Double chicken Burger"]
tuple -> () -> ("Popcorn Chicken", "Burger", "Double chicken Burger")
dictionaries -> {Name : "Velu", Age : 23}
set -> {"Popcorn Chicken", "Burger", "Double chicken Burger"}
'''
# #integer
# # i = 65
# # print("this is an integer ",i)
# # print(type(i))
# # #float
# # j = 6.5
# # print("this is an float",j)
# # print(type(j))
# # #string
# # k = "Only thing that could make this day better is ice cream"
# # print("My Quotes is ",k)
# # print(type(k))
# # #boolean
# # l = False
# # print(l)
# # print(type(l))
# #data types
# #list,tuple,set and dictionary

# #lists
# m = ["Jackie Chan","Dragon Booster","Gloriavin Veedu", "Chin Chan","Pokeman","Ninja Hattori", "Ben10"]
# #index
# #      0                   1                 2             3            4          5             6
# print(m)
# #data type
# print(type(m))
# #length of data
# print(len(m))
# #Access lists items
# print(m[2])
# #change lists items
# m[6] = "DANDANDAN"
# print(m)
# print(len(m))
# #multi change lists items
# print(m[2:])
# print(m[:6])
# print(m[2:6])
# #m[2:3]
# #left side starting
# #right side stop before value
# print(len(m))

n = ["Apple","Banana","Cherry","Strawberry","Blueberry"]
print(n)

print(n[1])

n[1] = "Orange"
print(n)
#range of items
n[1:4] = ["Watermelon","Green Apple","Mosawmbi"]
print(n)
print(len(n))
#insert
n.insert(3,"cherry")
print(n)
#add
n.append("Muskmelon")
print(n)
print(len(n))
#extend
o = ["mango","pineapple","papaya"]
n.extend(o)
print(n)
print(len(n))
#extend any iterations
p = ("Kiwi","Orange")
print(p)
print(type(p))
n.extend(p)
print(n)
#Remove lists items
q = ["Watermelon","Kiwi"]
n.extend(q)
print(n)
n.remove("Watermelon")
print(n)

#Remove Specified Index
#pop
n.pop(1)
print(n)
#if did not specify the index , the pop() method removes the last item
n.pop()
print(n)
#delete
del n[1]
print(n)
#delete the list
#del n
#print(n)
#clear the list
n.clear()
print(n)
