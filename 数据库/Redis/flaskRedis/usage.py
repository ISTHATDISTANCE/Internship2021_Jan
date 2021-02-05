import redis
from flask import current_app


class Redis(object):

    @staticmethod
    def _get_r():
        # get obj
        host = current_app.config['REDIS_HOST']
        port = current_app.config['REDIS_PORT']
        db = current_app.config['REDIS_DB']
        r = redis.StrictRedis(host, port, db)
        return r

    @classmethod
    def setCode(cls, key, val):
        r = cls._get_r()
        r.set(key, val, ex=60)

    @classmethod
    def getCode(cls, key):
        r = cls._get_r()
        value = r.get(key)
        return value.decode('utf-8') if value else value
