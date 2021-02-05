import fasttext.FastText as fasttext
import jieba
import re


class Predict(object):
    def __init__(self):
        jieba.enable_paddle()
        f = open("data/stop_words_utf-8.txt", mode='r',
                 encoding='utf-8')
        self.stop_words = [line.strip() for line in f.readlines()]
        f.close()
        print("停用词加载成功")
        self.classifier = fasttext.load_model(
            'model/data_dim100_lr00.5_iter5.model')
        print("模型加载成功")

    @staticmethod
    def eliminate(self, cont):
        el = re.compile(r"[^0-9a-zA-Z\u4e00-\u9fa5]+")
        return el.sub("", cont)

    @staticmethod
    def sep(self, sen):
        contEl = self.eliminate(self, sen)
        return ' '.join([i for i in jieba.cut(contEl, use_paddle=True) if i not in self.stop_words])


    def pred(self, sen):
        label = self.classifier.predict(self.sep(self, sen))[0][0]
        label = label.strip("__label__")
        cate = {
            '0': "文化",
            '1': "娱乐",
            '2': '体育',
            '3': '财经',
            '4': '房产',
            '5': '汽车',
            '6': '教育',
            '7': '科技',
            '8': '军事',
            '9': '旅游',
            '10': '国际',
            '11': '证券',
            '12': '农业',
            '13': '电竞',
            '14': '民生'
        }
        return cate[label]
