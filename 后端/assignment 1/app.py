from flask import Flask, render_template, request, jsonify
import pymysql
import json

app = Flask(__name__)

db = pymysql.connect(host="localhost", user="root", password="Lt@6890838", database="ass")


@app.route('/', methods=["get", "post"])
def hello_world():
    cursor = db.cursor()
    cursor.execute(
        "select name from area where LEVEL = 1"
    )
    data = cursor.fetchall()
    res = []
    for i in range(0, len(data)):
        res.append(data[i][0])
    return render_template("index.html", res=res)


@app.route('/showcity', methods=["get", "post"])
def showcity():
    if request.method == 'POST':
        rev = request.get_json()['province']
        # print(rev)
        cursor = db.cursor()
        sql = "select name from area where parent_id = (select id from area where level = 1 && name = \'" + str(
            rev) + "\') && level = 2;"
        cursor.execute(sql)
        # print(sql)
        data = cursor.fetchall()
        res = []
        for i in range(0, len(data)):
            res.append(data[i][0])
        return jsonify(res)
        # return render_template("show.html", res=data)
    else:
        print(1)
        return render_template('show.html')


@app.route('/showcounty', methods=["get", "post"])
def showcounty():
    if request.method == 'POST':
        rev = request.get_json()['city']
        # print(rev)
        cursor = db.cursor()
        sql = "select name from area where parent_id = (select id from area where level = 2 && name = \'" + str(
            rev) + "\') && level = 3;"
        cursor.execute(sql)
        # print(sql)
        data = cursor.fetchall()
        res = []
        for i in range(0, len(data)):
            res.append(data[i][0])
        return jsonify(res)
        # return render_template("show.html", res=data)
    else:
        print(1)
        return render_template('show.html')


if __name__ == '__main__':
    app.run()
