from flask import Flask
from bluePrint import bp
# from test import bp

app = Flask(__name__)
app.config['REDIS_HOST'] = "127.0.0.1"  # redis数据库地址
app.config['REDIS_PORT'] = 6379  # redis 端口号
app.config['REDIS_DB'] = 0  # 数据库名
app.config['REDIS_EXPIRE'] = 60  # redis 过期时间60秒
# 注册接口
app.register_blueprint(bp, url_prefix='/')

if __name__ == "__main__":
    app.run()
