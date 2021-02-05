from flask import Flask, request, json, Response, render_template
import pymysql
from myFastText_predict import Predict
import myFastText
import os
from content_separation import Separation
import time

app = Flask(__name__)

db = pymysql.connect(host="localhost", user="root", password="Lt@6890838", database="ass")

p = Predict()

s = Separation()


def train():
    cursor = db.cursor()
    cursor.execute(
        "select * from document_classification"
    )
    res = list(cursor.fetchall())
    f = open('data/train_rev.txt', 'w')
    for i in res:
        f.write(i[0] + ' , ' + i[1] + '\n')
    t = myFastText.Trainer()
    t.training()
    os.remove('data/train_rev.txt')


@app.route('/')
def idx():
    return render_template("login.html")


@app.route('/login', methods=["get", "post"])
def login():
    username = request.get_json()["username"]
    psw = request.get_json()["psw"]
    print(username, psw)
    if (username == "" or psw == ""):
        return {}
    cursor = db.cursor()
    sql = "select * from users where userName=\'" + username + "\'&& psw=\'" + psw + "\';"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    if data == ():
        return {
            "username": ""
        }
    else:
        return {
            "username": data[0][3]
        }


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/registered', methods=["get", "post"])
def registered():
    try:
        name = request.get_json()["name"]
        sex = request.get_json()["sex"]
        email = request.get_json()["email"]
        username = request.get_json()["username"]
        psw = request.get_json()["psw"]
        sql = "insert into users (`name`,sex,email,userName,psw) values (\'" + name + "\',\'" + sex + "\',\'" + email + "\',\'" + username + "\',\'" + psw + "\');"
        print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        return "注册成功！"
    except:
        return "您的用户名已经被注册！"


@app.route('/regsucc')
def regsucc():
    return render_template("regSucc.html")


@app.route('/regfail')
def regfail():
    return render_template("regFail.html")


@app.route('/welcome')
def welcome():
    uname = request.args.get("username")
    return render_template("welcome.html", res=uname)


@app.route('/doc_classify')
def doc_classify():
    return render_template("docClsf.html")


@app.route('/predict_doc', methods=['POST', 'GET'])
def predict_doc():
    content = request.get_json()['content']
    res = p.pred(content)
    content_sep = p.sep(p, content)
    if (content_sep == ''):
        return {
            "result": "NULL"
        }
    else:
        return {
            'result': res,
        }


@app.route('/add', methods=["GET", "POST"])
def add():
    cla = request.get_json()['class']
    cont = request.get_json()['content']
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
    if p.pred(cont) == cate[str(cla)]:
        return {
            "result": "ok"
        }
    # print("lalala")
    cla = "__label__" + str(cla)
    cont = p.sep(p, cont)
    sql = "insert into document_classification (label, content) values (\'" + cla + "\',\'" + cont + "\')"
    # print(sql)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    train()
    return {
        "result": "done"
    }


@app.route('/training_done')
def training_done():
    return render_template("training_done.html")


@app.route('/int_recognize')
def int_recognize():
    return render_template('int_recognize.html')

@app.route('/predict_int', methods=['GET', 'POST'])
def predict_int():
    cont = request.get_json()['content']
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
        'x': '非语素字', 'y': '语气词', 'z': '状态词', 'zg': '状态语素', 'LOC': '专有地名', 'PER': '专有人名',
        'ORG': '组织名', 'TIME': '时间'
    }
    words = s.separate(cont)
    res = {}
    for word, flag in words:
        res[word] = flag_en2cn[flag]
    res["intent"] = p.pred(cont)
    return res

@app.route('/save', methods=['GET', 'POST'])
def save():
    aud = request.files['wave_file']
    file_name = "Record_" + time.strftime("%Y_%m_%D_%H_%M_%S", time.localtime(time.time())) + ".mp3"
    # aud.save('data/test.mp3')
    aud.seek(0)
    aud_bytes = aud.read()
    print(len(aud_bytes))
    # aud_b64 = base64.b64encode(aud_bytes)
    # print(len(aud_b64))
    aud_hex = ''.join(['%02x' % x for x in aud_bytes])
    # print(aud_hex)
    cursor = db.cursor()
    sql = f"""insert into audio_files (file_name, content) values ('{file_name}', 0x%s);"""
    print(len(sql % aud_hex))
    cursor.execute(
        sql % aud_hex
    )
    db.commit()
    cursor.close()
    return 'done'


@app.route('/download')
def download():
    cursor = db.cursor()
    sql = f"""select max(id), content, file_name from audio_files"""
    cursor.execute(sql)
    res = cursor.fetchall()
    data = {
        "result": str(res[0][1]),
        "filename": str(res[0][2])
    }
    # print(res)
    return data




if __name__ == '__main__':
    app.run()
