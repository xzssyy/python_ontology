import gensim
import pandas as pd
import numpy as np

if __name__ == '__main__':


    word_list = [u'数字', u'字符串', u'列表', '元组', '集合', '字典']
    model_path = '../Word2Vector/noob.model'
    model = gensim.models.Word2Vec.load(model_path)
    df = pd.DataFrame()

    pd.DataFrame(np.ndarray(shape=(8, 5), dtype=str))

    index_list = []
    for x in word_list:
        index_list.append((x, '相关'))
        index_list.append((x, '向量值'))

    index = pd.MultiIndex.from_tuples(index_list)

    list_t = []
    for w in word_list:
        result = model.wv.most_similar(w, topn=50)
        list_t.append([])
        list_t.append([])
        for word in result:
            list_t[-1].append(word[1])
            list_t[-2].append(word[0])


    df = pd.DataFrame(list_t, index=index)
    df.to_csv('Word2Vector.csv', encoding='gb2312')


