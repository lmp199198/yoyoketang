#import os
#os.mkdir(r'\Baidu cloud\lmp1')

#os.makedirs(r'F:\Baidu cloud\a\b\c')
#os.mkdir('lmp2')
'''
os.chdir(r'F:\Baidu cloud')
print(os.listdir(r'F:\Baidu cloud'))
print(os.getcwd())

os.chdir(r'F:\Baidu cloud')
print(os.getcwd())

os.chdir(r'F:\Baidu cloud')
#os.rmdir('c')
#os.removedirs(r'F:\Baidu cloud\a\b')
os.rmdir('lmp1')

os.system('calc')

print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.linesep)
print(os.name)

def temp():
    a=0
    b=1
    while True:
        a,b=b,a+b
        yield a
for each in temp():
    if each >200:
        break
    print(each)

a=(x for x in range(10))


for each in a:
    print(each)

def c2f(cel):
    fah=cel*1.8+32
    return fah

def f2c(fah):
    cel=(fah-32)/1.8
    return cel

def test():
    print("32摄氏度 = %.2f华氏度" % c2f(32))
    print("99华氏度 = %.2f摄氏度" % f2c(99))

if __name__=='__main__':    #调用模块时只会调用test函数，而不会调用其他模块里面的东西
    test()


#文件写入：
import os
os.chdir(r'F:\Baidu cloud\随书附件')
print(os.getcwd())

f =open('boy_1.txt','a')
f.write(' 我爱你')
f.close()


import urllib.request
response = urllib.request.urlopen('http://www.taobao.com')
html = response.read().decode('utf-8')
print(html)




#求100以内的质数：

i = 2
while i < 100:
    j = 2
    while j <= i / j:
        if not i % j:
            break
        j = j + 1
    if j > i / j:
        print(i, " 是素数")
    i = i + 1

print("Good bye!")

#if __name__ == '__main__'de 用法：

import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")


from one import PI

def calc_round_area(radius):
    return PI * (radius ** 2)

def main():
    print("round area: ", calc_round_area(2))

main()



if __name__ == '__main__':
    web_driver_type = raw_input('please input your int:')
    print(web_driver_type)


list='{0} is {1} {2} baby'.format('梁美萍','李茂鹏','favorite')
print(list)


list = '{a} {b} {c} favorite {d}'.format(a='梁美萍',b='is',c='李茂鹏',d='girl')
print(list)

a='a\tv'
print(a)



dictionary={}
flag = 'a'
pape = 'a'
off = 'a'
while flag == 'a' or 'c':
    flag = raw_input("add or search words ?(a/c)")
    if flag == 'a':
        word=raw_input('words:')
        definition=raw_input('value:')

        dictionary[str(word)]=str(definition)
        print('add success')
        pape = raw_input('search the dictionary?(a/0)')
        if pape == 'a':
            print(dictionary)
        else:
            continue
    elif flag=='c':
        checkwords = raw_input("please input what you want to enter:")
        for keys in sorted(directionay.keys()):
           if str(checkwords)==keys:
                print("this element exists", key,directionay[key])

            else:
        #print "this elemtn is not exists"
            print ("error type")
            break

#join用法———将列表转换成字符串
a='limaopeng'
b=list(a)
c=' '.join(b)
print(c,)



#左对齐，正负号，补零
x = 1223
res = 'integers: ... %d...%d...%3d...%-5d...%0007d' % (x,x,x,x,x)
print(res)


#格式化字符串中通过 * 计算宽度和精度，从 % 右边的输出中逐个获取变量
q = '%E %.2f %g ' %(1/4,2/7,1/8)
print(q)


#基于字典的字符串格式化(键值顺序不固定)
x = '%(n)s %(m)s %(q)s %(w)s  %(s)s' % {'w':'足','n':'人','m':'要','q':'学会','s':'知',}
print(x)

relay =
Greetings...
Hello %(name)s, your age squared is %(age)d

values = {'name':'Bob','age':40}
print(relay % values)

# 内置函数vars()
food = 'spam'
age = 40
x = '%(age)d %(food)s' % vars()
print(x)

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

#通过关键字参数
temp = '{a},{b} or {c}'.format(b='eggs',a='cat',c='tom')
print(temp)


# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名:{0[0]}, 地址:{0[1]}".format(my_list))      # "0" 是必须的


class Value():
    def __init__(self,value):
        self.value =value
my = Value(5)
print('value 为: {.value}'.format(my))
'''

#冒泡排序

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

#水仙花数
num = int(input('请输入一个数：'))
n = num
sum = 0
length = len(str(num))
while n != 0:
    a = n % 10
    sum  = sum + a **length
    n = n // 10
if sum ==num:
    print(num)
else:
    print(num,'不是水仙花数',sep='')

#方法1：
for temp in range(10,1000):
    sum=0 #各个位数的立方和
    # temp=i
    while temp:
        sum=sum+(temp%10)**3   #累加
        temp//=10   #地板除
    if sum==temp:
        print(temp)

#方法2：
for i in range(11,1000):
    a = i//100
    b = (i-a*100)//10
    c = i % 10
    d = a**3+b**3+c**3
    if i == d:
        print(i)

#求闰年
num = int(input('请输入一个年份：'))
i=num
if i % 4 ==0 and i % 100 != 0:
    print(num)
elif i % 400 == 0:
    print(num)
else:
    print(num,'为平年',sep='')

#求质数
n = int(input('请输入一个数：'))
if n >= 2:
    for i in range(2,n):
        if n % i ==0:
            print(n,'为合数,',i, '*', n // i,'=',n,sep='')
            break
    else:
        print(n,'为质数')

else:
    print(n,'既不是合数也不是质数')


#九九乘法表：
for i in range(1,10):

    for j in range(1,10):
        if i>=j:
            print('{0}*{1}={2}'.format(i,j,i*j),end=' ')
    print()







