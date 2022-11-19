import jieba.analyse

# TF-IDF 获取关键词列表
txt = ''
with open('./txt/noob/noob.txt', 'r', encoding='utf-8') as f:
    txt += f.read()

tags = jieba.analyse.extract_tags(txt, topK=200, withWeight=True, allowPOS=('n', 'nz', 'nr', 'ns', 'v', 'an', 'eng'))

# 输出至excel
import pandas as pd

df = pd.DataFrame(tags, columns=['key', 'value'])
df.to_csv('noob.csv', encoding='gb2312')
