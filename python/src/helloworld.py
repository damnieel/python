#coding=utf-8
'''
Created on 2018年12月13日

@author: xiaohui
'''

print "hello world!"


'''

数据类型
整数
Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。

计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。

浮点数
浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。

整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。

字符串
字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。

如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：
'I\'m \"OK\"!'
表示的字符串内容是：
I'm "OK"!
转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，可以在Python的交互式命令行用print()打印字符串看看：
如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用''' r'内容...' '''的格式表示多行内容，可以自己试试：

布尔值
布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：
布尔值可以用and、or和not运算。
and运算是与运算，只有所有都为True，and运算结果才是True：
or运算是或运算，只要其中有一个为True，or运算结果就是True：
not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
布尔值经常用在条件判断中

空值
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到。

变量
变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头，比如：


常量
所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
PI = 3.14159265359

/除法
//称为地板除，两个整数的除法仍然是整数
% 余数
'''

print('I\'m ok.')
print('I\'m learning\nPython.')
print('\\\n\n\\')

print('\\\t\\')
print(r'\\\t\\')

print('''line1
line2
line3''')

print True
print False
print 3 > 2
print 3 > 5
print('--------------------') 
print True and True
print True and False
print 5 > 3 and 3 > 1
print('--------------------') 
print True or True
print True or False
print False or True
print('--------------------') 
print not True
print not False

x = 10
x = x + 2
print x
print 10 / 3
print 10.0 / 3
print 9 / 3
print 10 // 3
print 10 % 3

'''
list和tuple
索引是从0开始
list是一个可变的有序表，所以，可以往list中追加元素到末尾： append
也可以把元素插入到指定的位置，比如索引号为1的位置： insert
要删除list末尾的元素，用pop()方法：
list元素也可以是另一个list
如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
'''
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
classmates.append('Adam')
print classmates
classmates.insert(1, 'Jack')
print classmates
classmates.pop()
print classmates
classmates[1] = 'Sarah'
print classmates

s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)

L = []
print len(L)

t = (1, 2)
print t

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print L[0][0],L[1][1],L[2][2]
print L[1][2]
print L[2][2]

'''

判断

'''

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
   
print('--------------------')    

'''

if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，所以，请测试并解释为什么下面的程序打印的是teenager

'''

age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
    
print('--------------------')    

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
    
'''

循环

'''