# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:40:54 2018
情感标注补充3 从A中挑出一些属于C的来
@author: kingkong
"""
import xlrd, xlwt
if __name__ == '__main__':
    xlsfile = 'E:\\new2.xls'
    newfile = 'E:\\new3.xls'
    sheetname  =  u'ctdata'
    newxlr  =  xlwt.Workbook()
    newSheet=newxlr.add_sheet(sheetname,cell_overwrite_ok=True )#cell_overwrite_ok=True 保证可以如果对一个单元格重复操作
    k=0;n=0
    na=0;nb=0;nc=0;nd=0;
    myxlr=xlrd.open_workbook(xlsfile)
    mySheet=myxlr.sheet_by_name(sheetname)
    nrows=mySheet.nrows
    for num in range(nrows):
        testcase0 = mySheet.cell(num, 0).value
        testcase1 = mySheet.cell(num, 1).value
        newSheet.write(k, 0, testcase0)
        newSheet.write(k, 1, testcase1)
        if (mySheet.cell(num, 1).value == 'A' ):
             if ('梗' in testcase0 )or('骨折' in testcase0 )or('缺' in testcase0 )or('结节' in testcase0 )or('偏' in testcase0 )or('萎缩' in testcase0 )or('流产' in testcase0 )or('退' in testcase0 )or('囊肿' in testcase0 )or(len(testcase0) > 50):
                newSheet.write(k, 1, 'C')
                n=n+1
              #  print("新插入",k)
            
        k=k+1
        if (mySheet.cell(num, 1).value == 'A' ):
            na=na+1
        if (mySheet.cell(num, 1).value == 'B' ):
            nb=nb+1
        if (mySheet.cell(num, 1).value == 'C' ):
            nc=nc+1
        elif (mySheet.cell(num, 1).value == '' ):
            nd=nd+1
    print(n)
    print(na+nb+nc+nd)
    newxlr.save(newfile)

