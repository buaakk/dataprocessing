# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:40:54 2018
情感标注补充3 从A中挑出一些属于C的来
@author: kingkong
"""
import xlrd, xlwt
if __name__ == '__main__':
    biaozhufile = 'E:\\new3.xls'
    yuanshifile = 'E:\\ctdata_yxbx.xls'
    newfile = 'E:\\newdatabz.xls'
    sheetname  =  u'ctdata'
    newxlr  =  xlwt.Workbook()
    newSheet=newxlr.add_sheet(u'带标注数据',cell_overwrite_ok=True )#cell_overwrite_ok=True 保证可以如果对一个单元格重复操作
    k=0;n=1
    bz=xlrd.open_workbook(biaozhufile)
    ys=xlrd.open_workbook(yuanshifile)
    bzSheet=bz.sheet_by_name(sheetname)
    ysSheet=ys.sheet_by_name(sheetname)
    nrows=bzSheet.nrows
    for num in range(nrows):
        yxbx = ysSheet.cell(num, 0).value
        yxzd = bzSheet.cell(num, 0).value
        bzvalue = bzSheet.cell(num, 1).value
        newSheet.write(k, 0, n)
        newSheet.write(k, 1, yxbx)
        newSheet.write(k, 2, yxzd)
        newSheet.write(k, 3, bzvalue)
        k=k+1
        n=n+1
    print(n-1)
    newxlr.save(newfile)