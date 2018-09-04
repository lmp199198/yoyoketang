'''
import random
secret = random.randint(1,10)
temp = input('不妨猜猜我在想哪个数字吧：')
guess = int(temp)
while guess != secret:
    temp = input('哈哈,输入错误,请重新输入吧：')
    guess = int(temp)
    if guess == secret:
        print('卧槽，竟然被你蒙对了\n即使猜对了也没有奖励，哈哈哈')
    else:
        if guess > secret:
            print('大哥，大了大了')
        else:
            print('小了小了，再大点')
print('游戏结束，不玩了')

#冒泡排序
import requests
if __name__ == '__main__':
    _url = 'https://www.taobao.com'
    resp = requests.get(_url)
    print(resp.text)


import random


def bubblesort(target):
    length = len(target)
    while length > 0:
        length -= 1
        cur = 0
        while cur < length: #拿到当前元素
            if target[cur] < target[cur + 1]:
                target[cur], target[cur + 1] = target[cur + 1], target[cur]
            cur += 1
    return target
if __name__ == '__main__':
    a = [random.randint(1,1000) for i in range(100)]
    print(bubblesort(a))

class A():             #默认不用传值
    def add(self,a,b): #传参数，通过return返回
        return a*b

class B(A):           #B类引用了A类
    def sub(self,a,b):
        return a-b    #返回的不是a-b，而是A类里面的a*b；
C = B()
print(C.add(4,3))


from time import *
sleep(1)
print('--宝贝你知道吗？')
sleep(2.3)
print("--你和我的名字真有姻缘哦。")
sleep(2.3)
print('--李茂鹏的首字母拼音是lmp。')
sleep(2.3)
print('--而宝贝你的名字梁美萍也是lmp')

'''

for i in range(11,1000):
    a = i//100
    b = (i-a*100)//10
    c = i % 10
    d = a**3+b**3+c**3
    if i == d:
        print(i)

for i in range(100,1000):#for循环区间为100-999的数
    a = i//100 #取整除，返回商的整数部分。该处返回百位数数字
    b = (i-a*100)//10 #该处返回十位数上的数字
    c = i-a*100-b*10 #该处返回个位上的数字
    if a*a*a+b*b*b+c*c*c == i : #这里做是否满足水仙花数的逻辑判断
        print(i) #打印符合条件的数字

def printNarcissisticNumber(self, num):
    self.num =num
    num = int(num)
    if num < 100 or num > +1000:
        print("不是水仙花数")
    else:
        geWei = num % 10
        baiWei = int(num / 100)
        shiWei = int((num - baiWei * 100) / 10)
        # print(geWei)
        # print(shiWei)
        # print(baiWei)
        sum = geWei * geWei * geWei + shiWei * shiWei * shiWei + baiWei * baiWei * baiWei
        if sum == num:
            print("%d是水仙花数" % num)
        else:
            print("不是水仙花数")
if __name__=='__main__':

    def printNarcissisticNumber(self):

        for num in range(100, 1000):
            geWei = num % 10
            baiWei = int(num // 100)
            shiWei = int((num - baiWei * 100) // 10)
            sum = geWei**3 + shiWei**3 + baiWei**3
            if sum == num:
                print("%d是水仙花数" % num)













































































