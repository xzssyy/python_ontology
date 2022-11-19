import logging
import os.path
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(
        sys.argv[0])  # os.path.basename表示返回path最后的文件名；sys.argv[0]表示传递命令行参数，参数train_word2vec_model.py为argv[0]
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)  ##
    logging.info("running %s" % ' '.join(sys.argv))  # info表示打印，Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    if len(sys.argv) < 4:
        print(globals()['__doc__'] % locals())  # 全局变量，局部变量
        sys.exit(1)
    inp, outp, outp2 = sys.argv[1:4]  # 依次表示切割后的文本，模型，向量
    model = Word2Vec(LineSentence(inp), vector_size=20, window=10, min_count=10, epochs=20,
                     workers=multiprocessing.cpu_count())
    # size指的是词向量维度的大小，维度越大，需要的语料越多；window是句子中当前词与目标词之间的最大距离；min_count是用于设置舍弃词的阈值，低于这个值的词语自动舍弃；Iter训练模型的迭代次数
    model.save(outp)  # 训练后的模型保存；# 以二进制格式存储
    model.wv.save_word2vec_format(outp2, binary=False)  # 以文本格式存储, 一行是一个词的vector


# python train_model.py ../spider/txt/noob/seg_noob.txt noob.model noob.vector
