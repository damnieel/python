#coding=utf-8
'''
Created on 2018年12月13日

@author: xiaohui
'''

print ("hello world!")


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

print (True)
print (False)
print (3 > 2)
print (3 > 5)
print('--------------------') 
print (True and True)
print (True and False)
print (5 > 3 and 3 > 1)
print('--------------------') 
print (True or True)
print (True or False)
print (False or True)
print('--------------------') 
print (not True)
print (not False)

x = 10
x = x + 2
print (x)
print (10 / 3)
print (10.0 / 3)
print (9 / 3)
print (10 // 3)
print (10 % 3)

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
print (classmates)
classmates.append('Adam')
print (classmates)
classmates.insert(1, 'Jack')
print (classmates)
classmates.pop()
print (classmates)
classmates[1] = 'Sarah'
print (classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print (len(s))

L = []
print (len(L))

t = (1, 2)
print (t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print (L[0][0],L[1][1],L[2][2])
print (L[1][2])
print (L[2][2])

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
第一种是for...in循环
第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
break
在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
continue
在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
'''
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
    
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

'''
Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
'''
print (list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

'''
dict
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。

第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
你可以猜到，这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。

把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
返回None的时候Python的交互环境不显示结果。
要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 67
print(d)
d['Jack'] = 90
print(d)
d['Jack'] = 88
print(d)

print('Thomas' in d)
print('Jack' in d)

'''
返回None的时候Python的交互环境不显示结果。
'''
print(d.get('Thomas', 0))
print(d.get('Thomas'))
print(d.get('Thomas', -1))
d.pop('Bob')
print(d)

'''
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
'''

'''
set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：
'''
s = set([1, 2, 3])
print (s)
s = set([1, 1, 2, 2, 3, 3])
print (s)
s.add(4)
print (s)
s.remove(4)
print (s)

'''
上面我们讲了，str是不变对象，而list是可变对象。
对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：

要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'
当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了
'''
a = ['c', 'b', 'a']
a.sort()
print (a)

a = 'abc'
a.replace('a', 'A')
print (a)

a = 'abc'
b = a.replace('a', 'A')
print (b)
