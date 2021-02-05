from sklearn import svm
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import jieba


def training(tr_x, tr_y, Vec):
    # model = svm.SVC()
    # model = MultinomialNB(alpha=0.00001)
    model = LogisticRegression()
    tr_x_vec = Vec.fit_transform(tr_x)

    model.fit(tr_x_vec, tr_y)
    # save the model
    joblib.dump(model, 'models/model_logReg.pkl')
    joblib.dump(Vec, 'models/vec_logReg.pkl')
    return model


def testing(model, Vec):
    te = open("test.tsv", mode='r', encoding='utf-8')
    te_x = list()
    te_y = list()
    te_data = te.readlines()
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
    # print(stop_words[50])
    Vec = TfidfVectorizer(stop_words=stop_words, tokenizer=jieba_tokenizer, lowercase=False)
    model = training(tr_x, tr_y, Vec)
    # Vec = joblib.load('models/vec_MultinomialNB.pkl')
    # model = joblib.load('./models/model_MultinomialNB.pkl')
    print(1)
    testing(model, Vec)
    tr.close()


if __name__ == '__main__':
    main()
