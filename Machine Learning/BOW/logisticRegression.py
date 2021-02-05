from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.linear_model import LogisticRegression
from sklearn import svm

vectorizer = CountVectorizer(ngram_range=(1, 1), token_pattern=r"(?u)\b\w+\b")
file = open("./data/train.tsv", mode="r", encoding="utf-8")
data = file.readlines()
# print(data)
x = []
for i in range(0, len(data) - 1):
    w = ""
    for j in range(0, len(data[i]) - 1):
        if data[i][j] == '\t':
            break
        else:
            w = w + data[i][j]
    x.append(w)
y = []
for i in range(0, len(data) - 1):
    n = int(data[i][len(data[i]) - 2])
    if data[i][len(data[i]) - 3] == '-':
        n = -n
    y.append(n)
# vectorizer.fit(x)
x_train = vectorizer.fit_transform(
    x)  # fit_transform creates a new word list and then do the transformation (create a vector that can be recognized by computer)
# print(x_train)
# print(y)

# model = LogisticRegression()
model = svm.NuSVC()
model.fit(x_train, y)
test = ["是的", "不对，不是的是开心的s", "不是", "错了错了，是打给成功，成功的功", "是成功的成"]
print(model.predict(vectorizer.transform(test)))
file.close()
