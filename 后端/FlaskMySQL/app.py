import uuid
from flask import Flask, request, json, Response, render_template
from flask_sqlalchemy import SQLAlchemy

import pymysql

db = pymysql.connect("localhost", "root", "Lt@6890838", "ass")

app = Flask(__name__)


@app.route('/')
def idx():
    return render_template("login.html");


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/registered')
def registered():
    try:
        name = str(request.args.get("name"))
        sex = str(request.args.get("sex"))
        email = str(request.args.get("email"))
        username = str(request.args.get("username"))
        psw = str(request.args.get("psw"))
        sql = "insert into users (`name`,sex,email,userName,psw) values (\'" + name + "\',\'" + sex + "\',\'" + email + "\',\'" + username + "\',\'" + psw + "\');"
        print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        return render_template("afterReg.html", res="注册成功！")
    except:
        return render_template("afterReg.html", res="您的用户名已经被注册！")


@app.route('/login')
def login():
    username = str(request.args.get("username"))
    psw = str(request.args.get("psw"))
    print(username, psw)
    if (username == "" or psw == ""):
        return render_template("login.html", res="账号或密码不能为空！")
    cursor = db.cursor()
    sql = "select * from users where userName=\'" + username + "\'&& psw=\'" + psw + "\';"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    if data != ():
        return render_template("welcome.html", res=username)
    else:
        return render_template("login.html", res="账号或密码错误！")


if __name__ == '__main__':
    app.run()
    db.close()
