import os
import numpy as np
import nltk
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from gensim.models.word2vec import Word2Vec
import pandas as pd
import csv
#分词加分句
raw_text = ''
import spacy
nlp = spacy.load('en_core_web_sm')

for file in os.listdir("D:\\MY_STUDY\\scientific_research\\MY_NOTEBOOK\\RUNNING\\content\\"):
    if file.endswith(".txt"):
        raw_text = open("D:\\MY_STUDY\\scientific_research\\MY_NOTEBOOK\\RUNNING\\content\\"+file, errors='ignore').read() + '\n\n'
    text = raw_text

    # [fname, fename] = os.path.splitext("D:\\MY_STUDY\\scientific_research\\MY_NOTEBOOK\\RUNNING\\content\\"+file, errors='ignore')
    # print(file)
    ner = nlp.create_pipe("ner")
    doc = nlp(text)
    tokens=[]
    f = open("Word_Seg_5.csv", "a+",encoding="UTF-8")
    f.write(file)
    f.write('\n')
    for token in doc:
        # tokens.append(token.text)
        tokens += [token.text,"~O"]
        # tokens.append('\n')
        # print(tokens)
    tmp = 1
    for token in tokens:
        s = ''.join(token)
        f.write(s)
        tmp+=1
        if(tmp%2==1):
            f.write('\n')
            tmp=1
    f.close()

    ff = open("Sent_Seg_5.txt","a+",encoding="UTF-8")
    ff.write(file)
    ff.write('\n')
    for sent in doc.sents:
        print(sent,file=ff)
'''
    with open("seg.csv","w+") as datacsv:
        csvwriter = csv.writer(datacsv)
        for token in tokens:
            csvwriter.writerow(token)
'''
'''
    with open("seg.csv", "w+") as datacsv:
        # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
        csvwriter = csv.writer(datacsv)
        # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
        csvwriter.writerow(tokens)
'''
    # print(list(doc.sents))
'''
    with open("sent_seg_3186_3192.txt", "a+", newline="") as datacsv:
        # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
        csvwriter = csv.writer(datacsv)
        # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
        csvwriter.writerow(file)
        csvwriter.writerow(list(doc.sents))
'''
