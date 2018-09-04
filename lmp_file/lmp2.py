temp= input('宝贝知道我现在心里想的是啥：')
guess =str(temp)
while guess !='爱我的小宝贝':
    temp = input('回答错误，小心被梁凉打死，再给你一次机会：')
    guess = str(temp)
    if guess =='爱我的小宝贝':
        print('回答正确，小宝贝梁凉爱你一辈子')
    elif guess =='我想你':
        print('程度还不够，再回答：')
    elif guess =='我爱你':
        print('距离正确答案差一点，再想想：')
    else:
        print('竟然不知道？打死你，哼')





