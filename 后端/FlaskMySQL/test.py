import uuid
from flask import Flask, request, json, Response, render_template
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'Authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Text, nullable=False)


db.create_all()


# def generate_reqst(usernames, ages):
#     username = request.args.get(usernames)
#     age = request.args.get(ages)
#     article = Article(username=username, age=age)
#     db.session.add(article)
#
# with app.test_request_context():
#     generate_reqst("zs","12")
#     db.session.commit()

@app.route('/add')
def add():
    username = request.args.get("username")
    age = request.args.get("age")
    article = Article(username=username, age=age)
    db.session.add(article)
    db.session.commit()
    return "insert successfully"


@app.route('/showall')
def showall():
    result = Article.query.all()
    return render_template("show.html", result=result)


@app.route('/query')
def query():
    data = Article.query.all()
    result = int(request.args.get("id"))
    # print(data[result].username)
    return (data[result].username)


@app.route('/deletefirst')
def deletefirst():
    result = Article.query.filter(Article.age == '12').first()
    db.session.delete(result)
    db.session.commit()
    return "delete successfully"


