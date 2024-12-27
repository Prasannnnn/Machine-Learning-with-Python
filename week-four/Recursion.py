'''
5
4
3
2
1
'''
# for i in range(5,0,-1):
#     print(i)
# def countdown(n):
#     if n<=0:
#         print("its zero or negative")
#         return
#     else:
#         print(n)
#         countdown(n-1)

# m = float(input("Enter the Number for Countdown: "))
# countdown(m)


'''
n = 5 : Print(5) --> countdown(5-1) -- > countdown(4)
n = 4 : print(4) --> countdown(4-1) --> countdown(3)
n = 3 : print(3) --> countdown(3-1) --> countdown(2)
'''

'''
n= 5
n = 1+2+3+4+5
n = 15
'''

def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n-1)
    

print(sum_numbers(5))

'''
n= 5 --> 5 + sum_numbers(4)
n = 4 -->4 + sum_numbers(3)

'''
'''
Hello World

reverse string
dlrow olleH
'''