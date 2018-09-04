# -*- coding:utf-8 -*-
'''
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.quit()

for i in range(10,1000):
    sum=0 #各个位数的立方和
    temp=i
    while temp:
        sum=sum+(temp%10)**3   #累加
        temp//=10   #地板除
    if sum==i:
        print(i)
'''

for i in range(100,1000):#for循环区间为100-999的数
    a = i//100 #取整除，返回商的整数部分。该处返回百位数数字
    b = (i-a*100)//10 #该处返回十位数上的数字
    c = i-a*100-b*10 #该处返回个位上的数字
    if a*a*a+b*b*b+c*c*c == i : #这里做是否满足水仙花数的逻辑判断
        print(i) #打印符合条件的数字
