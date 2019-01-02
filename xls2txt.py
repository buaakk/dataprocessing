# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:35:32 2018
将xls转为txt，将数据和标注打包形成对(数据，标注),
@author: kingkong
"""
    #将分词数据按元祖写入txt    
import xlrd
import random
import copy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
#将数据和标注打包形成对(数据，标注)
sentences1 = []
def excel2txt():
    global sentences1
    num = 0
    data = xlrd.open_workbook('E:\\traindata\\bzfenci.xls')
    file = open("E:\\traindata\\bz2txt.txt", "a")
    sentences = []
    table = data.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    
    for i in range(nrows):
        col0 = table.row(i)[0].value #col0为str类型
        col1 = table.row(i)[1].value
        num = num+1
        sentences.append((col0, col1)) #作为元组存入list
    random.shuffle(sentences)
    sentences1 =copy.deepcopy(sentences)
    #print(num)
 #   for sen in sentences[:3]:
      #  print(sen[0], sen[1])        
  #  file.write(str(sentences))#sentence为list,需要转为str才能写入
  #  file.close()
excel2txt()

#特征提取
vec = CountVectorizer(
        analyzer='word', # tokenise by character ngrams
        ngram_range=(1,4), #优化，是指将text分成min，min+1，min+2,max个不同的词组，优化到0.77
        max_features=20000,  # keep the most common 1000 ngrams
        
    )
#生成训练集测试集
#print(sentences1)
x, y = zip(*sentences1)#zip(*)为解压元祖
#test_size为x_test, y_test的数量，如果为小数比如0.2，则为比例
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=16888,random_state=0) 
print(y_test)
for i in range(len(y_train)):
    if y_train[i] =='A':
        y_train[i]=0
    elif y_train[i] =='B':
        y_train[i]=1
    elif y_train[i] =='C':
        y_train[i]=2
for i in range(len(y_test)):
    if y_test[i] =='A':
        y_test[i]=0
    elif y_test[i] =='B':
        y_test[i]=1
    elif y_test[i] =='C':
        y_test[i]=2   
print(y_test)

#把训练数据转换为词袋模型
vec.fit(x_train)
'''
#使用朴素贝叶斯训练
classifier = MultinomialNB()
classifier.fit(vec.transform(x_train), y_train)
print(classifier.score(vec.transform(x_test), y_test))
#pre = classifier.predict(vec.transform(x_test)) 预测
#print(pre)

#使用svm训练，准确率0.8745
from sklearn.svm import SVC
svm = SVC(kernel='linear')
svm.fit(vec.transform(x_train), y_train)
print(svm.score(vec.transform(x_test), y_test))
'''

#使用xgboost训练迭代，准确率0.8865（0.2测试集）
import xgboost as xgb  
from sklearn.model_selection import StratifiedKFold  
# xgb矩阵赋值  
xgb_train = xgb.DMatrix(vec.transform(x_train), label=y_train)  
xgb_test = xgb.DMatrix(vec.transform(x_test)) 

dtrain = xgb.DMatrix(vec.transform(x_train), label=y_train)
dtest = xgb.DMatrix(vec.transform(x_test),label=y_test)  # label可以不要，此处需要是为了测试效果
param = {'max_depth':6, 'eta':0.5, 'eval_metric':'merror', 'silent':1, 'objective':'multi:softmax', 'num_class':3}  # 参数
evallist  = [(dtrain,'train'), (dtest,'test')]  # 这步可以不要，用于测试效果
num_round = 500  # 循环次数
bst = xgb.train(param, dtrain, num_round, evallist)
preds = bst.predict(dtest)

