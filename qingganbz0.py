#!/usr/bin/python
# coding=utf-8
'''
处理原始文本 情感标注
'''
__author__ = 'Paul'
import xlrd, xlwt
if __name__ == '__main__':
  #  xlsfile  =  'E:\data1.xlsx'
    xlsfile  =  'E:\ctdata_yxzd.xls'
    newfile  =  'E:\\new.xls'
    sheetname  =  u'ctdata'
    newxlr  =  xlwt.Workbook()
    newSheet=newxlr.add_sheet(sheetname)
    myxlr=xlrd.open_workbook(xlsfile)
    mySheet=myxlr.sheet_by_name(sheetname)
    nrows=mySheet.nrows
    k=0
    n=1
    na=0
    nb=0
    nc=0
    for num in range(nrows):
        testcase = mySheet.cell(num, 0).value

        newSheet.write(k, 0, testcase)
     #   print(num + 1)
     #   print(testcase)
     #   print (len(testcase))
        if (('未见异常' in testcase and len(testcase) < 50) or('未见确切' in testcase and len(testcase) < 40 ) or ('未见明显' in testcase and len(testcase) < 50 ) or ('单活胎' in testcase)or ('未见特殊' in testcase) or (('单胎' in testcase) and ('羊水' not in testcase)) or ('正常' in testcase and len(testcase) < 40) or  ('符合' in testcase)or('明显吸收' in testcase and len(testcase) < 40 )or('好转' in testcase ) or ('未探及' in testcase )or('胎' in testcase and '活'in testcase))and('声像'not in testcase  ) and ('骨折' not in testcase) and('炎' not in testcase):
            newSheet.write(k, 1, 'A')
            na=na+1
        elif (('建议' in testcase) or ('结合' in testcase) or ('必要时' in testcase) or ('可能' in testcase) or ('考虑' in testcase) or ('？' in testcase) or ('?' in testcase) or('未见异常' in testcase and '建议' in testcase) or('未见明显' in testcase and '建议' in testcase) or ( '单胎' in testcase) or ('早孕' in testcase)or ('不排除' in testcase)or('积液' in testcase)or ('声像' in testcase and len(testcase) < 25 ) ) and ('炎' not in testcase) and ('改变' not in testcase)and ('伤' not in testcase)and ('骨折' not in testcase) and('肿' not in testcase)and('感染' not in testcase)and('退变' not in testcase)and('退行性' not in testcase )and (len(testcase) < 50):
            newSheet.write(k, 1, 'B')
            nb=nb+1
        elif ('退行性' in testcase) or ('退变' in testcase) or ('感染' in testcase) or ('骨折' in testcase) or ('增生' in testcase) or ('异物' in testcase) or ('肿' in testcase) or ('炎' in testcase)or('金属' in testcase)or('可能性大' in testcase)or('改变' in testcase)or('形成' in testcase)or('增大' in testcase)or('稍大' in testcase)or('厚' in testcase)or('结石' in testcase)or('瘤' in testcase)or('膨出' in testcase)or('突出' in testcase)or('病' in testcase)or('减退' in testcase):
            newSheet.write(k, 1, 'C')
            nc=nc+1
        k=k+1
        n=n+1
         
    print('各分类行数',na,nb,nc)
    newxlr.save(newfile)
        
'''
第二次检索，如果该行为空值，则 
  if 包含 建议 或 进一步 或 必要时 或 结合
     写入B
'''