# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:00:24 2018
去掉文件中的特殊字符
@author: kingkong
"""
import sys
content=""
infile = open("E:\\fcouttxt.txt")
outfile = open("E:\\fcouttxt1.txt","a")
content = infile.read()
content = content.replace("[",'')
content = content.replace("]",'')
content = content.replace("'",'')
outfile.write(content)
infile.close()
outfile.close()
print(len(content))
