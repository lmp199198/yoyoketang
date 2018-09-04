'''
import math
class Solver(object):
    def demo(self,a,b,c):
        d = b ** 2 - 4 * 2 * c
        disc = math.sqrt(d)
        root1 = (-b + disc) / (2 * a )
        root2 = (-b - disc) / (2 * a )
        print(root1,root2)
        return root1,root2
'''
#print('limao','peng',sep='')
#print('265*456=',265*456,sep='')
# sep是separation的简称,即代表分隔符.end则代表结束处的符号,
# 在字符串结尾处追加一个值。通常情况下，sep默认是一个空格,意思是去掉中间的空格符号；
# end默认是一个换行符。
#print('li','mao','peng',end='');print('lmp')
#print('i love \"you\"')
#Python还允许用r''表示''内部的字符串默认不转义，
#print(r'\\sf\\');print('\\fa\\')
#print(1,2,3,1,sep='\n')

#ord()函数获取字符的整数，例如：ord('A')=65,chr()函数把编码
#转换成对应的字符，例如：chr(66)='B'
#a=b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
#b=b'fajfgj'.decode('ascii')
#b='daddaf'.encode('ascii')
#a=b'da'.decode('utf-8')

#!/user/bin/env/python3.6.3
#-*- coding: utf-8 -*-

#格式化(%d 整数；%f 浮点数；%s 字符串；%x 16进制整数)：
#有几个 “%?”占位符，后面就跟几个变量，顺序要对应好，只有一个%？时，括号可以省略。
#字符串：a='lmmaopeng is %s'%'dabendan'  a='hi,you is %s my %s'% ('son','dear')

#整数：中间的数字 “2” 代表占用了空格2，表示占位符占用的空格：
# a='%2d+%2d' % (1,3)

#a='%5.2f' % 3.25453,前面的5代表5个占位符，没有那么多数字，则在前面用空格代替，
#后面的.2代表小数点截取后两位。

#%s永远起作用，会把任何数据类型转换成字符串：
#a='生命在于运动，这句话对不对？%s? and %s?' % ('yes','no')


#字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
#a='这次报名参赛的有:%d人，排名全班人数%d%%' % (45,90)

#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
#a=72,b=85,c=(b-a)/a*100,print('%.1f%%' % c)



#list
#a=['jerry','tom','sandy'],print(len(a)),print(a[2]),print(a[0]),print(a[-2])
#a.append('david'),a.insert(4,'tony'),a[2]='bob'
#a=['jerry','tom','sandy',[21,'jed'],12,True] b=[110,120,119] a.insert(0,b)

#tuple
#tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list
#并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，
#就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
#a=(1,'aim','eye',[110,'Bob'],120) a[3][0]='119' a[3][1]='Alan'


# -*- coding: utf-8 -*-  作业
# 打印Apple:
# 打印Python:
# 打印Lisa:
'''
L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]
print(L[0][2]),print(L[1][1]),print(L[2][2])
'''

#条件判断（if语句）
#print('我的年龄是:',age,'%s' % '岁',sep='') 我的年龄是:18岁
#age=18 if age>16:

#input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成
#b=input('birthday:')  a=int(b)


#练习
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
'''
height = 1.75
weight = 60
BIM = weight / (height*height)
if BIM < 18.5:
    print('过轻')
elif 18.5 <= BIM < 25:
    print('正常')
elif 25 <= BIM < 28:
    print('过重')
elif 28 <= BIM < 32:
    print('肥胖')
else:
    print('严重肥胖') 
'''

#循环语句

'''
循环语句之for x in ...(依次把list或tuple中的每个元素迭代出来)

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
    
for a in ['Michael', 'Bob', 'Tracy']:
    print(a)

print跟sum对齐时，每次都执行sum的结果，10个数字共执行10次：
sum = 0
for a in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum =sum + a
    print(sum)

print跟for对齐，执行for的结果，只执行1次：
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
'''
'''
如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，
可以生成一个整数序列，再通过list()函数可以转换为list。比如range(10)生成的序列是从0开始小于10的整数：
例子：
print(list(range(10))) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
for a in range(101):
    sum = sum +a
print(sum)

循环语句之while：(只要条件满足，就不断循环，条件不满足时退出循环。)

100以内的奇数和：
sum = 0
a = 99
while a > 0:
    sum = sum +a
    a = a - 2
print(sum)

100以内的偶数之和：
sum = 0
a = 0
while a <= 100:
    sum = sum +a
    a = a + 2
print(sum)
'''


