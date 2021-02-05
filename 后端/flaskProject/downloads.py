from flask import send_from_directory, send_file
from flask import Flask

app = Flask(__name__)


@app.route('/download')
def download():
    # return send_file(r'D:\后端\flaskProject\Image\ltt.jpg')
    # return send_from_directory(r'D:\后端\flaskProject\Image', "ltt.jpg")
    return "okk"


if __name__ == '__main__':
    app.run()
