# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:16:46 2018

@author: kingkong
"""
import jieba
import xlrd,xlwt
#加载停用词表
stopwords = [line.strip() for line in open('E:\\dic\\stop1.txt', 'r', encoding='utf-8').readlines()]

#jieba.load_userdict('E:\\dic\yxfcb.txt')
#jieba.load_userdict('E:\\dic\jibing_pos_name.txt')
#jieba.load_userdict('E:\\dic\symptom_pos.txt')
jieba.suggest_freq("未见",True)#添加字典无效？好像jieba默认自定义长词有效，自定义短词无效
jieba.suggest_freq("异常",True)
jieba.add_word('未见')
def read_excel():
    data = xlrd.open_workbook('E:\\ctdata_yxbx.xls')
    file = xlwt.Workbook()
    table_w =file.add_sheet("fc",cell_overwrite_ok=True)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    
    for i in range(nrows):
        list = jieba.cut(str(table.row(i)[0].value),cut_all=False)
        outstr = ''
     #   value = "|".join(list)
        for word in list:
            if word not in stopwords:
                if word !='\t':
                    if word !=' ':    
                        outstr += word
                        outstr +=' '
        print(outstr)           
     #   print(value)    
        if i >= 0:
          #  table_w.write(i,0,table.row_values(i)[0])
          #  table_w.write(i,1,outstr)
          #  table_w.write(i,0,table.row_values(i)[0])
            table_w.write(i,0,outstr)   
 
    file.save('E:\\fcout1.xls')     

read_excel()    

        
    
