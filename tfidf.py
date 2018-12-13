# -*- coding: utf-8 -*-
"""
jieba中tf-idf特征提取

This is a temporary script file.
"""
import jieba.analyse
import sys
file = open("E:\\fcouttxt1.txt")

list1 =str(file.read())
#返回关键词
'''
keywords = " ".join(jieba.analyse.extract_tags(list1 , topK=10, withWeight=False, allowPOS=()))
print(keywords)

#返回关键词和权重————元组 （）
keywords = (jieba.analyse.extract_tags(list1 , topK=10, withWeight=True, allowPOS=()))
print(keywords)
'''
#textrank提取关键词
keywords = jieba.analyse.textrank(list1, topK=10, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
print(keywords)