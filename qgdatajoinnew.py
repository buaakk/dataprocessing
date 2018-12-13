# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:40:54 2018
从标注数据中去除空行
@author: kingkong
"""
import xlrd, xlwt
if __name__ == '__main__':
    ysfile = 'E:\\newdatabz.xls'
    newfile = 'E:\\newdatabznew.xls'
    sheetname  =  u'带标注数据'
    newxlr  =  xlwt.Workbook()
    newSheet=newxlr.add_sheet(u'带标注数据',cell_overwrite_ok=True )#cell_overwrite_ok=True 保证可以如果对一个单元格重复操作
    k=0;n=1
    aaa=xlrd.open_workbook(ysfile)
    Sheet=aaa.sheet_by_name(sheetname)
    nrows=Sheet.nrows
    for num in range(nrows):
        if (Sheet.cell(num, 3).value == '' ):
            continue
        yxbx = Sheet.cell(num, 1).value
        yxzd = Sheet.cell(num, 2).value
        bzvalue = Sheet.cell(num, 3).value
        newSheet.write(k, 0, n)
        newSheet.write(k, 1, yxbx)
        newSheet.write(k, 2, yxzd)
        newSheet.write(k, 3, bzvalue)
            
        n=n+1
        k=k+1     
    print(n-1)
    newxlr.save(newfile)