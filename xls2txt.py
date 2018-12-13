# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:35:32 2018
将xls转为txt
@author: kingkong
"""

import xlrd

# 打开文件
try:
    data = xlrd.open_workbook("E:\\fcout2.xls")
except:
    print("fail to open file")
else:
    # 文件读写方式是追加
    file = open("E:\\fcouttxt.txt", "a")
    # 表头
    table = data.sheets()[0]
    # 行数
    row_cnt = table.nrows
    # 列数
    col_cnt = table.ncols
    # 第一行数据
    title = table.row_values(0)
    # 打印出行数列数
    print(row_cnt)
    print(col_cnt)
    print(title)
    for i in range(row_cnt):
        row = table.row_values(i)
        # 将字符串写入新文件
        file.writelines(str(row) + " ")
    # 关闭写入的文件
    file.close()