#练习
#请利用循环依次对list中的每个名字打印出Hello, xxx!：
# -*- coding: utf-8 -*-
'''
L = ['Bart', 'Lisa', 'Adam']
for a in L:
    print('Hello,',a,'!',sep='')
Hello,Bart!
Hello,Lisa!
Hello,Adam!


循环语句之break:

循环打印1～100的数字：
n = 1
while n < 100:
    n= n + 1
    print(n)
print('end')

如果要提前结束循环，可以用break语句：(打印到10就结束程序)
n = 1
while n < 100:
    if n > 9:  # 当n = 10时，条件满足，执行break语句
        break  # break语句会结束当前循环
    n= n + 1
    print(n)
print('end')

bingo= '李茂鹏是大帅哥'
answer = input('请输入李茂鹏最爱听的一句话：')
while  True:
    if answer == bingo:
        break
    answer = input('对不起，请重新输入:')
print('恭喜您，输入正确')


循环语句之continue:
打印100以内的奇数：
第一种例子:
n = -1
m = 0
while n < 99:
    m = n + 2
    n = n + 2
    print(m)
    
第二种例子：
n = 0
while n < 100:
    n = n + 1
    if n % 2 == 0: #如果是偶数，余数为0，执行continue语句
        continue   #continue语句会直接继续下一轮循环，后续的print（）语句不会执行
    print(n)       #continue的作用是提前结束本轮循环，并直接开始下一轮循环

第三种例子：
for a in range(1,100,2):
    print(a,end=' ')
使用range函数执行。

for a in range(10):
    if a % 2 ==1:
        print(a)
        continue
    a= a + 2
    print(a)
    
小结
循环是让计算机做重复任务的有效的方法。
break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
这两个语句通常都必须配合if语句使用。

不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。
大多数循环并不需要用到break和continue语句，上面的两个例子，
都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。


s=int(input('请输入你的分数：'))
if s >= 90:
    print('优秀')
elif 80 <= s < 90:
    print('良好')
elif 60 < s < 80:
    print('及格')
else:
    print('不及格')

name = 'limaoepng'
for a in name:
    print(a,end='')

member=['李茂鹏','李丽华','李治','李治廷','李梦男','谷智鑫','袁田野']
for a in member:
    print(a,end=' ')
limaoepng李茂鹏 李丽华 李治 李治廷 李梦男 谷智鑫 袁田野 

member=['李茂鹏','李丽华','李治','李治廷','李梦男','谷智鑫','袁田野']
for a in member:
    print(a,len(a))
'''
#列表--range可以是range（10），从0到9 10个数字，也可以是range（1，9）从1-9 九个数字。
#range语法：
'''
range（[start],stop[,step=1]）
1.这个BIF有三个参数，其中用中括号括起来的两个表示这两个参数是可选的；
2.step=1表示第三个参数的默认值是1；
3.range这个BIF的作用是生成一个从start参数的值开始到stop参数的值结束的数字序列。


for a in range(5):
    print(a,end='' )  01234

for a in range(1,9):
    print(a,end='')   12345678

for a in range(1,100,2):
    print(a,end=' ')
'''

#列表--数据交换,从第一个到第n个：
'''
a=['daling','hele','vhign','fhsj','cindy']
b=a[0]
a[0]=a[1]
a[1]=b
print(a)
'''

#列表--数据删除之remove：
'''
a=['daling','hele','vhign','fhsj','cindy']
a.remove('daling')
print(a)
a.insert(0,'daling')
print(a)
'''

