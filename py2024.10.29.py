
from PIL import Image
import jieba
import jieba.posseg as pg
import numpy as np
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
wine=pd.read_csv(r'winequality-red.csv',sep=';')
wine.to_excel('1.xlsx')
print(wine.head())
# txt='正在安装“textblob==0.18.0”'
# lst=pg.lcut(txt)
# words=jieba.lcut(txt)
# print(lst)
# for i,j in lst:
#     print(f"{i},{j}")
# with open(r'百度停用词列表.txt','r') as file:
#     swds=file.read().split('\n')
# with open(r'三国演义.txt','r',encoding='Ansi') as file:
#     text=file.read()
# words=jieba.cut(text)
# clw=[i for i in words if i not in swds and len(i)>2]
# wordc=Counter(clw)
# mask_i=Image.open("D:\6.jpg")
# wc=WordCloud(font_path='simhei.ttf',width=800,height=800,mask=mask_i,min_word_length=2,background_color='white').generate_from_frequencies(wordc)
# wc.to_file('2.jpg')
# image=wc.to_image()
# image.show()
# print(wordc)