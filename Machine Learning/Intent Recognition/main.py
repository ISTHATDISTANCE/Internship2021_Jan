import jieba
import jieba.posseg as pseg
import jieba.analyse
import re

jieba.enable_paddle()

def eleminate(sen):
    el = re.compile(r"[a-zA-Z!\"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~\s]+")
    return el.sub("", sen)

if __name__ == '__main__':
    flag_en2cn = {
        'a': '形容词', 'ad': '副形词', 'ag': '形语素', 'an': '名形词', 'b': '区别词',
        'c': '连词', 'd': '副词', 'df': '不要', 'dg': '副语素',
        'e': '叹词', 'f': '方位词', 'g': '语素', 'h': '前接成分',
        'i': '成语', 'j': '简称略语', 'k': '后接成分', 'l': '习用语',
        'm': '数词', 'mg': '数语素', 'mq': '数量词',
        'n': '名词', 'ng': '名语素', 'nr': '人名', 'nrfg': '古近代人名', 'nrt': '音译人名',
        'ns': '地名', 'nt': '机构团体', 'nz': '其他专名',
        'o': '拟声词', 'p': '介词', 'q': '量词',
        'r': '代词', 'rg': '代语素', 'rr': '代词', 'rz': '代词',
        's': '处所词', 't': '时间词', 'tg': '时间语素',
        'u': '助词', 'ud': '得', 'ug': '过', 'uj': '的', 'ul': '了', 'uv': '地', 'uz': '着',
        'v': '动词', 'vd': '副动词', 'vg': '动语素', 'vi': '动词', 'vn': '名动词', 'vq': '动词',
        'x': '非语素字', 'y': '语气词', 'z': '状态词', 'zg': '状态语素','LOC': '专有地名', 'PER': '专有人名',
        'ORG': '组织名', 'TIME': '时间'
    }
    sen = "T申"
    # sen = eleminate(sen)
    # print(sen)
    words = pseg.cut(sen)
    for word, flag in words:
        print("%s %s" %(word, flag_en2cn[flag]))