#列表--数据删除之del：
'''
a=['daling','hele','vhign','fhsj','cindy']
del a[0]   删除指定索引元素
del a      删除全部列表元素
'''

#列表--数据删除之pop：
a=['daling','hele','vhign','fhsj','cindy']
'''
a.pop(2)   删除指定索引元素
a.pop()    删除最后一个元素
'''

#列表的分片操作：
'''
str = "0123456789"
print("打印第0个元素:" ,str[0])
print("负数表示倒数第N个元素，-1表示倒数第一个元素:" ,str[-1])
print("分片操作，str[start:end], start会包含在结果中而end却不会:" ,str[1:5])
print("冒号后不写表示从start到末尾:" ,str[5:])
print("表示从倒数第二个元素一直到末尾:" ,str[-2:])
print("表示从倒数第六个元素到倒数第二个元素，但不包含倒数第二个元素:" ,str[-6:-2])
print("start不写表示从开头开始到end, 但不包含end:" ,str[:4])
print("start和end都不写表示整个列表:" ,str[:])
print("支持步长，步长为正数表示从start到end每隔N个数打印一个:" ,str[::2])
print("步长为负数表示从end到start每隔N个数打印一个:" ,str[::-2])
print("若end比start小，则步长必须为负数否则会出错:" ,str[-1:-6:-1])
print("两个序列相加会合并:" ,[1, 2, 3] + [4, 5, 6]) 
print("序列乘法相当于3个序列相加：" , [1, 2, 3] * 3)
'''

#字典-dict的应用
'''
a={'Michael':85,'Bob':95,'Tracy':80}
print(a['Bob'])   通过list把属于'Bob'的value值提取出来；

由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
a={'Michael':85,'Bob':95,'Tracy':80}
a['Bob']=90
print(a)  {'Michael': 85, 'Bob': 90, 'Tracy': 80}

a={'Michael':85,'Bob':95,'Tracy':80}
a.pop('Bob')     删除一个key，使用pop（key）方法，对应的value也会从dict中删除；
print(a)   {'Michael': 85, 'Tracy': 80}
'''

#和list比较，dict有以下几个特点：
'''
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，
正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
'''
#set的应用
'''
a=set([1,3,5,3,6,2,1])
print(a)    {1, 2, 3, 5, 6}   自动过滤重复的元素，以花括号的形式打印出来，表示其中有这些元素

a=set([1,3,5,3,6,2,1])
a.add(4)     通过add（key）方法添加元素到set中；
a.remove(3)  通过remove（key）方法删除元素；
'''
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
'''
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)    交集；
print(s1|s2)      并集；
print(s1-s2)      差集；
print(s1^s2)      不存在的元素；

'''
#list--不可变对象
'''
a = ['q', 'b', 'a']
a.sort()    顺序颠倒;
'''
#str--不可变对象

'''
容器序列：
  list/tuple/collections.deque
  能存放不同类型的数据
  存放的使他们所包含的任意类型的对象的引用
扁平序列：
  str/bytes/bytearray/memoryview/array.array
  只能存放单一类型的数据
  存放的是值，而不是引用
  是一段连续的内存空间
可变序列：
  list/bytearray/array.array/collections.deque/memoryview
不可变序列：
  tuple/str/bytes
'''

