#coding=utf-8
'''
Created on 2018年12月13日
pip3 install pymysql
@author: xiaohui
'''
import pymysql
# 注意把password设为你的root口令:
conn = pymysql.connect('192.168.1.123','root', 'root', 'aimall')
cursor = conn.cursor()
cursor.execute("SELECT * from keyword_item limit 0,10")
values = cursor.fetchall()
print(values)
print(values[0][0])
array = tuple(values)
print(len(array))
for list in array:
    print(list)
cursor.close()
conn.close()