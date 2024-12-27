def f1():
    a = "I love Spagetti"

    def f2():
        print(a)

    f2()



f1()

'''
Anonymous Functions in Python
'''

def cube(x): return x*x*x


cube_v1 = lambda x : x*x*x

print(cube(7))

print(cube_v1(7))