#调用函数:
'''
1.int(x [,base])  将x转换为一个整数      base作为一个进制，默认是10进制，例:print(int('123',16))--291
2.float(x)  将x转换到一个浮点数           例:print(float(1))--1.0
3.complex(real [,imag])  创建一个复数     例:print(complex(1,3))--(1+3j)
4.str(x)   将对象 x 转换为字符串          例:print(str(123))--123
5.repr(x)  将对象 x 转换为表达式字符串    例:print(repr('123'))--'123'
6.eval(str)   用来计算在字符串中的有效Python表达式,并返回一个对象   
例：a="'a','123','110','abs'"
b=eval(a)
print(b)
('a', '123', '110', 'abs')

7.tuple(s)   将序列 s 转换为一个元组    例：a=[12,323,'da','da']--print(tuple(a))
8.list(s)   将序列 s 转换为一个列表     例：a=(12,323,'da','da')--print(list(a))
9.set(s)   转换为可变集合     例：print(set('abcd'))--{'c', 'd', 'b', 'a'}
10.dict(d)   创建一个字典。d 必须是一个序列 (key,value)元组。  例：a={'Michael':85,'Bob':95,'Tracy':80}
11.frozenset(s)   转换为不可变集合    例：print(frozenset('abcd'))--frozenset({'a', 'd', 'c', 'b'
12.chr(x)     将一个整数转换为一个字符      例：print(ord('5'))--53
13.unichr(x)  将一个整数转换为Unicode字符   例：print(unichr(97))--u'a'
14.ord(x)     将一个字符转换为它的整数值    例：print(ord('1'))--49
15.hex(x)     将一个整数转换为一个十六进制字符串    例：print(hex(12))--0xc
16.oct(x)     将一个整数转换为一个八进制字符串      例：print(oct(12))--0o14
'''
#数据类型转换
'''
print(abs(5))
print(max(1,2,5))
print(min(1.22,25,2))
print(int(12.02))
print(float(12))
print(str(1.23))
print(bool(2.2))
print(bool(''))


函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a=abs(-2)
b=int('123')
c=float('100')
print(a,b,c)
#hex()函数是将一个整数转换成16进制的字符串：
n1 = 255
n2 = 1000
print(hex(n1),hex(n2))
0xff 0x3e8
'''

#定义函数--def语句，并使用return语句返回：
'''
定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。
这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python提示符执行。

语法：
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]


import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x=move(100,100,60,math.pi/3)
print(x)

def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print("函数内取值: ", mylist)
   return
'''

#定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。
#这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python提示符执行。
#如下实例调用了printme（）函数：

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return

# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")

def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print("函数内取值: ", mylist)
   return


'''
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
1.不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
2.可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：
1.不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，
只是修改另一个复制的对象，不会影响 a 本身。
2.可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。


#python传不可变对象实例:
# !/usr/bin/python
# -*- coding: UTF-8 -*-

def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)
# 结果是 2

#python传可变对象实例:
# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)
'''

#参数：
#以下是调用函数时可使用的正式参数类型：
#1、必备参数
#2、关键字参数
#3、默认参数
#4、不定长参数

'''
1、必备参数
必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
调用printme()函数，你必须传入一个参数，不然会出现语法错误：
'''
# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return
# 调用printme函数
printme(str='哥只是个传说')

'''
2、关键字参数
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
以下实例在函数 printme() 调用时使用参数名：
'''

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)

    return
# 调用printme函数
printme("My string")

def print1(sex,name,age,):
    print('name:',name)
    print('age:', age)
    print('sex：', sex)

    return
print1(sex='man',name='cindy',age=20,)

'''
3、默认（缺省）参数
调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：

'''
def print1(sex,name,age=21,): #age=21为默认值
    print('name:',name)
    print('age:', age)
    print('sex：', sex)

    return
print1(sex='man',name='cindy')  #age=20(省去)

'''
4、不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，
和上述2种参数不同，声明时不会命名。基本语法如下：

def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
   



# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def printinfo(a, *b):
    "打印任何传入的参数"
    print("input ")
    print(a)

    for var in b:
        print(var)

    return
# 调用printinfo 函数
printinfo(a=12)
printinfo(7,1,20)


def factorial(n):
    result = n
    for i in range(1,n):
        result *=1
        return result


def facyorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)
'''

# 斐波那契 数列 
'''
a=[0,1]
for i in range(10):
    a.append(a[-2]+a[-1])
print(a)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

'''

a = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
m=[]
n=3
for b in range(n):
    m.append(a[b])
print(m)


#迭代--for循环（字典）
#默认情况下，dict迭代的是key。如果要迭代value，
#可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
'''
d = {'a': 1, 'b': 2, 'c': 3}
for a in d.values():
    print(a)
for a in d:
    print(a)
for a,b in d.items():
    print(a,b)
'''

#Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：
'''
for a,b in enumerate(('a','b','c','d')):
    print(a,b)   例：索引和元素本身被同时迭代
for a,b in ((1,1),(2,2),(3,3),(4,4)):
    print(a,b)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)

##任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，
# 只要符合迭代条件，就可以使用for循环。
'''

#列表生成式：
'''
生成[1x1, 2x2, 3x3, ..., 10x10]，
##把要生成的元素a * a放到前面，后面跟for循环，就可以把list创建出来
方法一：循环
a=[]
for b in range(1,11):
    a.append(b*b)
print(a)

方法二：列表生成式子：
[a*a for a in range(1,11)]
print(a)

b=[b * b for b in range(1,11) if b % 3 == 0]
print(b)     [9, 36, 81]
'''

#两层循环--列表生成式
l=[m+n for m in 'asd' for n in 'qwe']
print(l)
#['aq', 'aw', 'ae', 'sq', 'sw', 'se', 'dq', 'dw', 'de']

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
'''
d = {'a': 1, 'b': 2, 'c': 3}
for  a,b in d.items():
    print('[',a,'=',b,']',sep='',end=' ')

d = {'a': 1, 'b': 2, 'c': 3}
x=[a +'='+ b for a,b in d.items()]
print(x)

'''
##dir()打印出当前列表的所有list语法：
'''
list=[1,2,3,1,1]
print(dir(list))
print(list.count(1))
'''
##list.index(n,start,stop),n代表要查询的元素，start表示从起始位置开始查询，stop表示结束位置；

##list.reverse()将列表进行翻转排序；

##list.sort()将列表中要从小到大排序；list.sort(reverse=False),默认为False，
# list.sort(reverse=True)则是颠倒顺序，从大到小排序；


##元祖：
##定义tuple时，当元素只有一个时，需要加一个逗号，否则会判断该元素为 “int”；
# 逗号可以定义tuple，定义空 tuple时，直接 temp = （）；
'''
temp=1,2,3,4
print(type(temp))   打印：<class 'tuple'>

temp1=(1)
print(type(temp1))  打印：<class 'int'>

temp1=(1，)
print(type(temp1))  打印：<class 'tuple'>


m=('小可爱','小煞笔','小傻逼','小垃圾','小东西')
n=('大死你','大宝剑','大保健','大包间','大宝贝')
l=m[0:1]+n[1:3]
print(l)    打印:('小可爱', '大宝剑', '大保健')

'''
##字符串--string
'''
1、
str='python'
print(str.capitalize())--{将字符串的第一个字符转换为大写}   打印:Python
 
2、
str='PYTHON'
print(str.swapcase())--将大写转换成小写

3、
str='P\tYTH\tON'
print(str.expandtabs())
expandtabs(tabsize=8)把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。

4、
str='PYTHON'
print(str.replace('PYTHON','Python'))--replace(old, new [, max])把 将字符串中的 str1 替换成 str2,
如果 max 指定，则替换不超过 max 次。
'''

