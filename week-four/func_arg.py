def nam(a,b):
    return a+b

num1 = 5
num2 = 6
print(nam(num1,num2))

def oe(x):
    if x%2==0:
        print("Even")
    else:
        print("odd")

oe(4)
oe(5)

'''
Types of python function Arguments

Default Argument
Keyword Argument
Positional Argument
Arbitrary Argument
'''
#default argument
def fun(x,y=50):
    print("x: ",x)
    print("y: ",y)

fun(10)

#keyword Argument
def student(fname,lname):
    print(fname,lname)

student(fname='Bhuvana',lname="bala")
student(fname="Pranav",lname="Sivaprakash")

#positional Argument

def nameage(name,age):
    print("Hi , I am ",name)
    print("My age is ",age)

nameage("Suraj",27)
nameage(27,"suraj")


#Arbitrary Keyword Arguments
'''
*args (Non Keyword Argument)
**kwargs (Keyword Argument)

'''

def mun(**kargs):
    for keys,values in kargs.items():
        print("%s == %s " % (keys,values))

mun(first = 'Running',second = 'up',third = 'that',fourth ='hill', fifth ='kate',six = 'selena')