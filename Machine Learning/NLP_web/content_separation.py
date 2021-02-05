import jieba.posseg as pseg
import jieba.analyse
import re


class Separation(object):
    def __init__(self):
        jieba.enable_paddle()

    @staticmethod
    def eleminate(sen):
        el = re.compile(r"[a-zA-Z!\"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~\s]+")
        return el.sub("", sen)

    def separate(self, sen):
        # sen = "股票00700走势大好天安门"
        sen = self.eleminate(sen)
        # print(sen)
        words = pseg.cut(sen)
        # for word, flag in words:
        #     print("%s %s" %(word, flag_en2cn[flag]))
        return words
