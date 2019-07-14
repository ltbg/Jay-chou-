# -*- coding: utf-8 -*-
import os
from collections import Counter
import  jieba
import wordcloud
from wordcloud import WordCloud
import matplotlib
from matplotlib import pyplot
from scipy.misc import imread
from pylab import mpl

#
# def stopwordslist(filepath):
#     stopwords = [line.strip() for line in open(filepath, 'rb').readlines()]
#     return stopwords
# stopwords=stopwordslist('C:/Users/Administrator/PycharmProjects/stoplist.txt')

stopwords=[u"薛之谦",u"母",u"带",u"合音",u"什么",u"郑伟",u"他",u"到",u"所以",u"已经",u"用",u"赵靖",u"越",u"太",u"",u"",u"",u"",u"",u"",u"",u"",u"",u"",u"",u"可",u"里",u"不要",u"录制",u"别",u"可以",u"找",u"莫家伟",u"母带",u"",u"",u""u'下',u'我',u'的',u'在',u'制作',u"作词",u"你",u"作曲",u"编曲",u"不",u"是",u"了",u"说",u"要",u"人",u"录音师",u"录音室",u"着",u"说",u"就",u"谢",u"春花",u"谢知",u"吉他",u"再",u"不会",u"把",u"像",u"没有",u"Gary",u"杩",u"叫",u"看",u"只",u"涓",u"浣",u"仓雁彬",u"也",u"小皮",u"非",u"人声",u"studio",u"和",u"造音",u"时俊峰",u"等",u"被",u"还",u"而",u"JVR",u".",u"（",u"）",u"却",u"将",u"师",u"对",u"因为",u"怎么",u"让",u"去",u"会",u"又",u"很",u"录音",u"工作室",u"杨大纬",u"上",u"真的",u"Studio",u"杨瑞代",u"方文山",u"都",u"有",u"这",u"那",u"谁",u"混音",u"更",u"能",u"飞",u"贝司",u"高",u"懂",u"没",u"@",u"好",u"中",u"鼓",u"福达",u"懂过",u"键盘",u"秦孟达",u"来",u"音乐",u"曾嵘",u"卢山",u"过",u"多"]

all_words=[]
outstr = ''
for filename in os.listdir('5781'):
    with open('5781/'+filename) as f:
        lyrics=f.read()
        data=jieba.cut(lyrics)
        all_words.extend(set(data))
for word in all_words:
    if word not in stopwords:
        if word != '\t':
            outstr += word
            outstr += " "
all_words_new= outstr.split(" ")

count=Counter(all_words_new)
result=sorted(count.items(), key=lambda x: x[1], reverse=True)
print(result)

word_dic=dict(count.items())

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
color_mask=imread('C:/Users/Administrator/Desktop/1.png')
cloud=WordCloud(
    font_path='C:\Windows\Fonts\SIMYOU.TTF',
    width=600,
    height=480,
    background_color='white',
    mask=color_mask,
    max_words=500,
    max_font_size=150)
world_cloud=cloud.fit_words(word_dic)
world_cloud.to_file('123.jpg')
pyplot.imshow(world_cloud)
