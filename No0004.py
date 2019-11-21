# -*- coding: utf-8 -*-
import io
import sys
import re
import pandas as pd
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 改变标准输出的默认编码

f = open('file_name')
# 通过正则表达式设定分隔符
key = re.compile(r'[,.?:\s\n]')
# 利用分隔符分隔文本
subs = re.split(key,f.read())
# 去掉所有的空字符
while '' in subs:
    subs.remove('')
print(subs)
f.close()
# 进行词频统计
word_count = pd.value_counts(subs)
print(type(word_count))
#<class 'pandas.core.series.Series'>
# 词语列表
word = list(word_count.index)
# 词频列表
count = list(word_count.values)
