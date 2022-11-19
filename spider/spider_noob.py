import re

from requests import request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import jieba
import json

response = request('GET', 'https://www.runoob.com/python3/python3-tutorial.html')
soup = BeautifulSoup(response.content, 'html.parser')

base_url = 'https://www.runoob.com/python3/python3-tutorial.html'
unit_list = soup.find(id='leftcolumn')
a_list = unit_list.find_all('a')

# 保存 tittle, url
with open('url_noob.json', 'w', encoding='utf-8') as f:
    mp = {}
    for a in a_list[:]:
        mp[a.get_text().strip()] = urljoin(base_url, a.get('href'))
    f.write(json.dumps(mp, indent=2).encode('utf-8').decode('unicode_escape'))

# 读取界面信息
with open('url_noob.json', 'r', encoding='utf-8') as f:
    mp = json.loads(f.read())
    all_txt = ''
    for key, value in mp.items():
        tittle = key
        url = value
        response = request('GET', url)
        soup = BeautifulSoup(response.content, 'html.parser')
        txt = soup.find('div', 'article-body').get_text()
        all_txt += tittle + '\n' + re.sub('[^\u4e00-\u9fa5。，]', '', txt) + '。\n'

# 写入文件
with open('txt/noob/noob.txt', 'w', encoding='utf-8') as f:
    f.write(all_txt)

# 分词
with open('seg_noob.txt', 'w', encoding='utf-8') as f:
    seg_list = jieba.cut(all_txt)
    space = ' '
    f.write(space.join(seg_list))
