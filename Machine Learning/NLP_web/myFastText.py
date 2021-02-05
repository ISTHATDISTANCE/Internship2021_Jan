import os
import re
import jieba
import fasttext.FastText as fasttext
import numpy as np


class _MD(object):
    mapper = {
        str: '',
        int: 0,
        list: list,
        dict: dict,
        set: set,
        bool: False,
        float: .0
    }

    def __init__(self, obj, default=None):
        self.dict = {}
        assert obj in self.mapper, \
            'got a error type'
        self.t = obj
        if default is None:
            return
        assert isinstance(default, obj), \
            f'default ({default}) must be {obj}'
        self.v = default

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __getitem__(self, item):
        if item not in self.dict and hasattr(self, 'v'):
            self.dict[item] = self.v
            return self.v
        elif item not in self.dict:
            if callable(self.mapper[self.t]):
                self.dict[item] = self.mapper[self.t]()
            else:
                self.dict[item] = self.mapper[self.t]
            return self.dict[item]
        return self.dict[item]


def defaultdict(obj, default=None):
    return _MD(obj, default)

class Trainer(object):

    def __init__(self):
        f = open("data/stop_words_utf-8.txt", mode='r', encoding='utf-8')
        self.stop_words = [line.strip() for line in f.readlines()]
        f.close()

    @staticmethod
    def eliminate(cont):
        el = re.compile(r"[^0-9a-zA-Z\u4e00-\u9fa5]+")
        return el.sub("", cont)

    def loadData(self, path):
        if os.path.isfile(path):
            tr = open(path, 'r')
            fw = open(path.strip('.tsv') + '_rev.txt', 'w')
            for line in tr.readlines():
                cla, cont = line.split('\t', 1)
                contEl = self.eliminate(cont)
                fw.write("__label__" + cla + ' , ')
                for i in jieba.cut(contEl):
                    if i not in self.stop_words:
                        fw.write(i + ' ')
                fw.write('\n')
        else:
            print("File not exists!")


    def train_model(self, ipt=None, opt=None, model='', dim=100, epoch=0.5, lr=0.1, loss='softmax'):
        np.set_printoptions(suppress=True)
        classifier = fasttext.train_supervised(ipt, label='__label__', dim=dim, epoch=epoch,
                                               lr=lr, wordNgrams=3, loss=loss)
        classifier.save_model(opt)
        return classifier

    def training(self):
        dim = 100
        lr = 0.5
        epoch = 5
        model = f'model/data_dim{str(dim)}_lr0{str(lr)}_iter{str(epoch)}.model'

        self.train_model(ipt='data/train_rev.txt',
                                 opt=model,
                                 model=model,
                                 dim=dim, epoch=epoch, lr=lr
                                 )
        # result = classifier.test('data/train_rev.txt')
        # print(result)
        # result = classifier.test('data/val_rev.txt')
        # print(result)
        # result = classifier.test('data/te_rev.txt')
        # print(result)
