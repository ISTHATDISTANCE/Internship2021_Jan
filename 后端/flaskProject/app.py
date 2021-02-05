from flask import Flask, render_template, Response, request, redirect

app = Flask(__name__)


@app.route("/", methods=['get'])
def welcome():
    return render_template('welcome.html', name='小明ming')


@app.route("/image")
def image():
    f = open("Image/ltt.jpg", 'rb')
    resp = Response(f.read(), mimetype="image/jpeg")
    return resp


@app.route('/login', methods=['GET', 'POST'])
def do_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        password = request.form['password']
        if name == 'python':
            return render_template('index.html', name=name)
        else:
            return redirect('/login')


if __name__ == '__main__':
    app.run()
