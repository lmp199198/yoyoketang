'''
import pickle

pickle1=open(r'\Baidu cloud\lmp','rb')           #只读模式打开二进制文件
list1=pickle.load(pickle1)                       #加载pickle1中的数据到list1
print(list1)                                     #打印list1

import lmp6 as tc

print('32摄氏度= %.2f华氏度'% tc.c2f(32))
print('99华氏度= %.2f摄氏度'% tc.f2c(99))

import sys
sys.path.append('F:\\Python\\lmp')
print(sys.path)

import lmp.p13_1 as tc

print('32摄氏度= %.2f华氏度'% tc.c2f(32))
print('99华氏度= %.2f摄氏度'% tc.f2c(99))

import urllib.request
response=urllib.request.urlopen('https://www.taobao.com')
html=response.read()
html=html.decode('utf-8')
print(html)

str1 = "Runoob example....wow!!!"
str2 = "exam"

print(str1.find(str2))
print(str1.find(str2,5))
print(str1.find(str2, 8))
'''

# web后台系统日志文件 记录了每个服务器请求处理时间（server.log）

#开发一个工具，统计时间在0-100ms,100-500ms,500-1000ms,>1s,每个请求的百分比为多少。

'''
  1.取出日志文件中每一次处理请求的时间，存入相应的list中
  1.1取出时间字符串
  先找到‘op takes ’的位置——idx1
  再找到其后面紧跟着的第一个空格的位置——idx2
  运行日志[idx1:idx2]——responsetimestr
  
  1.2判断其值，并存入相应容器
  
 #取出日志文件中每一次处理请求的时间，存入相应的容器中，病统计出每个时间段容器中处理时间的个数，并计算百分比。

list100 = []       #100ms以下
list100_500 = []   #100-500ms
list500_1000 = []  #500-1000ms
list1000 = []      #1s以上

file = 'server.log'
f = open(file)           #打开文件
lines = f.readlines()    #读取文件内容（行）
f.close()                #关闭文件

for line in lines:
    idx1 = line.find('op takes ')   #find会索引到'op takes '前面的字符串，而不会索引到后面空格处
    idx1 += len('op takes ')        #需要在idx1的基础上再加上'op takes '自身的字符长度
    idx2 = line.find('',idx1)
    responsetimestr = line[idx1:idx2]

    rts = float(responsetimestr)
    if rts < 0.1:
        list100.append(rts)
    elif 0.1 < rts <0.5:
        list100_500.append(rts)
    elif 0.5 < rts < 1:
        list500_1000.append(rts)
    elif rts > 0.1:
        list1000.append(rts)

num100 = len(list100)
num100_500 = len(list100_500)
num500_1000 = len(list500_1000)
num1000 = len(list1000)
number = float(num100 + num100_500 + num500_1000 + num1000)

print('number的总数为:%.2f个。' % number)
print('0-100ms:%s个，占比%.2f' % (num100,num100/number),'%',sep='')
print('100-500ms:%s个，占比%.2f' % (num100_500,num100_500/number),'%',sep='')
print('500-1000ms:%s个，占比%.2f' % (num500_1000,num500_1000/number),'%',sep='')
print('>1000ms:%s个，占比%.2f' % (num1000,num1000/number),'%',sep='')


#异常处理：
try-except：

try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生

使用except而不带任何异常类型

你可以不带任何异常类型使用except，如下实例：

try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码



try-finally:

#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("test.txt", "a")
    fh.write("woaini")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()


#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print "关闭文件"
        fh.close()
except IOError:
    print "Error: 没有找到文件或读取文件失败"


for i in range(5):
    if i ==3:
        break
    print(i)


l1 = [11,22,33,44,55]
l2 = [33,44,55,46]
l1_s = set(l1)
l2_s = set(l2)
l1_s.add(11)
l1_s.update([12,13,14])
l1_s.remove(12)
print(l1_s.pop())
print(len(l1_s))
print(len(l1))
print(l1_s)



f =open("yesterday","a")       #写入操作：如果文件不存在则会创建新文件，否则会覆盖原来的文件
f.write("\n我爱你！！！我擦累了")
f.close()

f = open("yesterday","r")
for i in range(5):
    print(f.readline(),end='')

  

for line in f.readlines():
    print(line.strip())

    
f = open("yesterday","r")
count = 0
for line in f:
    if count == 3:          #读取到第九行，并打印
        print("------分割线---------")
        count += 1
        continue
    print(line.strip())
    count += 1


f = open("yesterday","r")
#f.write('nima')
#f.close()
print(f.tell())
print(f.encoding)
print(f.read(3))
print(f.name)
print(f.fileno())
f.seek(0)
print(f.readable())
print(f.writable())

f = open("yesterday","r")
f_new = open('yesterday1','w')

for line in f:
    if 'nima' in line:
        line = line.replace('nima','caonima')
    f_new = f_new.write(line)
f.close()
f_new.close()

with open('ll','wt') as file:
    file.write('nimade')


spam = ['cat', 'dog', 'mouse']
for i in spam:
    print(len(i),end=' ')

spam = ('I','have','a','pet')
spam = spam[:1] + spam[3:]
print(spam)


import Resquests
if __name__ == '__main__':
    _url = 'https://www.taobao.com'
    resp = Requests.get(_url)
    print(resp.text)


'''
def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
lists=[12,5,2,2,3,6,5,89,5623,11,45]
print()
























