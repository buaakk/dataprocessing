# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:40:54 2018
情感标注补充B
@author: kingkong
"""
import xlrd, xlwt
if __name__ == '__main__':
    xlsfile = 'E:\\new.xls'
    newfile = 'E:\\new1.xls'
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
             if (('建议' in testcase0 ) or ('或' in testcase0 )or ('进一步' in testcase0 )or('必要' in testcase0 )or('未见' in testcase0 )or ('？' in testcase0) or ('?' in testcase0))and('萎缩' not in testcase0 )and('梗' not in testcase0 )and('伤' not in testcase0 ) :
                newSheet.write(k, 1, 'B')
                nb=nb+1
                print("新插入",k)
        k=k+1
    print(nb)
    newxlr.save(newfile)