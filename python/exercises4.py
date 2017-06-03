# -*- coding: utf-8 -*-
article="this is a python and Python"
article=article.lower()
wordcount={}
article_list=article.split(' ')
for k in article_list:
    if k in wordcount:
        wordcount[k]=wordcount[k]+1
    else:
        wordcount[k]=1
items=wordcount.items()
items.sort(key=lambda x:x[1],reverse=True)
word,count=items[0]
print(word)
# print "单词出现最多是： "+str(word)+" 出现的次数为： "+str(count)