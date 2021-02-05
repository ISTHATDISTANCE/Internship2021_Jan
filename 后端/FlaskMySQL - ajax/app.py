from flask import Flask, request, json, Response, render_template

import pymysql

app = Flask(__name__)

db = pymysql.connect(host="localhost", user="root", password="Lt@6890838", database="ass")


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


@app.route('/registered',methods=["get","post"])
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


if __name__ == '__main__':
    app.run()
