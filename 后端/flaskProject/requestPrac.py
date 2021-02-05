from flask import Flask, jsonify, render_template, Response

app = Flask(__name__)


@app.route('/text')
def get_text():
    return '返回文本'


@app.route('/dict')
def get_dict():
    return {'state': 0}


@app.route('/json')
def get_json():
    return jsonify({'state': 0})


@app.route('/html')
def get_html():
    return render_template('index.html')


@app.route('/response')
def get_resonponse():
    return Response('Not Found', status=404)


if __name__ == '__main__':
    app.run(port=5566)
