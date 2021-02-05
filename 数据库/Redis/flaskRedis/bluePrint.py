from flask import Blueprint, render_template, current_app, request
import random

from usage import Redis

bp = Blueprint("ltt", __name__)


# host = current_app.config['REDIS_HOST']
# port = current_app.config['REDIS_PORT']
# db = current_app.config['REDIS_DB']
# r = redis.StrictRedis(host, port, db)


@bp.route('/')
def idx():
    return render_template("index.html")


@bp.route('/verification', methods=['get', 'post'])
def verify():
    if request.method == 'POST':
        num = request.get_json()["id"]
        print(num)

        code = ""
        for i in range(0, 6):
            code += str(random.randint(0, 9))
        Redis.setCode(str(num), code)
        return {
            "code": code,
            "key": str(num)
        }
    else:
        print(request.method)
        return {}


@bp.route('/check', methods=['get', 'post'])
def check():
    if request.method == 'POST':
        ipt = request.get_json()["input"]
        key = request.get_json()["key"]

        print(type(ipt))
        if ipt == Redis.getCode(key):
            return {"result":1}
        else:
            return {"result":0}
    else:
        print(request.method)
        return {}


@bp.route('/success')
def suc():
    return render_template("success.html")


@bp.route('/fail')
def fail():
    return render_template("fail.html")
