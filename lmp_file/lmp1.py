for i in range(11,10000):
    a = i//1000
    b = (i-a*1000)//100
    c = (i -a*1000-b*100) // 10
    e = i % 10
    d = a**4+b**4+c**4+e**4
    if i == d:
        print(i)

num = int(input('请输入一个数：'))
n=num
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