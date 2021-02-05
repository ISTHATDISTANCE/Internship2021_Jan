from sklearn import svm
from sklearn import metrics

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import jieba


def training(tr_x, tr_y, Vec, te_x, te_y):
    # model = svm.SVC()
    tr_x_vec = Vec.fit_transform(tr_x)
    para = validate(Vec, te_x, te_y)
    model = MultinomialNB(alpha=para)

    model.fit(tr_x_vec, tr_y)
    # save the model
    joblib.dump(model, 'models/model_MultinomialNB.pkl')
    joblib.dump(Vec, 'models/vec_MultinomialNB.pkl')
    return model


def validate(Vec, te_x, te_y):
    res = 0
    m = -1
    c = 1000
    for i in range(1,c):
        model = MultinomialNB(alpha=i / c)
        model.fit(Vec.transform(te_x), te_y)
        # pd = model.predict(Vec.transform(te_x))
        x = model.score(Vec.transform(te_x), te_y)
        if x > m:
            res = i
            m = x
    return res/c


def testing(model, Vec):
    te = open("test.tsv", mode='r', encoding='utf-8')
    te_x = list()
    te_y = list()
    te_data = te.readlines()
    # print((tr_data[1][0]))
    for i in range(1, len(te_data)):
        j = 0
        cla = 0
        while te_data[i][j] != '\t':
            cla = cla * 10 + int(te_data[i][j])
            j = j + 1
        j = j + 1
        te_y.append(cla)
        w = ""
        while j < len(te_data[i]) - 1:
            w = w + te_data[i][j]
            j = j + 1
        te_x.append(w)
    # data = list()
    # for i in range(len(te_x)):
    #     segw = jieba.cut(te_x[i])
    #     for w in segw:
    #         feature = ' '.join(w)
    #         data.append(feature)
    # te_x_vec = TfidfVectorizer().fit_transform(te_x)
    # te_x_vec = ['2018年美国中期选举，你认为特朗普会下台吗？', '刘涛王子文遭道德绑架，没送生日祝福给蒋欣，被质疑是塑料姐妹花']
    res = model.predict(Vec.transform(te_x))
    # print(model.score(Vec.transform(te_x), te_y))
    print(metrics.classification_report(te_y, res))


def jieba_tokenizer(text):
    return jieba.lcut(text)


def main():
    # Read training set
    tr = open("train.tsv", mode='r', encoding='utf-8')
    tr_x = list()
    tr_y = list()
    tr_data = tr.readlines()
    # print((tr_data[1][0]))
    for i in range(1, len(tr_data)):
        j = 0
        cla = 0
        while tr_data[i][j] != '\t':
            cla = cla * 10 + int(tr_data[i][j])
            j = j + 1
        j = j + 1
        tr_y.append(cla)
        w = ""
        while j < len(tr_data[i]) - 1:
            w = w + tr_data[i][j]
            j = j + 1
        tr_x.append(w)
    # print(tr_x[0])
    # print(tr_y)
    f = open("stop_words_utf-8.txt", mode='r', encoding='utf-8')
    stop_words = [line.strip() for line in f.readlines()]
    te = open("val.tsv", mode='r', encoding='utf-8')
    te_x = list()
    te_y = list()
    te_data = te.readlines()
    # print((tr_data[1][0]))
    for i in range(1, len(te_data)):
        j = 0
        cla = 0
        while te_data[i][j] != '\t':
            cla = cla * 10 + int(te_data[i][j])
            j = j + 1
        j = j + 1
        te_y.append(cla)
        w = ""
        while j < len(te_data[i]) - 1:
            w = w + te_data[i][j]
            j = j + 1
        te_x.append(w)
    Vec = TfidfVectorizer(stop_words=stop_words, tokenizer=jieba_tokenizer, lowercase=False)
    model = training(tr_x, tr_y, Vec, te_x, te_y)
    # Vec = joblib.load('models/vec_MultinomialNB.pkl')
    # model = joblib.load('./models/model_MultinomialNB.pkl')
    print(1)
    testing(model, Vec)
    tr.close()


if __name__ == '__main__':
    main()
