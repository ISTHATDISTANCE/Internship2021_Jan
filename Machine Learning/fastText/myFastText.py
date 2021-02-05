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


def eliminate(cont):
    el = re.compile(r"[^0-9a-zA-Z\u4e00-\u9fa5]+")
    return el.sub("", cont)

def sep(sen, stop_words):
    contEl = eliminate(sen)
    return ' '.join([i for i in jieba.cut(contEl) if i not in stop_words])


def loadData(path):
    if os.path.isfile(path):
        tr = open(path, 'r')
        f = open("data/stop_words_utf-8.txt", mode='r', encoding='utf-8')
        stop_words = [line.strip() for line in f.readlines()]
        f.close()
        fw = open(path.strip('.tsv') + '_rev.txt', 'w')
        for line in tr.readlines():
            cla, cont = line.split('\t', 1)
            contEl = eliminate(cont)
            fw.write("__label__" + cla + ' , ')
            for i in jieba.cut(contEl):
                if i not in stop_words:
                    fw.write(i + ' ')
            fw.write('\n')
    else:
        print("File not exists!")


def train_model(ipt=None, opt=None, model='', dim=100, epoch=5, lr=0.1, loss='softmax'):
    np.set_printoptions(suppress=True)
    if os.path.isfile(model):
        classifier = fasttext.load_model(model)
    else:
        classifier = fasttext.train_supervised(ipt, label='__label__', dim=dim, epoch=epoch,
                                               lr=lr, wordNgrams=3, loss=loss)
    classifier.save_model(opt)
    return classifier


def cal_precision_and_recall(file, stop_words):
    precision = defaultdict(int, 1)
    recall = defaultdict(int, 1)
    total = defaultdict(int, 1)
    with open(file) as f:
        for line in f:
            label, content = line.split(',', 1)
            total[label.strip().strip('__label__')] += 1
            labels2 = classifier.predict([sep(content,stop_words)])
            pre_label, sim = labels2[0][0][0], labels2[1][0][0]
            recall[pre_label.strip().strip('__label__')] += 1

            if label.strip() == pre_label.strip():
                precision[label.strip().strip('__label__')] += 1

    print('precision', precision.dict)
    print('recall', recall.dict)
    print('total', total.dict)
    for sub in precision.dict:
        pre = precision[sub] / total[sub]
        rec = precision[sub] / recall[sub]
        F1 = (2 * pre * rec) / (pre + rec)
        print(f"{sub.strip('__label__')}  precision: {str(pre)}  recall: {str(rec)}  F1: {str(F1)}")


if __name__ == '__main__':
    # loadData('data/train.tsv')
    # loadData('data/test.tsv')
    # loadData('data/val.tsv')
    f = open("data/stop_words_utf-8.txt", mode='r', encoding='utf-8')
    stop_words = [line.strip() for line in f.readlines()]
    dim = 100
    lr = 0.5
    epoch = 5
    model = f'model/data_dim{str(dim)}_lr0{str(lr)}_iter{str(epoch)}.model'

    classifier = train_model(ipt='data/train_rev.txt',
                             opt=model,
                             model=model,
                             dim=dim, epoch=epoch, lr=lr
                             )
    result = classifier.test('data/train_rev.txt')
    print(result)
    result = classifier.test('data/val_rev.txt')
    print(result)
    result = classifier.test('data/te_rev.txt')
    print(result)
    # cal_precision_and_recall('data/te_rev.txt', stop_words)
    # sen = "A股大涨"
    # label = classifier.predict(sep(sen, stop_words))
    # print(label)
