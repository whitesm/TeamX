#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud
from collections import Counter

font_name = font_manager.FontProperties(fname="app/AppleGothic.ttf").get_name()
rc('font', family=font_name)

def wc(t,s):
    c=[]
    f=open(t).read()
    words = []
    word_list = f.lower().split('\n')
    for word in word_list:
        word = word.replace("조금","")
        word = word.replace("약간","")
        words.append(word)
    c = Counter(word_list)
    wordcloud=WordCloud(background_color='white',font_path='AppleGothic.ttf').generate_from_frequencies(c)
    plt.figure(figsize=(8,8))
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")
    plt.savefig(s, dpi=300)
