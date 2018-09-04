'''
a=[x * x  for x in range(1, 11) if x % 2 !=0]
print(a)

input=input('输入你的答案：')
if answer =='你真了不起':
    break

    print('回答正确，牛逼！')
n = 1
while n < 100:
    n= n + 1
    print(n)
print('end')
'''
n = 1
while n < 100:
    if n > 9:  # 当n = 10时，条件满足，执行break语句
        break  # break语句会结束当前循环
    n= n + 1
    print(n)
print('end')