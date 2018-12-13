# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:40:54 2018
情感标注补充2 剩余标为c
@author: kingkong
"""
import xlrd, xlwt
if __name__ == '__main__':
    xlsfile = 'E:\\new1.xls'
    newfile = 'E:\\new2.xls'
    sheetname  =  u'ctdata'
    newxlr  =  xlwt.Workbook()
    newSheet=newxlr.add_sheet(sheetname,cell_overwrite_ok=True )#cell_overwrite_ok=True 保证可以如果对一个单元格重复操作
    k=0;nb=0
    myxlr=xlrd.open_workbook(xlsfile)
    mySheet=myxlr.sheet_by_name(sheetname)
    nrows=mySheet.nrows
    for num in range(nrows):
        testcase0 = mySheet.cell(num, 0).value
        testcase1 = mySheet.cell(num, 1).value
        newSheet.write(k, 0, testcase0)
        newSheet.write(k, 1, testcase1)
        if (mySheet.cell(num, 1).value == '' ):
             if ('可见' in testcase0 )or('大' in testcase0 )or('缺' in testcase0 )or('伤' in testcase0 )or('萎缩' in testcase0 )or('梗' in testcase0 )or(len(testcase0) > 30):
                newSheet.write(k, 1, 'C')
                nb=nb+1
              #  print("新插入",k)
             if ('阅片' not in testcase0):
                 if (len(testcase0) > 3)and('。。' not in testcase0)and('-' not in testcase0)and ('宫' not in testcase0)and ('确费' not in testcase0)and ('同上' not in testcase0)and ('报告' not in testcase0)and ('妊娠' not in testcase0)or ('未见'  in testcase0) :
                     newSheet.write(k, 1, 'C')
                     nb=nb+1

        k=k+1
    print(nb)
    newxlr.save(newfile)