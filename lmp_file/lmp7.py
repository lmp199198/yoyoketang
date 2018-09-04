# -*- coding:utf-8 -*-
'''
#python实例1-1、2、3、4组成互不相同且无重复的三位数：
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a != b and b != c and a != c:
                print(a*100+b*10+c)

#python实例2-输入利润来查奖金金额：
i = int(input('请输入利润：'))

brice = 0
if i <= 10:
    brice = 0.1*i
    print(brice)
elif i <= 20 and i >= 10:
    brice = 0.1*10+(i-10)*0.075
    print(brice)
elif i <= 40 and i >= 20:
    brice = 0.1*10+10*0.075+(i-20)*0.05
    print(brice)
elif i <= 60 and i >= 40:
    brice = 0.1*10+10*0.075+20*0.05+(i-40)*0.03
    print(brice)
elif i <= 100 and i >= 60:
    brice = 0.1*10+10*0.075+20*0.05+20*0.03+(i-60)*0.015
    print(brice)
elif i >= 100:
    brice = 0.1*10+10*0.075+20*0.05+20*0.03+40*0.015+(i-100)*0.01
    print(brice)
else:
    print('错误')


#python实例3-求平方数(数学分析，遍历求解)
#x + 100 = n**2, x + 100 + 168 = m**2
#m**2-n**2=168
#(m+n)(m-n)=168
#m+n=i  m-n=j  i*j=168
#m=(i+j)/2 n=(i-j)/2
#i和j均为偶数，且i，j均大于2
#j>=2,则i<=84
for i in range(2,85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i+j) % 2 == 0 and (i - j) % 2 == 0:
            m =(i + j) // 2
            n =(i - j) // 2
            x =(m**2-268)
            y =int(x)
            print(y)

#python实例4-输入某年某月某日，判断这一天是这一年的第几天？
year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
months = (0,31,59,90,120,151,181,212,243,273,304,334)   #每个月的天数，用列表展示
if 0 < month < 12:
    sum = months[month - 1]           #通过索引获取之前月共多少天
else:
    print('错误')
sum += day                 #之前所有月的天数加上当前月的哪一号
leap = 0
if year % 4 == 0 or year % 400 ==0 and year % 100 !=0 :
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print(sum)


#python实例5-输入三个数，按大小排列:
list = []
for i in range(5):   #遍历输入五次
    x = int(input('请输入:'))
    list.append(x)
print(sorted(list))
'''
#python实例6-斐波那契数列：
#递归求第n个斐波那契数列
#数列列表

def febonaqi(n):
    febo = []
    for i in range(n):
        if i <= 1:
            febo.append(i)
        else:
            febo.append(febo[i-1] + febo[i-2])  #  febo[i-1] + febo[i-2]==febo[-1] + febo[-2]
    return febo
print(febonaqi(6))

def febonaqi(n):
    febo = [0,1]
    for i in range(n-2):
        febo.append(febo[-1]+febo[-2])
    return febo
print(febonaqi(8))
#迭代打表
febo = [i for i in range(10)]
for i in range(10):
    if i <=1:
        febo[i] = i
    else:
        febo[i] = febo[i-1]+febo[i-2]
print(febo)

#递归数：
N=int(input(":"))
fib=[0 for x in range(N+1)]
fib[0]=0
fib[1]=1
for i in range(2,N+1):
    fib[i]=fib[i-1]+fib[i-2]
print(fib[N])


def febonaqi(n):
    if(n<=1):
        return n
    else:
        return febonaqi(n-1)+febonaqi(n-2)
print(febonaqi(8))

































































