
'''
import pickle                 #定义模块
list1=[12,32,54,'jake Ma',['I LOVE YOU'],'GUN NI MA BI']   #新建序列
pickle1=open(r'F:\Baidu cloud\lmp','wb')         #打开文件
pickle.dump(list1,pickle1)                      #保存文件
pickle1.close()                                  #关闭文件



import sys
sys.path.append('F:\\Python\\lmp')
print(sys.path)


num100 = 532
num100_500 = 142
num500_1000 = 236
num1000 = 340
number = float(num100 + num100_500 + num500_1000 + num1000)

print('number的总数为:%.f个。' % number)
print('0-100ms:%s个，占比%.2f' % (num100,num100/number),'%',sep='')
print('100-500ms:%s个，占比%.2f' % (num100_500,num100_500/number),'%',sep='')
print('500-1000ms:%s个，占比%.2f' % (num500_1000,num500_1000/number),'%',sep='')
print('>1000ms:%s个，占比%.2f' % (num1000,num1000/number),'%',sep='')



#语言表：
table = {'Python':'Guido van Rossum',
         'Perl':'Larry Wall',
         'Tcl':'John Ousterhout'}

#language = 'Python'
#creator = table[language]

for lang in table:
    print(lang,'\t',table[lang])

#-*-coding=utf8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


myfile = open('lmp.txt','w')
myfile.write('李茂鹏是个大傻逼\n李茂鹏在家里干嘛？\n')
myfile.close()
for line in open('lmp.txt'):
    print(line,end='')

dic={
"山东省":{
'潍坊市':['寒亭区','高密市','寿光市','昌乐县'],
'济南市':['长清区','历下区','禹城市'],
'青岛市':['即墨市','黄岛区','崂山区']
},
"陕西省":{
'西安市':['未央区','长安区','雁塔区','新城区'],
'咸阳市':['秦都区','渭城区','礼泉县'],
'安康市':['汉阴县','白河县','紫阳县']
}
}
dic['陕西省']['西安市'][0]="碑林区"

print(dic.keys())
print(dic.values())
print(dic.items())
dic.setdefault('台湾省',{'baidu.com':[1,2,3]})
dic.pop('陕西省')
print(dic)
'''

'''
程序：购物车程序
需求:
启动程序后，让用户输入工资，然后打印商品列表
允许用户根据商品编号购买商品
用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒 
可随时退出，退出时，打印已购买商品和余
'''
product_list = [
('Iphone',5800),
('Mac Pro',9800),
('Bike',800),
('Watch',10600),
('Coffee',31),
('Alex Python',120),
]
shopping_list = []
salary = input("Please input your salary:")
if salary.isdigit():
    salary=int(salary)
    while True:
        for num,item in enumerate(product_list):
            print(num,item)
            user_choice = input("Please choice your item:")
            if user_choice.isdigit():
                user_choice=int(user_choice)
                if user_choice < len(product_list) and user_choice >= 0:
                    p_item = product_list[user_choice]
                    if p_item[1] <= salary:
                        shopping_list.append(p_item)
                        salary -= p_item[1]
                        print("added %s into shopping car,your current balence is \033[31;1m%s\033[0m" %(p_item,salary))
                    else:
                        print("your money is not enough to buy,you have \033[41;1m%s\033[0m left" %(salary))
                else:
                    print("your choice %s is out of shopping_list" %(user_choice))
            elif user_choice == 'q':
                print("shopping_list".center(50,"*"))
                for i in shopping_list:
                    print(i)
                print("your current balence:",salary)
                exit()
            else:
                print("Invalid option!!")
else:
    print("invalid salary!!")








