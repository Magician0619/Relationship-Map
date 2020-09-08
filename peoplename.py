#  -*- coding:utf-8 -*-

'''
#@Author: Magician
#@Date: 
#@Description: 

Copyright 2020 by Magician
'''
content = []

with open('人名.txt', 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        content.append(line.replace("\n",""))

print(content)