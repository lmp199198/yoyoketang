def ds(x):
    return 2*x+5
print(ds(3))

a=lambda s:26*s-265+s/2-5
print(a(11))


def add(x,y):
    return x*y
print(add(2,5))

b=lambda d:3556/d -23+5*d
print(b(6))


temp = filter(None,[1,2,3,0,12.2,False,True,'EQWE','a<b'])
print(tuple(temp))


c = filter(lambda x:x % 2, range(15))    #过滤
print(tuple(c))


c = map(lambda x : x * 2, range(15))       #映射
print(tuple(c))



def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
'''
number = int(input('请输入一个正整数:'))
result = factorial(number)
print('%d 的阶乘是 %d' % (number,result))


def factorial(n):
    if n ==1:
        return n
    else:
        return n * factorial(n-1)

number = int(input('请输入一个正整数:'))
result = factorial(number)
print('%d 的阶乘是 %d' % (number,result))

a={}
print(type(a))


list1=[1,2,2,5,6,7,4,3,5,0]
for each in list1:
    print(each,end='')
'''