##字符串函数和方法：
'''
1 capitalize()将字符串的第一个字符转换为大写
2 center(width, fillchar)返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
3 count(str, beg= 0,end=len(string))返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指
定范围内 str 出现的次数
4 decode(encoding='UTF8',
errors='strict')使用指定编码来解码字符串。默认编码为字符串编码。
5 encode(encoding='UTF8',
errors='strict')以 encoding 指定的编码格式编码字符串，如果出错默认报一个
ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
6 endswith(suffix, beg=0, end=len(string))检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指
定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
7 expandtabs(tabsize=8)把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
8 find(str, beg=0 end=len(string))检测 str 是否包含在字符串中，如果 beg 和 end 指定范围，则检查是否
包含在指定范围内，如果是返回开始的索引值，否则返回1
9 index(str, beg=0, end=len(string))跟find()方法一样，只不过如果str不在字符串中会报一个异常.
10 isalnum() 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
11 isalpha() 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
12 isdigit() 如果字符串只包含数字则返回 True 否则返回 False
13 islower() 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，
则返回 True，否则返回 False
14 isnumeric() 如果字符串中只包含数字字符，则返回 True，否则返回 False
15 isspace() 如果字符串中只包含空格，则返回 True，否则返回 False
16 istitle() 如果字符串是标题化的(见 title())则返回 True，否则返回 False
17 isupper() 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，
则返回 True，否则返回 False
18 join(seq)以指定字符串作为分隔符，将 seq(序列) 中所有的元素(的字符串表示)合并为一个新的字符串
19 len(string)返回字符串长度
20 ljust(width[, fillchar])返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默
认为空格。
21 lower()转换字符串中所有大写字符为小写.
22 lstrip()截掉字符串左边的空格
23 maketrans()创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，
表示需要转换的字符，第二个参数也是字符串表示转换的目标。
24 max(str)返回字符串 str 中最大的字母。
25 min(str)返回字符串 str 中最小的字母。
26 replace(old, new [, max])把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
27 rfind(str, beg=0,end=len(string))类似于 find()函数，不过是从右边开始查找.
28 rindex( str, beg=0, end=len(string))类似于 index()，不过是从右边开始.
29 rjust(width,[, fillchar])返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
30 rstrip()删除字符串字符串末尾的空格.
31 split(str="", num=string.count(str)), 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num
个子字符串
32 splitlines( num=string.count('\n'))]按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅
切片 num 个行.
33 startswith(str, beg=0,end=len(string))检查字符串是否是以 obj 开头，是则返回 True，否则返回
False。如果beg 和 end 指定值，则在指定范围内检查。
34 strip([chars])在字符串上执行 lstrip()和 rstrip()
35 swapcase()将字符串中大写转换为小写，小写转换为大写
36 title()返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
37 translate(table, deletechars="")根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符
放到 deletechars 参数中
38 upper()转换字符串中的小写字母为大写
39 zfill(width)返回长度为 width 的字符串，原字符串右对齐，前面填充0
40 isdecimal()检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。

'''
#字符串：格式化
'''
a='{0} love {1}'.format('I','you')
print(a)     ......I love you
b='{0} love {a}'.format('I',a='you')
print(b)

1、c='%2.2f' % 3.25453    例子：3.25

2、q='{0:.3f}{1}'.format(3.1415926,'GB')   例子：3.142GB
'''

w='%03d' % 30
print(w)


#长字符串：
print("""
春眠不觉晓,
处处闻啼鸟.
夜来风雨声,
花落知多少
""")

#原始字符串   例1：
a='http:\nprotal'
print(a)

#例2：(加上一个'\'转义)
b='http:\\nprotal'
print(b)

#例3：(字符串前面加上一个英文字母'r')
c=r'http:\nprotal'
print(c)
'''
#打游戏：
import random
secret = random.randint(1,10)
temp = input('不妨猜猜我在想哪个数字吧：')
guess = int(temp)
while Guess != secret:
    temp = input('哈哈,输入错误,请重新输入吧：')
    Guess = int(temp)
    if Guess == secret:
        print('卧槽，竟然被你蒙对了\n即使猜对了也没有奖励，哈哈哈')
    else:
        if Guess > secret:
            print('大哥，大了大了')
        else:
            print('小了小了，再大点')
print('游戏结束，不玩了')
'''
import random
def bubble(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(i+1,count):
            if lists[i] > lists[j]:
                lists[i],lists[j] =lists[i],lists[j]
    print(lists)
    return lists
if __name__ == '__main__':
    lists = [random.randint(2,10) for i in range(15)]
    print('冒泡排序:')
    bubble=sorted(bubble(lists))
    print(bubble)

#冒泡排序(随机数字排序)
import random
def bubblesort(target):
    length = len(target)
    while length > 0:
        cur = 0
        length -= 1
        while cur < length: #拿到当前元素
            if target[cur] > target[cur + 1]:
                target[cur], target[cur + 1] = target[cur + 1], target[cur]
            cur += 1
    return target
if __name__ == '__main__':
    a = [random.randint(1,10) for i in range(10)]
    print('冒泡排序:')
    print(bubblesort(a))


























































































































































































































































































































































































